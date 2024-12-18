import os.path
import uuid

from fastapi import FastAPI
import uvicorn
import requests
from code_synthetic_main import merge_videos
from pydantic import BaseModel
from Analyze.download_file_from_google_drive import download_file_from_google_drive

# Tạo một ứng dụng FastAPI
app = FastAPI()

output_dir = '/opt/cdn/cdn.aiauto.io/videos/'
# output_dir = 'ResultVideo/'
cdn_base_name = 'https://cdn.aiauto.io/videos/'
# # Định nghĩa route đơn giản in ra "Hello, World!"
# @app.post("/")
# def hello_world(input):
#     input_text = input.text
#     return {"message": f"Hello {input_text}"}

# # Hàm main để chạy ứng dụng FastAPI
# def main():
#     # Chạy ứng dụng FastAPI với Uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# # Kiểm tra nếu script đang chạy trực tiếp thì gọi hàm main()
# if __name__ == "__main__":
#     main()

# Model cho dữ liệu đầu vào
class InputData(BaseModel):
    list_background: list
    background_music: str
    content: str
    file_name: str


# Route POST để nhận JSON và in ra dữ liệu
@app.post("/process/")
def process_data(input_data: InputData):
    try:

        # Trích xuất dữ liệu từ JSON
        backgrounds = input_data.list_background
        music = input_data.background_music
        content = input_data.content
        file_name = input_data.file_name

        # In ra các giá trị đã nhận
        print("Background videos:", backgrounds)
        print("Background music:", music)
        print("Content:", content)
        # output = "output_final_video_test_with_gradio"
        # audio_file = f"{file_name}.mp3"
        audio_file = "%s.mp3" % str(uuid.uuid4())
        output_file_name = "%s.mp4" % str(uuid.uuid4())
        output_video = os.path.join(output_dir, output_file_name)
        

        download_file_from_google_drive(music, audio_file)

        merge_videos(backgrounds, content, audio_file, output_video)
        if os.path.isfile(audio_file):
            os.remove(audio_file)

        # Trả về phản hồi
        return {
            "message": "Data processed successfully",
            "backgrounds": backgrounds,
            "music": music,
            "content": content,
            "file": cdn_base_name + output_file_name
        }
    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}


# Hàm main để chạy ứng dụng
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
