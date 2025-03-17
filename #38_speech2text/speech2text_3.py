# pip install playsound==1.2.2
# pip install pyaudio
# pip install SpeechRecognition
import speech_recognition as sr

class Speech2text:
    def __init__(self, language='ko-KR'):
        self.recognizer=sr.Recognizer()
        self.language=language

    def process_audio(self):
        try:
            with sr.Microphone() as source:
                print("음성을 입력하세요.")
                audio = self.recognizer.listen(source)
            
            stt=self.recognizer.recognize_google(audio,language=self.language)
            print("음성변환: "+stt)
            self.handle_keywords(stt)

        except sr.UnknownValueError:
            print("오디오를 이해할 수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생했습니다. 원인: {e}")

    def handle_keywords(self, text):
        if "안녕" in text:
            print("네, 안녕하세요!")
        elif "날씨" in text:
            print("정말 날씨가 좋네요")
        
        #필요한 다른 키워드 처리 추가


    def run(self):
        """음성 인식 프로세스를 계속 실행합니다."""
        try:
            while True:
                self.process_audio()
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")

if __name__=="__main__":
    processor=Speech2text(language='ko-KR')
    processor.run()