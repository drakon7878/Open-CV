import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import cv2
import numpy as np
import time

video = cv2.VideoCapture("Open-CV-main/video.mp4")

time.sleep(1)

for i in range(60):
    ret , frame = video.read()
    if ret == False:
        continue

bg = np.flip(frame , axis = 1)
cv2.imshow("Bg" , bg)
cv2.waitKey(0)
cv2.destroyAllWindows()