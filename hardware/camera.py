import cv2 
import os
import numpy as np
import time
import datetime as dt

cv2.namedWindow("Processed Output")

# cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 1280)
cam.set(4, 720)
cam.set(10,100)
if not cam.isOpened():
    print('Cam not initialised')


try:
    h = np.loadtxt('homographData.csv', delimiter=',')
except Exception as e:
    print("Homography Info not found!")
    print(e)
    raise Exception

i=0

while True:
    timeNow = dt.datetime.now()
    ret, frame = cam.read()

    if ret:
        cv2.imshow('Video Input', frame)
        warpedDisplay = cv2.warpPerspective(frame, h, (1920, 1080))

        # converting image into grayscale image
        gray = cv2.cvtColor(warpedDisplay, cv2.COLOR_BGR2GRAY)

        # otsu threshold
        threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

        # cv2.imshow('threshold output', cleanThreshold)
        cv2.imshow('GRAY', threshold)
                   
        # cv2 detect circle
        # grayBlur = cv2.medianBlur(gray, 5)
        # circles = cv2.HoughCircles(image=grayBlur, method=cv2.HOUGH_GRADIENT, dp=0.9, 
        #                     minDist=50, param1=30, param2=10, maxRadius=70)


        # for co, i in enumerate(circles[0, :], start=1):
        #     print(i)
            # draw the outer circle
            # cv2.circle(warpedDisplay,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            # cv2.circle(warpedDisplay,(i[0],i[1]),2,(0,0,255),3)


        # # using a findContours() function
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # list for storing names of shapes
        for contour in contours[1:]:
            contourX, contourY, contourWidth, contourHeight = cv2.boundingRect(contour)

            # print(contour)
            # print(contourWidth, contourHeight)
            sizeThreshold = 30
            if contourWidth < sizeThreshold or contourHeight < sizeThreshold:
                # print('too small')
                pass
            else:
                # cv2.approxPloyDP() function to approximate the shape
                approx = cv2.approxPolyDP(
                    contour, 0.01 * cv2.arcLength(contour, True), True)
                
                # using drawContours() function
                cv2.drawContours(warpedDisplay, [contour], 0, (0, 0, 255), 5)

                # finding center point of shape
                M = cv2.moments(contour)
                if M['m00'] != 0.0:
                    x = int(M['m10']/M['m00'])
                    y = int(M['m01']/M['m00'])

                # putting shape name at center of each shape
                if len(approx) == 3:
                    cv2.putText(warpedDisplay, 'Triangle', (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                elif len(approx) == 4:
                    cv2.putText(warpedDisplay, 'Quadrilateral', (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                elif len(approx) == 5:
                    cv2.putText(warpedDisplay, 'Pentagon', (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                elif len(approx) < 9: # should be six lol, doing this for my sanity
                    cv2.putText(warpedDisplay, 'Hexagon', (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                else:
                    print(f"Circle, {len(approx)}")
                    cv2.putText(warpedDisplay, 'circle', (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # displaying the image after drawing contours
        # cv2.imshow('shapes', contours)
        cv2.imshow("Processed Output", warpedDisplay)
        cv2.imwrite('Tangram Output.png', warpedDisplay)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    # print(dt.datetime.now()-timeNow)

cam.release()
cv2.destroyAllWindows()