import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import cv2

classifier = cv2.CascadeClassifier("C:/Downloads/Open-CV-main (1)/Open-CV-main/haarcascade_russian_plate_number.xml")

video = cv2.VideoCapture("Open-CV-main/Automatic Number Plate Recognition (ANPR) _ Vehicle Number Plate Recognition (1).mp4")
while video.isOpened():
    ret , frame = video.read()
    detectedplates = classifier.detectMultiScale(frame , 1.1 , 4)
    print(detectedplates)
    for (x,y,w,h) in detectedplates:
        cv2.rectangle(frame , (x,y) , (x+w,y+h) , (0,255,0) , 2)
    cv2.imshow("Detected" , frame)
    if cv2.waitKey(25) & 0xFF == ord('q'): break

cv2.destroyAllWindows()