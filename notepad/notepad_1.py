from tkinter import *
from tkinter.filedialog import *

#함수 정의
def new_file():
    text_area.delete(1.0,END)

def save_file():
    f = asksaveasfile(mode="w",defaultextension=".txt",filetypes=[('Text files','.txt')])
    text_save=str(text_area.get(1.0,END))
    f.write(text_save)
    f.close()

def maker():
    help_view=Toplevel(window)
    help_view.geometry("300x50+800+300")
    help_view.title("만든이")
    lb=Label(help_view,text="파이썬과 40개의 작품들 메모장 만들기 입니다.")
    lb.pack()

# 윈도우 지정
window =Tk()
window.title("메모장")
window.geometry("400x400+800+300")
window.resizable(False,False)
# 메뉴 만들기
menu = Menu(window)
menu_1 = Menu(menu,tearoff=0)
menu_1.add_command(label="새파일",command=new_file)
menu_1.add_command(label="저장",command=save_file)
menu_1.add_separator()
menu_1.add_command(label="종료",command=window.destroy)
menu.add_cascade(label="파일",menu=menu_1)
# 만든이 메뉴
menu_2=Menu(menu,tearoff=0)
menu_2.add_command(label="만든이",command=maker)
menu.add_cascade(label="만든이",menu=menu_2)
# 텍스트 구역 지정
text_area=Text(window)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N+E+S+W)

# 윈도우 설정 불러오기
window.config(menu=menu)
# 실행
window.mainloop()

##python -m PyInstaller --onefile --windowed notepad.py