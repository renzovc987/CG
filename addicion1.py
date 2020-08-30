import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread('add_1.jpg',0)
img2=cv2.imread('add_2.jpg',0)
img1=cv2.resize(img1,(img2.shape[1],img2.shape[0]))
img3=cv2.imread('blank.jpg',0)
f,c=img1.shape
for i in range(f):
    for j in range(c):
        r=int(img1[i][j]/2)+int(img2[i][j]/2)
        if(r<0):
            img3[i][j]=0
        elif(r>255):
            img3[i][j]=255
        else:
            img3[i][j]=r
            
cv2.imshow('res',img3)
