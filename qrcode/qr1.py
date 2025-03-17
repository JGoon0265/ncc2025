import qrcode
import os

os.chdir(os.path.dirname(os.path.abspath(os.getcwd())))
qr_data='www.naver.com'
qr_img=qrcode.make(qr_data)

save_path='4. qrcodemaker'+qr_data+'.png'
qr_img.save(save_path)
