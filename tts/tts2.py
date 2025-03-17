from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(os.path.abspath(__file__))))

text="안녕깔라똘라"

tts=gTTS(text=text,lang='ko')
tts.save("hi2.mp3")
playsound("hi2.mp3")