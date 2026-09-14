import cv2
import numpy

font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread("bdayimg.jpg")
img = cv2.resize(img , (500,300))
img = cv2.rectangle(img , (100,25) , (400,100) , (255,0,0) , 5)
img = cv2.putText(img , "Happy Birthday" , (150,75) , font, 1, (100,100,100) , 2 , cv2.LINE_AA )
cv2.imshow("Rect" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()