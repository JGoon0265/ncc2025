import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    try:
        seconds = int(entry.get())
        countdown(seconds)
    except ValueError:
        messagebox.showerror("오류", "숫자를 입력하세요!")

def countdown(seconds):
    for i in range(seconds, -1, -1):
        timer_label.config(text=f"남은 시간: {i}초")
        root.update()
        time.sleep(1)
    messagebox.showinfo("완료", "타이머 종료!")

# GUI 설정
root = tk.Tk()
root.title("타이머")
root.geometry("300x150")

# 입력 필드
entry_label = tk.Label(root, text="시간(초) 입력:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# 시작 버튼
start_button = tk.Button(root, text="시작", command=start_timer)
start_button.pack()

# 타이머 표시 라벨
timer_label = tk.Label(root, text="")
timer_label.pack()

root.mainloop()
