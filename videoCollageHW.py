import cv2
import numpy as np
from PIL import Image
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


path = "H:/Coding/Jetlearn Python Lessons/opencv/videos"

img1 = "H:/Coding/Jetlearn Python Lessons/opencv/images/image1.jpeg"
img2 = "H:/Coding/Jetlearn Python Lessons/opencv/images/image2.jpeg"
img3 = "H:/Coding/Jetlearn Python Lessons/opencv/images/image3.jpeg"
img4 = "H:/Coding/Jetlearn Python Lessons/opencv/images/image4.jpeg"
img5 = "H:/Coding/Jetlearn Python Lessons/opencv/images/image5.jpeg"
img6 = "H:/Coding/Jetlearn Python Lessons/opencv/images/image6.jpeg"
img7 = "H:/Coding/Jetlearn Python Lessons/opencv/images/image7.jpeg"

images = [img1, img2, img3, img4 , img5 , img6, img7]

avgWidth = 0
avgHeight = 0

os.chdir(path)
num = len(os.listdir("."))

for i in images:
    if i.endswith(".jpeg") or i.endswith(".jpg") or i.endswith(".png"):
        currentimg = Image.open(i)
        width , height = currentimg.size
        avgWidth += width
        avgHeight += height

avgWidth = int(avgWidth/num)
avgHeight = int(avgHeight/num)

for i in images:
    if i.endswith(".jpeg") or i.endswith(".jpg") or i.endswith(".png"):
        currentimg = Image.open(i)
        newimg = currentimg.resize((avgWidth , avgHeight) , Image.Resampling.LANCZOS)
        newimg.save( i, "jpeg" , quality = 95)

num = len(os.listdir("."))
videoName = "collageVideo"+str(num+1)+".avi"
video1 = cv2.VideoWriter(videoName , 0 , 0.5 , (avgWidth , avgHeight) , True)


for i in images:
    if i.endswith(".jpeg") or i.endswith(".jpg") or i.endswith(".png"):
        currentimg = cv2.imread(i)
        video1.write(currentimg)

cv2.destroyAllWindows()
video1.release()