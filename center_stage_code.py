import cv2 as cv 
import numpy as np
capture=cv.VideoCapture(0,apiPreference=cv.CAP_AVFOUNDATION) #for windows use cv.CAP_DSHOW or remove apipreference entirely
if not capture.isOpened():
    print("Error: Could not open video.")
    exit()
haar_cascade=cv.CascadeClassifier('haar_face.xml')
OUTPUT_WIDTH=640
OUTPUT_HEIGHT=480
while True:
    isTrue,frame=capture.read()
    frame_height, frame_width = frame.shape[:2]


    frame_rectangle=haar_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=2)
    crop_x,crop_y= frame_width//2-OUTPUT_WIDTH//2, frame_height//2-OUTPUT_HEIGHT//2
    (x,y,w,h)=frame_rectangle[0] if len(frame_rectangle)>0 else (0,0,0,0)
    face_center_x = x + w // 2
    face_center_y = y + h // 2
    crop_x = face_center_x - OUTPUT_WIDTH // 2
    crop_y = face_center_y - OUTPUT_HEIGHT // 2
    crop_x = max(0, min(crop_x, frame_width - OUTPUT_WIDTH))
    crop_y = max(0, min(crop_y, frame_height - OUTPUT_HEIGHT))
    frame = frame[crop_y:crop_y + OUTPUT_HEIGHT, crop_x:crop_x + OUTPUT_WIDTH]
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()