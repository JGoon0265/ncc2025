import numpy as np
import cv2

class FaceHide: # Class 선언, 아래 함수선언들은 메서드 선언.
    def __init__(self, image_path, scale_factor=0.4, pixelation_factor=0.05):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.image_path = image_path
        self.scale_factor = scale_factor
        self.pixelation_factor = pixelation_factor
        self.img = self.load_image()

    def load_image(self):
        ff = np.fromfile(self.image_path, np.uint8)
        img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, dsize=(0, 0), fx=self.scale_factor, fy=self.scale_factor, interpolation=cv2.INTER_LINEAR)
        return img

    def detect_faces(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.2, 5)
        return faces

    def Hide_faces(self):
        faces = self.detect_faces()
        for (x, y, w, h) in faces:
            face_image = self.img[y:y+h, x:x+w]
            face_image = cv2.resize(face_image, dsize=(0, 0), fx=self.pixelation_factor, fy=self.pixelation_factor)
            face_image = cv2.resize(face_image, (w, h), interpolation=cv2.INTER_AREA)
            self.img[y:y+h, x:x+w] = face_image
    
    def show_image(self):
        cv2.imshow('Face Pixelator', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    img_path = r'C:\2025ncc\2025ncc\#23_face_recog\group.png'
    pixelator = FaceHide(img_path) # 요놈이 객체, 메모리 위에서 동작하면 Instance
    pixelator.Hide_faces()
    pixelator.show_image()

