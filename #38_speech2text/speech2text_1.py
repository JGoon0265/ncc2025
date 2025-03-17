import speech_recognition as sr

try:
    while True:
        r=sr.Recognizer()

        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio=r.listen(source)
        try:
            print("음성변환: "+r.recognize_google(audio, language="ko-KR"))
        except sr.UnknownValueError:
            print("오디오를 이해할 수 없습니다.")
        except sr.RequestError as e:
            print("에러가 발생하였습니다. 원인: {e}")

except KeyboardInterrupt:
    pass