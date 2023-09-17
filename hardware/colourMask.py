import cv2 
import os
import numpy as np
import time
import datetime as dt
import matplotlib

cv2.namedWindow("Processed Output")

# cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 1280)
cam.set(4, 720)
cam.set(10,100)
if not cam.isOpened():
    print('Cam not initialised')

black = (0, 0, 0)
white = (255, 255, 255) 
successGreen = (156, 255, 124) 

# This format is in RGB 
pink = [255, 117, 118] 
purple = [217, 155, 255]
blue = [136, 149, 255] 
yellow = [255, 205, 31] 
orange = [255, 137, 0] 
lightGreen = [100, 255, 203] 
darkGreen = [45, 217, 152] 

# THis is what the camera sees
actualPink = [214, 121, 173]
actualPurple = [180, 175, 255]
# actualBlue = [206, 131, 68]
actualYellow = [208, 187, 124]
actualOrange = [255, 137, 0] 
actualLightGreen = [122, 247, 238]
actualDarkGreen = [29, 119, 87]

def makeMask(screenName, colour, actualColour, screen):
    # cv2.imshow("Processed Output", screen)

    # diff = [abs(colour[i] - actualColour[i]) for i in range(len(colour))]
    # lower = np.array([(actualColour[i]-diff[i]*1.3)/255 for i in range(len(diff))])
    # upper = np.array([(actualColour[i]+diff[i]*1.3)/255 for i in range(len(diff))])
    
    # lower = np.array([(colour[i]-diff[i]*2)/255 for i in range(len(diff))])
    # upper = np.array([(colour[i]+diff[i]*2)/255 for i in range(len(diff))])


    # lower_hsv = cv2.cvtColor([[lower]], cv2.COLOR_RGB2HSV_FULL)
    # upper_hsv = cv2.cvtColor([[upper]], cv2.COLOR_RGB2HSV_FULL)

    # upper = np.array([200/255, 230/255,150/255])
    # lower = np.array([150/255,180/255,90/255])
    # 173, 214, 121, 

    # lower = np.array([0,0,0])
    # upper = np.array([1,1,1])

    # lower_hsv = np.array([30,150,50])
    # upper_hsv = np.array([255,255,180])



    lower_hsv = np.array([0,50,50])
    upper_hsv = np.array([20,255,255])

    print(cv2.cvtColor(  np.uint8([[[0,0,139]]]) , cv2.COLOR_BGR2HSV))

    # print(lower_hsv, upper_hsv)



    # lower_hsv[0] = lower_hsv[0] * 179
    # upper_hsv[0] = upper_hsv[0] * 179
    # lower_hsv[1] = lower_hsv[1] * 255
    # upper_hsv[1] = upper_hsv[1] * 255
    # lower_hsv[2] = lower_hsv[2] * 255
    # upper_hsv[2] = upper_hsv[2] * 255


    # print(lower, upper)
    # print(lower_hsv, upper_hsv)

    screen_hsv = cv2.cvtColor(screen, cv2.COLOR_RGB2HSV)
    # screen_rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

    # screen_bgr = cv2.cvtColor(screen_hsv, cv2.COLOR_HSV2BGR_FULL)
    mask = cv2.inRange(screen_hsv, lower_hsv, upper_hsv) # not in range: black. in range: white.
    # mask = cv2.bitwise_not(mask)
    # print(mask)
    result = cv2.bitwise_and(screen, screen, mask=mask)

    cv2.imshow(screenName, result) 
    cv2.imshow('fml', mask)
    # cv2.imshow('fml2', screen_rgb)

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
        # cv2.imshow('Video Input', frame)
        warpedDisplay = cv2.warpPerspective(frame, h, (1920, 1080))

        # converting image into grayscale image
        # gray = cv2.cvtColor(warpedDisplay, cv2.COLOR_BGR2GRAY)

        # otsu threshold
        # threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

        makeMask('pink', pink, actualPink, warpedDisplay)
        # cv2.imshow('threshold output', cleanThreshold)
        # cv2.imshow('GRAY', threshold)
        # cv2.imshow("Processed Output", warpedDisplay)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    # print(dt.datetime.now()-timeNow)

cam.release()
cv2.destroyAllWindows()