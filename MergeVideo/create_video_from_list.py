from moviepy.editor import VideoFileClip, concatenate_videoclips

def create_video_from_list(video_list, target_duration, output_video):
    """
    Hàm ghép các video trong danh sách cho đến khi đạt được độ dài mục tiêu.
    Nếu không đủ độ dài, các video sẽ được lặp lại cho đến khi đủ.
    
    :param video_list: Danh sách các video (đường dẫn tới các video)
    :param target_duration: Độ dài mục tiêu (tính bằng giây)
    :param output_video: Đường dẫn để lưu video đầu ra
    """
    
    # Danh sách để chứa các video clip đã load
    video_clips = []
    
    # Tổng độ dài của video hiện tại
    current_duration = 0
    
    # Chỉ số video trong danh sách
    video_index = 0
    
    while current_duration < target_duration:
        # Lấy video tại chỉ số hiện tại, sau đó tăng chỉ số lên
        video_path = video_list[video_index % len(video_list)]  # Lặp lại video nếu hết danh sách
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
    print ("final_video" , final_video , type(final_video))
    # # Lưu video kết quả
    final_video.write_videofile(output_video, fps=24)
    
    # Đóng các file video clip để giải phóng tài nguyên
    for clip in video_clips:
        clip.close()
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

# # Ví dụ sử dụng:
# video_list = ["video1.mp4", "video2.mp4", "video3.mp4"]
# audio_file = "openai-tts-output.mp3" # 60 
# target_duration = get_audio_duration(audio_file)  # Thời lượng mục tiêu là 30 giây
# output_video = "output_final_video_openai.mp4"

# create_video_from_list(video_list, target_duration, output_video)
