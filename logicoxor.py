import cv2
import numpy as np
img1=cv2.imread('log_3.png',0)
img2=cv2.imread('log_4.png',0)
img3=cv2.imread('blankl.png',0)
f,c=img1.shape
for i in range(f):
    for j in range(c):
        img3[i][j]=np.bitwise_xor(img1[i][j], img2[i][j])

cv2.imshow('res',img3)
