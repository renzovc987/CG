#rotation
import cv2
import numpy as np
import math
img1=cv2.imread('oso.jpeg',0)
f,c=img1.shape
angulo=0.785398
scale=0.7
coseno=(np.cos(angulo))*0.7
seno=(np.sin(angulo))*0.7
px=f/2
py=c/2
bx=(1-coseno)*px-seno*py
by=seno*px+(1-seno)*py
M = np.float32([[coseno, seno,bx], [seno*(-1), coseno,by]])
dst=cv2.warpAffine(img1, M, (c, f))
cv2.imshow('res',dst)

