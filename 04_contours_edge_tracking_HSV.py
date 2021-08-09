import numpy as np
import cv2
##HSV field
lowerBound = np.array([0, 180, 55])
upperBound = np.array([20, 255, 200])

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    color_mask = cv2.inRange(hsv, lowerBound, upperBound)

    ret1, threshol = cv2.threshold(color_mask , 127, 255, 0)

    contours, _ = cv2.findContours(threshol, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        for i in range(len(contours)):
            area = cv2.contourArea(contours[i])

            if area > 100:
                rect = cv2.minAreaRect(contours[i])
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)
    
    cv2.imshow('color_bitwise',color_mask)
    cv2.imshow('cam_load',frame)
    cv2.waitKey()

cap.release()
cv2.destroyAllWindows()

