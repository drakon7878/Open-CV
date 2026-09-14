import cv2
import numpy as np
from PIL import Image
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


path = "C:/Downloads/Open-CV-main/Open-CV-main/images"

avgWidth = 0
avgHeight = 0

os.chdir(path)
num = len(os.listdir("."))

for i in os.listdir("."):
    if i.endswith(".jpeg") or i.endswith(".jpg") or i.endswith(".png"):
        currentimg = Image.open(os.path.join(path,i))
        width , height = currentimg.size
        avgWidth += width
        avgHeight += height

avgWidth = int(avgWidth/num)
avgHeight = int(avgHeight/num)

for i in os.listdir("."):
    if i.endswith(".jpeg") or i.endswith(".jpg") or i.endswith(".png"):
        currentimg = Image.open(os.path.join(path,i))
        newimg = currentimg.resize((avgWidth , avgHeight) , Image.Resampling.LANCZOS)
        newimg.save( i, "jpeg" , quality = 95)


videoName = "collageVideo.avi"
video1 = cv2.VideoWriter(videoName , 0 , 0.5 , (avgWidth , avgHeight) , True)


for i in os.listdir("."):
    if i.endswith(".jpeg") or i.endswith(".jpg") or i.endswith(".png"):
        currentimg = cv2.imread(os.path.join(path,i))
        video1.write(currentimg)

cv2.destroyAllWindows()
video1.release()