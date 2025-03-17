import pyautogui
import time
import pyperclip
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

Finance_list = ["KOSPI","KOSDAQ","KOSPI200"]

sch_x=1544  #검색창 좌표
sch_y=188

KOSPI_x=1807
KOSPI_y=504

KOSDAQ_x=1807
KOSDAQ_y=834

KOSPI200_x=1807
KOSPI200_y=878

Finance_x=[KOSPI_x,KOSDAQ_x,KOSPI200_x]
Finance_y=[KOSPI_y,KOSDAQ_y,KOSPI200_y]

start_x=1441
start_y=420
end_x=1825
end_y=906

for i in range(0,len(Finance_list)):
    pyautogui.moveTo(Finance_x[i],Finance_y[i])
    time.sleep(0.5)
    저장경로='.\\'+ Finance_list[i]+'.png'
    pyautogui.screenshot(저장경로,region=(start_x,start_y,end_x-start_x,end_y-start_y))
    time.sleep(1)


#삼성전자 검색하기
pyautogui.moveTo(sch_x,sch_y,1)
time.sleep(0.1)
pyautogui.click()
time.sleep(1)
pyautogui.write("tkatjdwjswk",interval=0.1)
pyautogui.write(["enter"])
time.sleep(1)