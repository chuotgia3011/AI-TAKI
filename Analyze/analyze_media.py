# from gtts import gTTS
from pydub import AudioSegment
import numpy as np

def analyze_audio_for_sentences(audio_file, sentence_list):
    """Phân tích âm thanh để lấy thời gian bắt đầu của từng câu."""
    # Đọc file âm thanh
    audio = AudioSegment.from_file(audio_file)
    duration = len(audio) / 1000.0  # Chuyển đổi từ milliseconds sang seconds
    
    # Tính độ dài của từng câu dựa trên số ký tự (hoặc có thể thay bằng số từ)
    sentence_lengths = [len(sentence) for sentence in sentence_list]
    total_length = sum(sentence_lengths)  # Tổng độ dài của tất cả các câu
    
    # Tính toán thời gian bắt đầu cho từng câu dựa trên tỷ lệ độ dài
    timings = []
    current_time = 0
    for length in sentence_lengths:
        sentence_duration = (length / total_length) * duration
        timings.append(current_time)
        current_time += sentence_duration
    timings.append(duration)
    # timings = timings[1:]
    return timings

def analyze_audio(audio_file, text_list):
    """Phân tích âm thanh để lấy thời gian bắt đầu của từng từ."""
    audio = AudioSegment.from_file(audio_file)
    duration = len(audio) / 1000.0  # Chuyển đổi từ milliseconds sang seconds
    
    return np.linspace(0, duration, len(text_list)).tolist()


# # Ví dụ sử dụng
# sentence_list = [
#     "Đây là câu đầu tiên.",
#     "Đây là câu thứ hai.",
#     "Câu này dài hơn một chút để có sự khác biệt."
# ]

# audio_file = "output_audio.mp3"
# timings = analyze_audio_for_sentences(audio_file, sentence_list)
# print(timings)
