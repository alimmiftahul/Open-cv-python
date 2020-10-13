import cv2
import numpy as np


img = cv2.imread("Picture/bola.jpg")
#5,5 kernel size
kernel = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
###---------5,5 itu adalah kernel size, o adalah sigma x---------###
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
#---canny adalah gambar yang hanya menampilkan garis saja, 200 adalah treshold atau banyak garis, semakin sedikit treshold maka semakin banyak garis
imgCanny = cv2.Canny(imgGray,100,100 )
imgDilate = cv2.dilate(imgCanny,kernel,iterations=1)
imgerode = cv2.erode(imgDilate,kernel,iterations=1)


cv2.imshow("dilate",imgDilate)
cv2.imshow("canny",imgCanny)
cv2.imshow("eroded",imgerode)

cv2.imshow("Blur image",imgBlur)
cv2.imshow("Greyimage", imgGray)

cv2.waitKey(0)