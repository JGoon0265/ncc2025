import smtplib
from email.mime.text import MIMEText


send_email='hidae0@naver.com'
send_pwd='070355az!@'

recv_email='jaeminjjeong@gmail.com'

smtp_name='smtp.naver.com'
smtp_port=465

#여기에 메일 내용 입력. 여러줄 가능
text= """
반갑습니다
혹 수신하시면 hidae0@naver.com 으로 회신부탁드립니다.
"""

msg=MIMEText(text)

msg['Subject']="반갑습니다"#메일제목
msg['From']=send_email
msg['To']=recv_email
print(msg.as_string())

s=smtplib.SMTP(smtp_name,smtp_port)
t=smtplib.SMTP_SSL(smtp_name,smtp_port)
#s.starttls()
#s.login(send_email,send_pwd)
s.sendmail(send_email,recv_email,msg.as_string)
s.quit()