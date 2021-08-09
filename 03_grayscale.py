#grayscale을 이용하는이유
#1) image processing 에서 색상을 필요로하지 않을 경우 생삭은 노이즈로 인식될 수 있음
#2) 엣지를 찾을때 gray scale로 변환하지 않고 색상 이미지만 사용할 경우 더 많은 작업 필요
#3) gray scale은 1채널을 이용하기떄문에 processing에 편함, 그 외 색상인식, 속도 등에 어려움이 있음

import numpy as np
import cv2

img_color = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('color image', img_color )
cv2.imshow('gray image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()



