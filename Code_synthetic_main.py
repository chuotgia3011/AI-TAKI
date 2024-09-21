
from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, AudioFileClip
import tempfile
import os
import uuid
from MergeVideo.creat_video_from_url import create_video_from_list , get_audio_duration
# from creat_video_from_list import create_video_from_list , get_audio_duration

from main_media import main_code
from Analyze.download_file_from_google_drive import download_file_from_google_drive

def merge_videos(video_list, text, audio_file , output_video ):
    # Ví dụ sử dụng:
    # video_list = [video1, video2, video3]

    target_duration = get_audio_duration(audio_file)  # Thời lượng mục tiêu là 30 giây
    # output_video_1 = "output_final_video_openai_gradio.mp4"
    output_video_1 = "%s.mp4" % str(uuid.uuid4())
    final_video = create_video_from_list(video_list, target_duration, output_video_1)
    main_code(output_video_1 , output_video , text , audio_file)
    if os.path.isfile(output_video_1):
         os.remove(output_video_1)
    return output_video


# # # video_list = ["video1.mp4", "video2.mp4", "video3.mp4"]
# video_list = ["https://92d485f5634b6966314be29e79b6d7b0.cdn.bubble.io/f1726279220790x822983329966417500/video3.mp4", "https://92d485f5634b6966314be29e79b6d7b0.cdn.bubble.io/f1726279220790x822983329966417500/video3.mp4"]
# # audio_file = "openai-tts-output.mp3"

# audio_file_url = "https://drive.google.com/file/d/1Vm38VZKEAjjXSM6esZXNsZCds2m09noV/view"

# output = "output_final_video_test_with_gradio"
# audio_file = f"{output}.mp3"
# output_video = f"{output}.mp4"

# download_file_from_google_drive(audio_file_url, f"{output}.mp3")

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

# merge_videos(video_list, text, audio_file , output_video )

