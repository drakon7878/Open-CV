import cv2
import numpy

img1 = cv2.imread("img2.jpg")
cv2.imshow("Base Image" , img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

gaussionBlurImg = cv2.GaussianBlur(img1 , (127,127) , 0)
cv2.imshow("Gaussion Blur" , gaussionBlurImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

medianBlurImg = cv2.medianBlur(img1 , 11)
cv2.imshow("Median Blur" , medianBlurImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

bilateralBlurImg = cv2.bilateralFilter(img1 , 9 , 999 , 999)
cv2.imshow("Bilateral Blur" , bilateralBlurImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#BORDERING

solidBorder_Img = cv2.copyMakeBorder(img1 , 10 , 10 , 10 , 10 , cv2.BORDER_CONSTANT , value=(50,153,64))
cv2.imshow("Solid Border" , solidBorder_Img)
cv2.waitKey(0)
cv2.destroyAllWindows()

relfectBorder_Img = cv2.copyMakeBorder(img1 , 10 , 10 , 10 , 10 , cv2.BORDER_REFLECT , value = (150,0,150))
cv2.imshow("Reflect Border" , relfectBorder_Img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Erosion

kernel = numpy.ones((5,5) , numpy.uint8)
erosionImg = cv2.erode(img1 , kernel)
cv2.imshow("Erosion" , erosionImg)
cv2.waitKey(0)
cv2.destroyAllWindows()