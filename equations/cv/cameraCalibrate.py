import cv2 
import os
import numpy as np
import time
import datetime as dt

cv2.namedWindow("Video Input")
# cv2.namedWindow("Markers") # this cannot be shown when running with assumption that h has been calculated
cv2.namedWindow("Processed Output")

srcPoints = np.array([[385,165],
 [535,165],
 [535,315],
 [385,315],
 [385,365],
 [535,365],
 [535,515],
 [385,515],
 [385,565],
 [535,565],
 [535,715],
 [385,715],
 [385,765],
 [535,765],
 [535,915],
 [385,915],
 [585,165],
 [735,165],
 [735,315],
 [585,315],
 [585,365],
 [735,365],
 [735,515],
 [585,515],
 [585,565],
 [735,565],
 [735,715],
 [585,715],
 [585,765],
 [735,765],
 [735,915],
 [585,915],
 [785,165],
 [935,165],
 [935,315],
 [785,315],
 [785,365],
 [935,365],
 [935,515],
 [785,515],
 [785,565],
 [935,565],
 [935,715],
 [785,715],
 [785,765],
 [935,765],
 [935,915],
 [785,915],
 [985,165],
 [1135,165],
 [1135,315],
 [985,315],
 [985,365],
 [1135,365],
 [1135,515],
 [985,515],
 [985,565],
 [1135,565],
 [1135,715],
 [985,715],
 [985,765],
 [1135,765],
 [1135,915],
 [985,915],
 [1185,165],
 [1335,165],
 [1335,315],
 [1185,315],
 [1185,365],
 [1335,365],
 [1335,515],
 [1185,515],
 [1185,565],
 [1335,565],
 [1335,715],
 [1185,715],
 [1185,765],
 [1335,765],
 [1335,915],
 [1185,915],
 [1385,165],
 [1535,165],
 [1535,315],
 [1385,315],
 [1385,365],
 [1535,365],
 [1535,515],
 [1385,515],
 [1385,565],
 [1535,565],
 [1535,715],
 [1385,715],
 [1385,765],
 [1535,765],
 [1535,915],
 [1385,915]])
cam = cv2.VideoCapture(0)
# cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 1280)
cam.set(4, 720)
cam.set(10,100)
if not cam.isOpened():
    print('cam not initialised')

ids = []
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_50)
h = None

try:
    h = np.loadtxt('homographData.csv', delimiter=',')
except Exception as e:
    print(e)
    h = None

while True:
    timeNow = dt.datetime.now()
    ret, frame = cam.read()

    if ret:
        cv2.imshow('Video Input', frame)
        
        frameCopy = frame.copy()
        if h is None:
            grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(grayFrame, dictionary)
            print('Detected markers!')
        
            if ids is not None:
                if len(ids) == 24:
                    frame_markers = cv2.aruco.drawDetectedMarkers(grayFrame, corners, ids)
                    ids = ids.reshape((24,))
                    sort = np.argsort(ids)
                    corners = np.array(corners)
                    corners = corners[sort]
                    resPoints = np.concatenate(np.concatenate(corners))

                    h, s = cv2.findHomography(resPoints, srcPoints, cv2.RANSAC, 5.0)
                    print('Found Homography!')
                    # time.sleep(10)
                else:
                    print("not whole homography img is in frame")
            else:
                print("No homography box is in frame")

        if h is not None:
        # M = cv2.getPerspectiveTransform(resPoints, srcPoints)
            warpedDisplay = cv2.warpPerspective(frame, h, (1920, 1080))

            # cv2.imshow("Markers", frame_markers)
            cv2.imshow("Processed Output", warpedDisplay)
            # print(these_res_corners)

            query_img = frame
            train_img = warpedDisplay

            query_img_bw = cv2.cvtColor(query_img,cv2.COLOR_BGR2GRAY)
            train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)
            
            # Initialize the ORB detector algorithm
            orb = cv2.ORB_create()
            
            # Now detect the keypoints and compute
            # the descriptors for the query image
            # and train image
            queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw,None)
            trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw,None)
            
            # Initialize the Matcher for matching
            # the keypoints and then match the
            # keypoints
            matcher = cv2.BFMatcher()
            matches = matcher.match(queryDescriptors,trainDescriptors)
            
            # draw the matches to the final image
            # containing both the images the drawMatches()
            # function takes both images and keypoints
            # and outputs the matched query image with
            # its train image
            final_img = cv2.drawMatches(query_img, queryKeypoints, 
            train_img, trainKeypoints, matches[:150],None)
            
            final_img = cv2.resize(final_img, (1920,1080))

            cv2.imshow('Homography Matching', final_img)


    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

    if cv2.waitKey(1) & 0xFF == ord('s'):
        np.savetxt('homographData.csv', h, delimiter=',')
        print('SAVED DATA')
        break
    
    else:
        h = None

    # print(dt.datetime.now()-timeNow)


cam.release()
cv2.destroyAllWindows()