import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound
import googletrans
import os

#경로 기본값 지정
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def translate_and_speak():
    str1 = entry.get() #TKInter, input값을 갖고오기
    if not str1.strip():
        messagebox.showerror("입력 오류", "번역할 내용을 입력하세요.")
        return
    try:
        translator = googletrans.Translator()
        result1 = translator.translate(str1, dest='ja').text
        output_label.config(text=f'번역: {result1}')
        
        tts = gTTS(text=result1, lang="en")
        filename = "result.mp3"
        tts.save(filename)
        playsound(filename)
    #예외 처리 : 오류 출력
    except Exception as e:
        messagebox.showerror("오류 발생", f"에러: {e}")

# GUI 설정
# 기본 윈도우 설정. title은 제목
window = tk.Tk()
window.title("일본말에 자신있는 미국인 번역기")
window.geometry("400x200")

# entry : Entry 위젯(입력 필드 생성)
entry_label = tk.Label(window, text="번역할 내용을 입력하세요:")
entry_label.pack()
entry = tk.Entry(window, width=50)
entry.pack()

# 버튼 생성 & 앞에 정의된 함수 트리거거
translate_button = tk.Button(window, text="번역 및 음성 출력", command=translate_and_speak)
translate_button.pack()

# 번역 결과 문장 출력
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()


# $ python -m PyInstaller --onefile --windowed trans_exe.py
# $ python -m PyInstaller --icon="translator.png" --onefile --windowed trans_exe.py