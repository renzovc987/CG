#!/usr/bin/env python
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
def raiz(inp,constante):
    f,c=inp.shape
    res=cv.imread("blank.png",0)
    for i in range(f):
        for j in range(c):
            r=constante*(math.sqrt(inp[i][j]))
            if(r<0):
                res[i][j]=0
            elif(r>255):
                res[i][j]=255
            else:
                res[i][j]=r
    return res


img = cv.imread('uploads/original.jpeg', cv.IMREAD_GRAYSCALE)
b = raiz(img,70)
cv.imwrite('uploads/resultado.jpeg',b)
