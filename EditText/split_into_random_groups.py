import random
def split_into_random_groups(sentences):
    
    groups = []
    
    while sentences:
        # Chọn ngẫu nhiên số câu từ 1 đến 3
        num_sentences = random.randint(1, min(3, len(sentences)))
        # Tạo nhóm và loại bỏ các câu đã chọn khỏi danh sách
        group = sentences[:num_sentences]
        groups.append(group)
        sentences = sentences[num_sentences:]
        # print (group )
    
    return groups