import cv2
import os
import numpy as np
import time
import datetime as dt


def detectHomography():
    cam = cv2.VideoCapture(0)
    # cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 1280)
    cam.set(4, 720)
    cam.set(10, 100)

    srcPoints = np.array(
        [
            [385, 165],
            [535, 165],
            [535, 315],
            [385, 315],
            [385, 365],
            [535, 365],
            [535, 515],
            [385, 515],
            [385, 565],
            [535, 565],
            [535, 715],
            [385, 715],
            [385, 765],
            [535, 765],
            [535, 915],
            [385, 915],
            [585, 165],
            [735, 165],
            [735, 315],
            [585, 315],
            [585, 365],
            [735, 365],
            [735, 515],
            [585, 515],
            [585, 565],
            [735, 565],
            [735, 715],
            [585, 715],
            [585, 765],
            [735, 765],
            [735, 915],
            [585, 915],
            [785, 165],
            [935, 165],
            [935, 315],
            [785, 315],
            [785, 365],
            [935, 365],
            [935, 515],
            [785, 515],
            [785, 565],
            [935, 565],
            [935, 715],
            [785, 715],
            [785, 765],
            [935, 765],
            [935, 915],
            [785, 915],
            [985, 165],
            [1135, 165],
            [1135, 315],
            [985, 315],
            [985, 365],
            [1135, 365],
            [1135, 515],
            [985, 515],
            [985, 565],
            [1135, 565],
            [1135, 715],
            [985, 715],
            [985, 765],
            [1135, 765],
            [1135, 915],
            [985, 915],
            [1185, 165],
            [1335, 165],
            [1335, 315],
            [1185, 315],
            [1185, 365],
            [1335, 365],
            [1335, 515],
            [1185, 515],
            [1185, 565],
            [1335, 565],
            [1335, 715],
            [1185, 715],
            [1185, 765],
            [1335, 765],
            [1335, 915],
            [1185, 915],
            [1385, 165],
            [1535, 165],
            [1535, 315],
            [1385, 315],
            [1385, 365],
            [1535, 365],
            [1535, 515],
            [1385, 515],
            [1385, 565],
            [1535, 565],
            [1535, 715],
            [1385, 715],
            [1385, 765],
            [1535, 765],
            [1535, 915],
            [1385, 915],
        ]
    )

    ids = []
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_50)
    homograhpyPointsFile = os.path.join(
        os.getcwd(), "myUtils", "cv", "homographData.csv"
    )
    h = None

    if os.path.exists(homograhpyPointsFile):
        os.remove(homograhpyPointsFile)

    while h is None:
        ret, frame = cam.read()

        if ret:
            grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            corners, ids, _ = cv2.aruco.detectMarkers(grayFrame, dictionary)

            if ids is not None:
                if len(ids) == 24:
                    ids = ids.reshape((24,))
                    sort = np.argsort(ids)
                    corners = np.array(corners)
                    corners = corners[sort]
                    resPoints = np.concatenate(np.concatenate(corners))

                    h, _ = cv2.findHomography(resPoints, srcPoints, cv2.RANSAC, 5.0)
                    print("Found Homography!")

                else:
                    print("NOT EVERYTHING IS IN FRAME. MOVE THE CAMERA. THX.")

        if cv2.waitKey(1) & 0xFF == ord("x"):
            break

    np.savetxt(
        os.path.join(os.getcwd(), "myUtils", "cv", "homographData.csv"),
        h,
        delimiter=",",
    )
    print("SAVED DATA")

    cam.release()


detectHomography()
