import requests
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import tempfile

def download_video(url):
    """
    Hàm tải video từ URL và lưu vào một file tạm.
    
    :param url: Đường dẫn URL của video
    :return: Đường dẫn đến file video tạm
    """
    response = requests.get(url, stream=True)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    
    with open(temp_file.name, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    
    return temp_file.name

def create_video_from_list(video_list, target_duration, output_video):
    """
    Hàm ghép các video từ URL trong danh sách cho đến khi đạt được độ dài mục tiêu.
    Nếu không đủ độ dài, các video sẽ được lặp lại cho đến khi đủ.
    
    :param video_list: Danh sách các video (URL tới các video)
    :param target_duration: Độ dài mục tiêu (tính bằng giây)
    :param output_video: Đường dẫn để lưu video đầu ra
    """
    
    # Danh sách để chứa các video clip đã load
    video_clips = []
    
    # Tổng độ dài của video hiện tại
    current_duration = 0
    
    # Chỉ số video trong danh sách
    video_index = 0
    
    # Danh sách tệp tạm để lưu các video tải về
    temp_files = []
    
    while current_duration < target_duration:
        # Tải video từ URL và lưu vào file tạm
        video_url = video_list[video_index % len(video_list)]  # Lặp lại video nếu hết danh sách
        video_path = download_video(video_url)
        temp_files.append(video_path)  # Lưu đường dẫn file tạm để sau này xóa
        
        video_clip = VideoFileClip(video_path)
        
        # Tính toán thời lượng còn thiếu
        remaining_duration = target_duration - current_duration
        
        if video_clip.duration > remaining_duration:
            # Nếu video dài hơn thời gian còn thiếu, chỉ cắt lấy phần cần thiết
            video_clip = video_clip.subclip(0, remaining_duration)
        
        # Thêm video vào danh sách và cập nhật độ dài hiện tại
        video_clips.append(video_clip)
        current_duration += video_clip.duration
        
        # Tăng chỉ số, nếu hết danh sách thì bắt đầu lại từ video đầu tiên
        video_index += 1
    
    # Kết hợp tất cả các video clip
    final_video = concatenate_videoclips(video_clips)
    
    # Lưu video kết quả
    final_video.write_videofile(output_video, fps=24)
    
    # Đóng các file video clip để giải phóng tài nguyên
    for clip in video_clips:
        clip.close()
    
    # Xóa các tệp tạm
    for file in temp_files:
        os.remove(file)

    return final_video      

from pydub import AudioSegment

def get_audio_duration(audio_file):
    """
    Hàm lấy độ dài của file âm thanh MP3.
    
    :param audio_file: Đường dẫn đến file âm thanh MP3.
    :return: Thời gian của file âm thanh (tính bằng giây).
    """
    audio = AudioSegment.from_file(audio_file)
    return len(audio) / 1000.0  # Đổi từ milliseconds sang second

# import requests
# from pydub import AudioSegment
# from io import BytesIO

# def get_audio_duration(url):
#     """
#     Hàm lấy độ dài của file âm thanh MP3 từ URL.

#     :param url: URL đến file âm thanh MP3.
#     :return: Thời gian của file âm thanh (tính bằng giây).
#     """
    
#     # If the url is a google drive link, modify it to get the direct download link
#     if 'drive.google.com' in url:
#         file_id = url.split('/')[-2]
#         download_url = f'https://drive.google.com/uc?export=download&id={file_id}'
#     else:
#         download_url = url
    
#     # Tải file âm thanh từ URL
#     response = requests.get(download_url)
#     response.raise_for_status()  # Đảm bảo yêu cầu thành công

#     # Chuyển đổi nội dung tải về thành đối tượng BytesIO
#     audio_file = BytesIO(response.content)

#     # Đọc âm thanh từ BytesIO
#     audio = AudioSegment.from_file(audio_file, format="mp3")

#     # Trả về độ dài của âm thanh (tính bằng giây)
#     return len(audio) / 1000.0

# # Ví dụ sử dụng:
# video_list = ["https://92d485f5634b6966314be29e79b6d7b0.cdn.bubble.io/f1726279220790x822983329966417500/video3.mp4", "https://92d485f5634b6966314be29e79b6d7b0.cdn.bubble.io/f1726279220790x822983329966417500/video3.mp4"]
# # audio_file = "openai-tts-output.mp3" 
# audio_file = "https://drive.google.com/file/d/1Vm38VZKEAjjXSM6esZXNsZCds2m09noV/view"
# target_duration = get_audio_duration(audio_file)  
# output_video = "output_final_video_openai.mp4"

# create_video_from_list(video_list, target_duration, output_video)   
