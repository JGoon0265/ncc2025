import requests
import re

url=input("URL을 입력하세요: ")

headers={
    'user-Agent':'Mozilla/5.0',
    'Content-Type':'text/html; charset=utf-8'
}

response=requests.get(url,headers=headers)

results=re.findall(r'[\w\.-]+@[\w\.-]+',response.text)
# [\w\.-]+: 문자 클래스=
# # \w:  영문자, 숫자, 밑줄을 의미하고, aaa@bbb.com
# # \.:  마침표, \-는 하이픈을 의미합니다.
# # + : 는 앞의 문자 클래스가 하나 이상 반복됨을 나타냅니다.
# # 즉, 이 부분은 이메일 주소의 로컬 부분(예: user.name)을 나타냅니다.
results=list(set(results))

print(results)