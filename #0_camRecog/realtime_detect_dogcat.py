from ultralytics import YOLO
import cv2
import math

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# load YOLO model
model=YOLO('yolo11l.pt')


while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame.")
        break
    
    # Yolo 모델을 프레임에서 실행
    results = model(img,stream=True)

    # 바운드할 영역과 레이블 지정
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2) # int로 변수형태 변경

            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)

            confidence=math.ceil((box.conf[0]*100))/100
            print("Confidence --->", confidence)

            cls=int(box.cls[0])
            class_name=r.names[cls]
            print("Class Name -->", class_name)

            if class_name in ["cat", "dog"]:
                x1,y1,x2,y2=map(int, box.xyxy[0])
                confidence=box.conf[0]

                color=(0,255,0) if class_name == 'dog' else (255,0,0)
                cv2.rectangle(img,(x1,y1),(x2,y2),color,2)

                text=f"{class_name}: {confidence:.2f}"
                cv2.putText(img, text, (x1,y1-10), cv2.FONT_HERSHEY_SIMPLEX,0.5,color,2)


    cv2.imshow('Webcam',img) 
    # q 입력시 나가기
    if cv2.waitKey(1)& 0xFF    == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
