# Required libraries
import tkinter as tk
from tkinter import simpledialog, messagebox
from pytubefix import YouTube
from pytubefix.cli import on_progress

# 유튜브 영상 다운로드
def youtube_downloader(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)  # YouTube 오브젝트
        print(f"Title: {yt.title}")  # 터미널에 유튜브 제목 출력력
        ys = yt.streams.get_highest_resolution()  # 해상도 최대로로
        ys.download()  # 비디오 다운로드드
        messagebox.showinfo("Download Complete", f"Video '{yt.title}' has been downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# url 인풋을 위한 윈도우 만들기기
def get_url():
    root = tk.Tk()
    root.withdraw()  # tk.Tk 루트 윈도우 가리기
    url = simpledialog.askstring("YouTube Downloader", "Enter the YouTube URL:")
    
    if url:
        youtube_downloader(url)
    else:
        messagebox.showwarning("Input Required", "Please enter a valid URL!")

if __name__ == "__main__":
    get_url()

# exe파일로 만들어서 배포하기 [pyinstaller]
# C:\Users\sys\Desktop\openCV\youtube_downloader_win.py
# $ python -m pip install pyinstaller
# $ python -m PyInstaller --onefile 
#          --windowed youtube_downloader_win.py
## (PyInstaller 대소문자 구별)
# .exe 파일은 dist 폴더 안에 생성됩니다.