import cv2
import numpy as np
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

fcClassifier = cv2.CascadeClassifier("C:/Downloads/Open-CV-main (1)/Open-CV-main/cars.xml")

video = cv2.VideoCapture("Open-CV-main/video2.avi")

while video.isOpened():
    ret , frame = video.read()
    detectedFaces = fcClassifier.detectMultiScale(frame , 1.03 , 1)
    print(detectedFaces)
    for (x,y,w,h) in detectedFaces:
        cv2.rectangle(frame , (x,y) , (x+w,y+h) , (0,255,0) , 2)
    cv2.imshow("Detected" , frame)
    if cv2.waitKey(25) & 0xFF == ord('q'): break

cv2.destroyAllWindows()









