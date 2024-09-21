
import random
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip , AudioFileClip
from EditText.split_sentences import split_sentences
from Analyze.analyze_media import analyze_audio_for_sentences
from EditText.split_into_random_groups import split_into_random_groups
from add_text_to_video import add_list_of_texts_with_special_words_color
from EditText.select_random_specialword import extract_word_pairs

# input_video = "output_final_video_openai.mp4"  # Video nền có sẵn
# output_video = "output_final_video_test.mp4"
# audio_file = "openai-tts-output.mp3" 
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

list_color=["red", "blue", "green", "yellow", "orange"]

def main_code(input_video , output_video , text , audio_file):
    sentence_list = split_sentences(text)
    special_words = extract_word_pairs(text)
    
    list_time = analyze_audio_for_sentences(audio_file, sentence_list)
    list_time_intervals = []
    result = split_into_random_groups(sentence_list)
    
    random_màu = random.sample(list_color, 2)
    start_pos = 0
    for i,group in enumerate(result):
        # print(group)
        start = start_pos
        end = start  + len(group) 
        start_pos += len(group)
        
        start_time = list_time[start]
        end_time = list_time[end]
        list_time_intervals.append((start_time,end_time))
    list_texts = result
    print ("input_video main code :" , input_video)
    add_list_of_texts_with_special_words_color(input_video, output_video, list_texts, list_time_intervals, audio_file , special_words=special_words, list_color=random_màu)


# main_code(input_video , output_video , text , audio_file)