import cv2
import numpy

img1 = cv2.imread("H:/Coding/Jetlearn Python Lessons/opencv/img1.jpg")
starting_coord = (50,50)
ending_coord = (200,200)

lineImg1 = cv2.line(img1 , starting_coord , ending_coord , (0 , 0 , 0) , 10)
cv2.imshow("Line on an Image" , lineImg1)
cv2.waitKey(0)
cv2.destroyAllWindows()

rectImg1 = cv2.rectangle(img1 , (300,300) , (600,600) , (255,255,255) , 5)
cv2.imshow("Rect" , rectImg1)
cv2.waitKey(0)
cv2.destroyAllWindows()

filled_rectImg1 = cv2.rectangle(img1 , (300,300) , (600,600) , (255,255,255) , -1)
cv2.imshow("Filled Rect" , filled_rectImg1)
cv2.waitKey(0)
cv2.destroyAllWindows()

circImg1 = cv2.circle(img1 , (800,200) , 25 , (255,100,100) , 5)
cv2.imshow("Cicle" , circImg1)
cv2.waitKey(0)
cv2.destroyAllWindows()

filled_circImg1 = cv2.circle(img1 , (800,200) , 25 , (255,100,100) , -1)
cv2.imshow("Filled Cicle" , filled_circImg1)
cv2.waitKey(0)
cv2.destroyAllWindows()

font = cv2.FONT_HERSHEY_SIMPLEX
origin = (60,60)
fontScale = 2
textImg1 = cv2.putText(img1 , "Mountains" , origin , font , fontScale , (100,100,100) , 2 , cv2.LINE_AA)
cv2.imshow("Text" , textImg1)
cv2.waitKey(0)
cv2.destroyAllWindows()