import cv2
import numpy as np
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

fcClassifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("frontalface.jpg")
detectedFaces = fcClassifier.detectMultiScale(img , 1.1 , 1)
print(detectedFaces)

for (x,y,w,h) in detectedFaces:
    cv2.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0) , 2)


cv2.imshow("Detected" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

eyeCascade = cv2.CascadeClassifier("H:/Coding/Jetlearn Python Lessons/opencv/haarcascade_eye.xml")
detectedEyes = eyeCascade.detectMultiScale(img , 1.1 , 15)
print("\n")
print(detectedEyes)

for (x,y,w,h) in detectedEyes:
    cv2.rectangle(img , (x,y) , (x+w,y+h) , (0,0,255) , 4)

cv2.imshow("Detected" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()