# webhook:
# https://discord.com/api/webhooks/1344102714912538705/ivOz5q3aDzRM_yLGyNHhwhakWAq1hEHSuDbkBxzj772a4XP2WAzRuozUbS7uEW5HjuZ1

import os
import requests
import json
from dotenv import load_dotenv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
load_dotenv("discord_hook.env")

webhook_url=os.getenv("DISCORD_WEBHOOK_URL")

json_data={
    "embeds": [{
        "title": f"네이버",
        "description": f'구글보다 좋다, 네이버',
        "url": f"https://www.naver.com",
        "thumbnail":{
            "url":f"https://i.namu.wiki/i/PkRVi8MTHhOTT8oibG4ULP2VYCgYFi_MBnjTWwjg-5PzWBOnEf5hVY6XORUKeI95k3qFdtRNctWHsuRqWW6Pkl35OlY1Q5Q0D-rFCx452GHXIdIUoRncijUwKZVeXeNBkbAMfsuK-az__8X0jTBUVg.svg"
        }
    }]
}

if webhook_url:
    response = requests.post(webhook_url,json=json_data)
    if response.status_code == 204:
        print("성공적으로 메시지가 출력되었습니다.")
    else:
        print(f'오류 발생:{response.status_code},{response.text}')
else:
    print("webhook url 설정 오류")