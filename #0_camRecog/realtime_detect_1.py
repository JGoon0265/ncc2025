from ultralytics import YOLO
import cv2
import math

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# load YOLO model
model=YOLO('yolo11l.pt')

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

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
            class_name=classNames[cls]
            print("Class Name -->", class_name)

            org=(x1,y1-10)
            font=cv2.FONT_HERSHEY_SIMPLEX
            fontScale=0.6
            color=(255,0,0)
            thickness=2
            cv2.putText(img,f'{class_name} {confidence}',org,font,fontScale,color,thickness)
    cv2.imshow('Webcam',img) 
    # q 입력시 나가기
    if cv2.waitKey(1)& 0xFF    == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
