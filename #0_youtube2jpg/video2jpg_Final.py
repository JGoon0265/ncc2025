from PyQt5 import QtWidgets
import sys
sys.path.append("C:\2025ncc\ncc_python\#0_youtube2jpg")
from youtube_down import Ui_Form
import cv2
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from tkinter import messagebox

class VideoDownloader(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.process)



    def youtube_downloader(self, url):
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            ys = yt.streams.get_highest_resolution()
            ys.download()
            messagebox.showinfo("Download Complete", f"Video '{yt.title}' has been downloaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mp4tojpg(self, filepath):
        if not os.path.exists(filepath):
            messagebox.showwarning("File Not Found", f"Could not find file: {filepath}")
            return

        video = cv2.VideoCapture(filepath)
        if not video.isOpened():
            messagebox.showwarning("Error", f"Could not open file: {filepath}")
            return

        fps = int(video.get(cv2.CAP_PROP_FPS)) or 30
        save_folder = filepath[:-4]
        os.makedirs(save_folder, exist_ok=True)

        count = 0
        while True:
            ret, frame = video.read()
            if not ret:
                break

            frame_id = int(video.get(cv2.CAP_PROP_POS_FRAMES))
            if frame_id % fps == 0:
                filename = os.path.join(save_folder, f"frame{count}.jpg")
                cv2.imwrite(filename, frame)
                count += 1

        video.release()
        messagebox.showinfo("Completed", f"Frames extracted successfully! {count} frames saved.")

    def process(self):
        text_input = self.lineEdit.text().strip()
        
        if not text_input:
            messagebox.showwarning("Input Required", "Please enter a valid URL or filename!")
            return
        
        if self.radioButton.isChecked():  # 영상 다운로드 선택
            self.youtube_downloader(text_input)
        elif self.radioButton_2.isChecked():  # 프레임 캡처 선택
            self.mp4tojpg(text_input)
        else:
            messagebox.showwarning("Selection Required", "Please select an option!")

            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VideoDownloader()
    window.show()
    sys.exit(app.exec_())
