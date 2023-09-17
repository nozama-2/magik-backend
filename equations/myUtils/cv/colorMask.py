import cv2
import os
import numpy as np
import time
import datetime as dt


cam = cv2.VideoCapture(0)
# cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 1280)
cam.set(4, 720)
cam.set(10, 100)
if not cam.isOpened():
    print("Cam not initialised")

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

try:
    h = np.loadtxt(
        os.path.join(os.getcwd(), "myUtils", "cv", "homographData.csv"), delimiter=","
    )
except Exception as e:
    print("Homography Info not found!")
    print(e)
    raise Exception


def makeMask(screenName, colour, actualColour, screen):
    lower_hsv = np.array([0, 0, 90])
    upper_hsv = np.array([5, 255, 255])

    print(cv2.cvtColor(np.uint8([[[200, 200, 200]]]), cv2.COLOR_BGR2HSV))

    screen_hsv = cv2.cvtColor(screen, cv2.COLOR_RGB2HSV)

    mask = cv2.inRange(screen_hsv, lower_hsv, upper_hsv)
    result = cv2.bitwise_and(screen, screen, mask=mask)

    cv2.imshow(screenName, result)
    cv2.imshow("fml", mask)


i = 0

while True:
    timeNow = dt.datetime.now()
    ret, frame = cam.read()

    if ret:
        print("ret")
        warpedDisplay = cv2.warpPerspective(frame, h, (1920, 1080))
        makeMask("pink", pink, actualPink, warpedDisplay)
        # cv2.imshow('threshold output', cleanThreshold)
        # cv2.imshow('GRAY', threshold)
        # cv2.imshow("Processed Output", warpedDisplay)

        cv2.imshow("raw", warpedDisplay)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break
    # print(dt.datetime.now()-timeNow)

cam.release()
cv2.destroyAllWindows()
