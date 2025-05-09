import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

ff=np.fromfile(r'C:\2025ncc\2025ncc\#23_face_recog\group.png',np.uint8)
img=cv2.imdecode(ff,cv2.IMREAD_UNCHANGED)
img=cv2.resize(img,dsize=(0,0),fx=0.4,fy=0.4,interpolation=cv2.INTER_LINEAR)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.2,5)
for (x,y,w,h) in faces:
    face_image=img[y:y+h,x:x+w]
    face_image=cv2.resize(face_image,dsize=(0,0), fx=0.05,fy=0.05)
    face_image=cv2.resize(face_image,(w,h),interpolation=cv2.INTER_AREA)
    img[y:y+h,x:x+w]=face_image

cv2.imshow('face find',img)
cv2.waitKey(0)
cv2.destroyAllWindows