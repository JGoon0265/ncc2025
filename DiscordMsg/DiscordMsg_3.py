import requests
import os
import json
from dotenv import load_dotenv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists("discord_hook.env"):
    print("환경 변수 파일 (discord_hook.env) 이 존재하지 않습니다.")
    exit()

load_dotenv("discord_hook.env")


def send_discord_msg(webhook_url,msg):
    headers={
        "Content-Type":"application/json"
    }
    json_data={
        "content":msg
    }
    response=requests.post(webhook_url,headers=headers,json=json_data)

    if response.status_code == 204:
        print("메시지가 성공적으로 전송되었습니다!")
    else:
        print(f"오류 발생: {response.status_code}, {response.text}")

webhook_url=os.getenv("DISCORD_WEBHOOK_URL")
message=input("메시지를 입력하세요 : ")
send_discord_msg(webhook_url,message)