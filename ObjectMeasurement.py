import cv2
import utilise
import numpy as np
webcam = False
path = '2.jpeg'
cap = cv2.VideoCapture(0)
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)

while True:
    if webcam:success, img = cap.read()
    else: img = cv2.imread(path)

    img, findCountours = utilise.getContoutours(img,showCanny=True,
                                                minArea=50000,filter=4)
    if len(findCountours)!=0:
        biggest = findCountours[0][2]
        #print(biggest)
        utilise.warpImg(img, biggest, 100, 100)

    img = cv2.resize(img,(0,0),None,0.5,0.5)

    cv2.imshow('original', img)
    cv2.waitKey(1)