import cv2
import numpy as np
##resize image
## 5,5 adalah kernel size
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("Picture/bola.jpg")
imgresize = cv2.resize(img,(100,100))
print(img.shape)
# hasilny print adalah(tinggi, lebar, rgb) yang bergubna untuk melihat bentuk gambar
# img cropped
# 50:600 adlah ukuran tinggi yang ingin dipotong, kemuadian lebar yang ingin dipotong.
imgcropped = img[50:600, 300:900 ]

imggreycroped = cv2.cvtColor(imgcropped,cv2.COLOR_BGR2GRAY)
imgcropedbw = cv2.Canny(imggreycroped,100,100)
imgdilatebw = cv2.dilate(imgcropedbw, kernel, iterations=1)
imgerodedbw = cv2.erode(imgdilatebw,kernel,iterations=1)

##--- hasil gambar potong/crop---##
cv2.imshow("img cropped", imgcropped)
##----gambar yang asli----##
cv2.imshow("img resize", img)
##---ekstraksi gambar----##
cv2.imshow("img erode", imgerodedbw)
cv2.waitKey(0)