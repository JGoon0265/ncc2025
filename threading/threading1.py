import threading
import time

def thread_1():
    while True:
        print("쓰레드1 동작")  ##해당 쓰레드를 무한루프프
        time.sleep(1.0)

def thread_2():
    while True:
        print("쓰레드2 동작")
        time.sleep(3.0)


t1=threading.Thread(target=thread_1)
t1.start()
t2=threading.Thread(target=thread_2)
t2.start()

while True:
    print("메인 동작")
    time.sleep(2.0)