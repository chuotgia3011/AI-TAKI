import random
from pyvi import ViTokenizer

from Analyze.analyze_media import analyze_audio_for_sentences

import random

def select_random_pairs_with_underscore(words, num_pairs=3):
    """
    Chọn ngẫu nhiên một số từ từ danh sách, chỉ chọn các từ có dấu gạch dưới (_).
    
    :param words: Danh sách các từ.
    :param num_pairs: Số lượng từ cần chọn.
    :return: Một danh sách các từ được chọn.
    """
    # Lọc các từ có chứa dấu gạch dưới
    underscore_words = [word for word in words if '_' in word]
    
    # Chọn ngẫu nhiên số từ cần thiết
    selected_words = random.sample(underscore_words, min(num_pairs, len(underscore_words)))
    
    return selected_words


def extract_word_pairs(text, num_pairs=3):
    """
    Tách đoạn văn bản thành các câu, sau đó chọn ra ít nhất 3 từ đôi từ mỗi câu.
    
    :param text: Đoạn văn bản cần xử lý.
    :param num_pairs: Số lượng từ đôi cần chọn từ mỗi câu.
    :return: Một danh sách các từ đôi từ mỗi câu.
    """
    # Tách đoạn văn bản thành các câu
    sentences = text.split('. ')
    # print (sentences)
    word_pairs_per_sentence = []
    
    for sentence in sentences:
        # Token hóa từng câu thành danh sách các từ
        words = ViTokenizer.tokenize(sentence).split()
        # print(words)
        res = select_random_pairs_with_underscore(words)
        for word in res:
            word_res = word.replace("_" , " ")
            word_pairs_per_sentence.append(word_res)
    
    return word_pairs_per_sentence

# # Ví dụ sử dụng hàm
 
# text = """Sức mạnh của kỷ luật không chỉ nằm ở việc hoàn thành công việc mà còn ở cách chúng ta hoàn thiện bản thân mỗi ngày. 
# Kỷ luật là nền tảng để phát triển bản thân, giúp chúng ta kiểm soát được hành vi, tư duy và cảm xúc của mình. 
# Khi chúng ta giữ vững kỷ luật trong từng hành động, chúng ta trở nên kiên trì hơn, tự tin hơn và thành công hơn. 
# Kỷ luật không phải là sự gượng ép, nó là sự lựa chọn thông minh. 
# Những người thành công đều biết tầm quan trọng của việc đặt ra mục tiêu cụ thể và kiên trì thực hiện chúng mỗi ngày. 
# Chúng ta dễ bị cám dỗ bởi những thú vui ngay trước mắt, nhưng chỉ có kỷ luật mới giúp chúng ta vượt qua những khó khăn đó để đạt được thành công dài hạn.
# Hãy bắt đầu từ những việc nhỏ nhặt nhất như dậy sớm, tập thể dục, học tập hay làm việc một cách đều đặn. 
# Sự thay đổi lớn lao luôn bắt đầu từ những thói quen nhỏ bé nhưng kiên định. 
# Sống có kỷ luật không chỉ giúp bạn đạt được ước mơ mà còn rèn luyện ý chí mạnh mẽ, tạo nên một cuộc sống có ý nghĩa và hạnh phúc hơn. 
# Hãy nhớ rằng, sức mạnh của kỷ luật chính là chìa khóa mở ra cánh cửa thành công và sự hoàn thiện bản thân."""

# # Gọi hàm
# result = extract_word_pairs(text)
# print(result)
