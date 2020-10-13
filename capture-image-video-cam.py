import cv2
import numpy as np

##---------------capture image---------##
# img = cv2.imread("Picture/Football.jpg")
# cv2.imshow("output", img)
# cv2.waitKey(0)

##--------------video capture----------##
# cap = cv2.VideoCapture("Video/20secondFootball.mp4")
# while True :
#     success, img =cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(21) & 0Xff ==ord('q'):
#         break
#
##------------screen camera--------------##
## index 0 pada videocapture = 0 = camera 1 yang dipakai. 1 = camera 2
cap = cv2.VideoCapture(0)
##mengatur atau resize frame dengan set, set id 3 = width,4 = height, 10 =brigthness
cap.set(3,480)
cap.set(4,480)
cap.set(10,20)
while True :
    success, img =cap.read()
    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF ==ord('q') :
        break
