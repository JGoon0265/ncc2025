from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(os.getcwd())))
file_path='bullsonparade.txt'
with open(file_path,'rt',encoding='UTF8') as f :
    read_file = f.read()

tts = gTTS(text=read_file, lang='en')

tts.save("Bullsonparade.mp3")
playsound("Bullsonparade.mp3")