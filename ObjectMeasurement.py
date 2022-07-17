import cv2
import utilise
import numpy as np
webcam = False
path = '1.jpeg'
cap = cv2.VideoCapture(0)
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)
scale = 3
wP = 210* scale
hP = 297*scale


while True:
    if webcam:success, img = cap.read()
    else:img = cv2.imread(path)

    img, findCountours = utilise.getContoutours(img,minArea=50000,filter=4)
    if len(findCountours)!=0:
        biggest = findCountours[0][2]
        #print(biggest)
        imgWarp = utilise.warpImg(img, biggest, wP, hP)


        img2, findCountours2 = utilise.getContoutours(imgWarp, minArea=2000, filter=4,cThr=[50,50],draw=False)

        if len(findCountours2)!=0:
            for obj in findCountours2:
                cv2.polylines(img2,[obj[2]],True,(0,255,0),2)
                nPoints = utilise.reorder(obj[2])
                print(utilise.finddis(nPoints[0][0]//scale,nPoints[1][0]//scale))

        cv2.imshow('A4',img2 )

    img = cv2.resize(img,(0,0),None,0.5,0.5)

    cv2.imshow('original', img)

    cv2.waitKey(1)