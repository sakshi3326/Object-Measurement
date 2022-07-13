import cv2
import numpy as np
webcam = False
path = '1.jpeg'
cap = cv2.VideoCapture(0)
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)

while True:
    if webcam:success, img = cap.read()
    else: img = cv2.imread(path)




    cv2.imshow('original', img)
    cv2.waitKey(1)