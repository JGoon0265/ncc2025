# webhook:
# https://discord.com/api/webhooks/1344102714912538705/ivOz5q3aDzRM_yLGyNHhwhakWAq1hEHSuDbkBxzj772a4XP2WAzRuozUbS7uEW5HjuZ1

import requests
import json

headers = {
    "Content-Type": "application/json"
}
json_data={
    "content": "이것은 입에서 나는 소리가 아니여" 
}
requests.post("https://discord.com/api/webhooks/1344222519435067443/1VUoE8ZmpWL2ttE0K3oQBhlotqk6zvT8KDckYtLzo6YRRZb2OmG8axg6pNiySQwwQk3b",headers=headers,json=json_data)