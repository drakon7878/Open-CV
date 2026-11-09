import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import cv2
import easyocr
import numpy as np

reader = easyocr.Reader(["en"] , gpu = False)
result1 = reader.readtext("Open-CV-main/car4.jpg")
for bbox, text, confidence in result1: 
    print(f'Text: {text} (Confidence: {confidence:.2f})')
