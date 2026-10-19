import cv2
import numpy as np
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

fcClassifier = cv2.CascadeClassifier("C:/Downloads/Open-CV-main (1)/Open-CV-main/cars.xml")

img = cv2.imread("Open-CV-main/vehicles3.jpg")
detectedFaces = fcClassifier.detectMultiScale(img , 1.03 , 1)
print(detectedFaces)

cv2.imshow("Detected" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()


for (x,y,w,h) in detectedFaces:
    cv2.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0) , 2)


cv2.imshow("Detected" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

