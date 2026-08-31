import cv2
import numpy

image = cv2.imread("opencv/image.jpeg")
cv2.imshow("Normal Image" , image)
cv2.waitKey(0)
cv2.destroyAllWindows()

resizedImage1 = cv2.resize(image , (500,500))
cv2.imshow("Larger Image" , resizedImage1)
cv2.waitKey(0)
cv2.destroyAllWindows()

greyImage = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image" , greyImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

HSVimage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image" , HSVimage)
cv2.waitKey(0)
cv2.destroyAllWindows()

image2 = cv2.imread("opencv/image2.jpeg")
resizedImage2 = cv2.resize(image2 , (500,500))
cv2.imshow("Normal Image2" , resizedImage2)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Arithmetic
addImg = cv2.add(resizedImage1 , resizedImage2)
cv2.imshow("Added Image" , addImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

subtractImg = cv2.subtract(resizedImage1 , resizedImage2)
cv2.imshow("Subtracted Image" , subtractImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

multiImg = cv2.multiply(resizedImage1 , resizedImage2)
cv2.imshow("Multiplied Image" , multiImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

divideImg = cv2.divide(resizedImage1 , resizedImage2)
cv2.imshow("Divided Image" , divideImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Channel Splitting
B,G,R = cv2.split(resizedImage2)

zeroArray = numpy.zeros_like(B)
blueImg = cv2.merge([B , zeroArray, zeroArray])
cv2.imshow("Blue Saturated Image" , blueImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

greenImg = cv2.merge([zeroArray , G , zeroArray])
cv2.imshow("Green Saturated Image" , greenImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

redImg = cv2.merge([zeroArray , zeroArray , R])
cv2.imshow("Red Saturated Image" , redImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("red.png" , redImg)