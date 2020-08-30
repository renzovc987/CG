#!/usr/bin/env python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
def logaritmo(inp,constante):
    f,c=inp.shape
    res=cv.imread('blank.png',0)
    for i in range(f):
        for j in range(c):
            r=constante*math.log((1+inp[i][j]),10)
            if(r<0):
                res[i][j]=0
            elif(r>255):
                res[i][j]=255
            else:
                res[i][j]=r
    return res


img = cv.imread('men2.jpg', cv.IMREAD_GRAYSCALE)
b = logaritmo(img,70)
cv.imshow('res',b)



