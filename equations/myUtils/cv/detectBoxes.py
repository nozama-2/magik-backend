import cv2
import os
import numpy as np
import time
import datetime as dt

from homography import detectHomography

# cv2.namedWindow("Processed Output")

cam = cv2.VideoCapture(0)
# cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam.set(3, 1280)
cam.set(4, 720)
cam.set(10, 100)
if not cam.isOpened():
    print("Cam not initialised")

i = 0

while True:
    timeNow = dt.datetime.now()
    ret, frame = cam.read()

    if ret:
        print("cam reading")
        cv2.imshow("Video Input", frame)
        warpedDisplay = cv2.warpPerspective(frame, h, (1920, 1080))

        cv2.imshow("Processed Output", warpedDisplay)
        cv2.imwrite("Tangram Output.png", warpedDisplay)

    if cv2.waitKey(1) & 0xFF == ord("x"):
        break
    # print(dt.datetime.now()-timeNow)

cam.release()
cv2.destroyAllWindows()
