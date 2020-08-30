import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("question_2.png",0)
f, c = img.shape
for i in range(f):
    for j in range(c):
        if(img[i][j]<=52):
            img[i][j]=0
        else:
            img[i][j]=255
        
img_out = img
cv2.imwrite("question_2_sol.png", img_out)
