# pip install playsound==1.2.2
# pip install pyaudio
# pip install SpeechRecognition
import speech_recognition as sr

try:
    while True:
        r=sr.Recognizer()

        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio=r.listen(source)
        try:
            stt=r.recognize_google(audio, language="ko-KR")
            print("음성변환: "+stt)
            if "안녕" in stt:
                print("네 안녕하세요?")
            elif "날씨" in stt:
                print("날씨가 정말 좋네요")

        except sr.UnknownValueError:
            print("오디오를 이해할 수 없습니다.")
        except sr.RequestError as e:
            print("에러가 발생하였습니다. 원인: {e}")

except KeyboardInterrupt:
    pass