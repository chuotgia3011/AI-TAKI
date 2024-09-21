import requests

def download_file_from_google_drive(share_url, destination):
    """
    Tải file từ Google Drive và lưu vào đích.
    
    :param share_url: Đường dẫn chia sẻ của file trên Google Drive.
    :param destination: Đường dẫn lưu file sau khi tải.
    """
    # Chuyển đổi URL chia sẻ thành file ID
    file_id = share_url.split('/d/')[1].split('/')[0]
    
    # URL tải file từ Google Drive
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    
    # Gửi yêu cầu tải file
    response = requests.get(download_url, stream=True)
    response.raise_for_status()  # Đảm bảo yêu cầu thành công

    # Lưu nội dung vào file
    with open(destination, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)