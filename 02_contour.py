#contousr : 같은 색 혹은 intensity를 가진 연속적으로 모이는 점의 곡선, 외곽선을 딴것
import cv2
import numpy as np

img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
#cv2.findContours의 3번째 인자
#cv2.CHAIN_APPROX_NONE : contours에 모든 외곽선을 이루는 점들이 저장 ,
#cv2.CHAIN_APPROX_SIMPLE : 불필요한 점들을 지우고 적은 점들로만 외곽선을 이룸
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow('lena', img)
cv2.imshow('lena_contours', thresh)
cv2.waitKey(0)

#real-time
import cv2
import numpy as np

capture = cv2.VideoCapture(0)
print("image width : %d"%(capture.get(3)))
print("image height : %d"%(capture.get(4)))

capture.set(3, 340)
capture.set(4, 440)

while(1):
    ret, frame = capture.read()

    if ret:

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lowerBound = np.array([20, 100, 100])
        upperBound = np.array([30, 255, 255])

        #yellow section in image
        mask = cv2.inRange(img, lowerBound, upperBound)

        kernelOpen = np.ones((5, 5))
        kernelClose = np.ones((20, 20))

        maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
        maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

        maskFinal = maskClose
        conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        cv2.drawContours(img, conts, -1, (255, 0, 0), 3)
        for i in range(len(conts)):
            x, y, w, h = cv2.boundingRect(conts[i])
            rec = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imshow('rec', rec)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
