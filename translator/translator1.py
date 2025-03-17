# pip install legacy-cgi
# pip install googletrans==4.0.0-rc1
import googletrans
from gtts import gTTS
from playsound import playsound
import os

transl=googletrans.Translator()
str1=input("번역할 내용을 입력하세요: ")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

###일본어 공부한 미국인이 영어 억양으로 일본어 쓰는 일어 번역기
try:
    result1=transl.translate(str1, dest='japanese', src='auto')
    print(f'{str1} => {result1.text}')
    tts = gTTS(text=result1.text, lang="en")
    tts.save("thanks.mp3")
    playsound("thanks.mp3")
except AttributeError:
    print("Sth went wrong. try again, noob. :D")