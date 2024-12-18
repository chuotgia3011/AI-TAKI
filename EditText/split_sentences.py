def split_sentences(text, max_words=7, min_words=2):
    sentences = text.split('.')
    result = []

    for sentence in sentences:
        words = sentence.strip().split()
        if not words:
            continue
        current_sentence = []
        for word in words:
            current_sentence.append(word)
            if len(current_sentence) == max_words:
                result.append(" ".join(current_sentence).strip())
                current_sentence = []
        if current_sentence and len(current_sentence) >= min_words:
            result.append(" ".join(current_sentence).strip())
    
    # Loại bỏ các khoảng trống không cần thiết
    result = [sent.strip() + "." if text.endswith(".") else sent.strip() for sent in result]
    
    return result

# # Test với đoạn text
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

# # Chia text thành các câu
# split_text = split_sentences(text)
# for s in split_text:
#     print(s)
