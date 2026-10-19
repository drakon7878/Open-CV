import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import cv2

classifier = cv2.CascadeClassifier("C:/Downloads/Open-CV-main (1)/Open-CV-main/haarcascade_russian_plate_number.xml")

img = cv2.imread("Open-CV-main/car4.jpg")

detectedplate = classifier.detectMultiScale(img , 1.1 , 5)
print(detectedplate)



for (x,y,w,h) in detectedplate:
    cv2.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0) , 2)


cv2.imshow("Detected" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
