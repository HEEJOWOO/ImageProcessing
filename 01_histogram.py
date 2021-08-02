import cv2
from matplotlib import pyplot as plt
#opencv를 이용하여 historgram 얻는 방법, numpy 보다 opencv가 속도가 더 빠름
#gray
gray_img = cv2.imread("lena.jpg",cv2.IMREAD_GRAYSCALE)
plt.title("gray histogram")
plt.xlabel("Bins")
plt.ylabel("num of Pixels")
histo = cv2.calcHist([gray_img],[0],None,[256],[0,256])
plt.plot(histo)
plt.show()
#color
color_img = cv2.imread("lena.jpg",cv2.IMREAD_COLOR)
color = ('b','g','r')
for i , col in enumerate(color):
    histo = cv2.calcHist([color_img],[i],None,[256],[0,256])
    plt.plot(histo, color = col)
    plt.xlim([0,256])
plt.title("color histogram")
plt.xlabel("Bins")
plt.ylabel("num of Pixels")
plt.show()
#grya histo gram full version
gray = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
hist_full = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.title("gray histogram(hist full)")
plt.xlabel("Bins")
plt.ylabel("num of Pixels")
plt.xlim([0, 256])
plt.plot(hist_full)
plt.show()
