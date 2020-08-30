import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
def exponencial(inp,bconst,constante):
    f,c=inp.shape
    res=cv.imread('blank.png',0)
    for i in range(f):
        for j in range(c):
            r=constante*(pow(bconst,inp[i][j])-1)
            if(r<0):
                res[i][j]=0
            elif(r>255):
                res[i][j]=255
            else:
                res[i][j]=r
    return res

    
a = cv.imread('men2.jpg',0)
b = exponencial(a,1.01,20)
cv.imshow('res',b)



