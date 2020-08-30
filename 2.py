import cv2
import numpy as np
#import matplotlib as plt
from matplotlib import pyplot as plt

img = cv2.imread("1.jpg",0)
img=cv2.resize(img,(500,300))
cv2.imshow("b.png",img)

#########  write your code here ##################

img_out = img

hist = cv2.calcHist([img_out], [0], None, [256], [0, 256])


height, width = img_out.shape
for i in range(height):
    for j in range(width):
        if img_out[i][j]<=97:
            img_out[i][j]=0
        else:
            img_out[i][j]=255
            



######## the result have to be set in img_out ####
######## not modify from here ####################

cv2.imshow("2.png", img_out)
    
