import random
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
from split_sentences import split_sentences
from analyze_media import analyze_audio_for_sentences
from split_into_random_groups import split_into_random_groups


def find_phrase_index(text_input, phrase):
    """
    Tìm chỉ số của cụm từ trong danh sách các từ.
    
    :param text_input: Chuỗi văn bản.
    :param phrase: Cụm từ cần tìm.
    :return: Chỉ số của từ đầu tiên của cụm từ trong danh sách, hoặc -1 nếu không tìm thấy.
    """
    tokenized_text = text_input.split(" ")
    phrase_tokens = phrase.split()
    phrase_length = len(phrase_tokens)

    for i in range(len(tokenized_text) - phrase_length + 1):
        if tokenized_text[i:i + phrase_length] == phrase_tokens:
            return i

    return -1


# def add_list_of_texts_with_special_words_color(input_video, output_video, list_texts, list_time_intervals, fontsize=50, default_color='white', special_words=None, list_màu=None, font="/usr/local/share/fonts/roboto/Roboto-Regular.ttf"):

# list_font = ["/usr/local/share/fonts/Anton/Anton-Regular.ttf"]

def add_list_of_texts_with_special_words_color(input_video, output_video, list_texts, list_time_intervals, audio_file,
                                               fontsize=70, default_color='white', special_words=None, list_màu=None,
                                               font="/usr/local/share/fonts/Anton/Anton-Regular.ttf"):
    """
    Thêm nhiều mảng văn bản vào video với các từ đặc biệt được tô màu ngẫu nhiên từ danh sách màu và thời gian xuất hiện tương ứng cho từng mảng.
    
    :param input_video: Đường dẫn đến video đầu vào.
    :param output_video: Đường dẫn đến video đầu ra.
    :param list_texts: Danh sách các mảng chứa các dòng văn bản.
    :param list_time_intervals: Danh sách các khoảng thời gian (start_time, end_time) cho mỗi mảng văn bản.
    :param fontsize: Kích thước phông chữ.
    :param default_color: Màu chữ mặc định.
    :param special_words: Danh sách các từ đặc biệt.
    :param list_màu: Danh sách các màu cho từ đặc biệt, sẽ chọn ngẫu nhiên.
    :param font: Đường dẫn đến phông chữ.
    """
    # background = VideoFileClip(background_video).resize(1080, 1920)
    if special_words is None:
        special_words = []

    if list_màu is None:
        list_màu = ['red']  # Nếu không có danh sách màu, mặc định là màu đỏ

    # Load video clip

    video = VideoFileClip(input_video)

    # Create list to hold text clips
    text_clips = []
    # print 

    # Loop through each group of texts
    for idx, texts in enumerate(list_texts):
        # Lấy khoảng thời gian tương ứng cho mảng văn bản hiện tại
        start_time, end_time = list_time_intervals[idx]

        # Calculate the vertical position for each text clip
        num_texts = len(texts)
        video_height = video.h
        # fontsize = random (50)
        line_spacing = fontsize  ### khoảng cách dòng * 1.5
        center_y = video_height / 2
        start_y = center_y - ((fontsize + line_spacing) * (num_texts - 1)) / 2

        for i, text in enumerate(texts):
            # Calculate the vertical position for each line
            y_pos = start_y + i * (fontsize + line_spacing)

            # Xử lý đoạn văn bản theo từ và cụm từ đặc biệt
            words = text.split(" ")
            line_text_clips = []
            line_width = 0

            # Lưu màu cho các cụm từ đặc biệt để đảm bảo tất cả từ trong cụm có cùng màu
            phrase_color_map = {}

            # Kiểm tra từng từ có phải từ đặc biệt hay không
            for word in words:
                word_color = default_color

                # Kiểm tra cụm từ đặc biệt
                for special_word in special_words:
                    start_index = find_phrase_index(text, special_word)
                    # Chỉ bôi màu nếu từ/cụm từ đặc biệt xuất hiện
                    if start_index != -1 and start_index <= words.index(word) < start_index + len(special_word.split()):
                        if special_word not in phrase_color_map:
                            phrase_color_map[special_word] = random.choice(
                                list_màu)  # Chọn màu ngẫu nhiên cho cụm từ nếu chưa có
                        word_color = phrase_color_map[special_word]
                        break

                # Tạo TextClip cho từng từ
                # word_clip = TextClip(word, fontsize=fontsize, color=word_color, font=font)
                word_clip = TextClip(word, fontsize=fontsize, color=word_color, font=font, stroke_color='black',
                                     stroke_width=1, method='label')
                line_width += word_clip.w + 5  # Add spacing between words

            # Tính vị trí dòng để căn giữa
            x_pos = (video.w - line_width) / 2

            # Thêm từng từ vào video
            for word in words:
                word_color = default_color

                # Kiểm tra cụm từ đặc biệt và gán màu
                for special_word in special_words:
                    start_index = find_phrase_index(text, special_word)
                    if start_index != -1 and start_index <= words.index(word) < start_index + len(special_word.split()):
                        word_color = phrase_color_map[special_word]  # Sử dụng màu đã chọn cho cụm từ
                        break

                word_clip = TextClip(word, fontsize=fontsize, color=word_color, font=font, stroke_color='black',
                                     stroke_width=2, method='label')
                word_clip = word_clip.set_pos((x_pos, y_pos)).set_start(start_time).set_duration(end_time - start_time)
                # text2 = create_text_clip("BẠN CÓ THỂ", fontsize=80, color='white', stroke_color='black', stroke_width=3, font='Arial-Bold', pos=('center', 'center'), start_time=3, duration=3)
                x_pos += word_clip.w + 10

                line_text_clips.append(word_clip)

            text_clips.extend(line_text_clips)

    # Combine video and text clips
    result = CompositeVideoClip([video] + text_clips)
    audio_clip = AudioFileClip(audio_file)
    result = result.set_audio(audio_clip)

    # Write the result to a file
    result.write_videofile(output_video, codec="libx264", fps=24)

# # Sử dụng hàm
# input_video = "output_final_video_openai.mp4"  # Video nền có sẵn
# output_video = "output_final_video_test.mp4"


# text = """
# Sức mạnh của kỷ luật không chỉ nằm ở việc hoàn thành công việc mà còn ở cách chúng ta hoàn thiện bản thân mỗi ngày. 
# Kỷ luật là nền tảng để phát triển bản thân, giúp chúng ta kiểm soát được hành vi, tư duy và cảm xúc của mình. 
# Khi chúng ta giữ vững kỷ luật trong từng hành động, chúng ta trở nên kiên trì hơn, tự tin hơn và thành công hơn. 
# Kỷ luật không phải là sự gượng ép, nó là sự lựa chọn thông minh. 
# Những người thành công đều biết tầm quan trọng của việc đặt ra mục tiêu cụ thể và kiên trì thực hiện chúng mỗi ngày. 
# Chúng ta dễ bị cám dỗ bởi những thú vui ngay trước mắt, nhưng chỉ có kỷ luật mới giúp chúng ta vượt qua những khó khăn đó để đạt được thành công dài hạn.
# Hãy bắt đầu từ những việc nhỏ nhặt nhất như dậy sớm, tập thể dục, học tập hay làm việc một cách đều đặn. 
# Sự thay đổi lớn lao luôn bắt đầu từ những thói quen nhỏ bé nhưng kiên định. 
# Sống có kỷ luật không chỉ giúp bạn đạt được ước mơ mà còn rèn luyện ý chí mạnh mẽ, tạo nên một cuộc sống có ý nghĩa và hạnh phúc hơn. 
# Hãy nhớ rằng, sức mạnh của kỷ luật chính là chìa khóa mở ra cánh cửa thành công và sự hoàn thiện bản thân.
# """


# sentence_list = split_sentences(text)
# audio_file = "openai-tts-output.mp3"   
# list_time = analyze_audio_for_sentences(audio_file, sentence_list)
# list_time_intervals = []
# result = split_into_random_groups(sentence_list)
# start_pos = 0
# for i,group in enumerate(result):
#     # print(group)
#     start = start_pos
#     end = start  + len(group) 
#     start_pos += len(group)

#     start_time = list_time[start]
#     end_time = list_time[end]
#     list_time_intervals.append((start_time,end_time))

# special_words = ["mạnh của", "sự hoàn thiện" , "thói quen nhỏ bé", "cám dỗ bởi những" , "sự gượng ép"]  # Danh sách các từ đặc biệt
# list_màu = ["red", "blue", "green", "yellow"]  # Danh sách các màu ngẫu nhiên


# list_texts = result
# add_list_of_texts_with_special_words_color(input_video, output_video, list_texts, list_time_intervals, audio_file , special_words=special_words, list_màu=list_màu)
