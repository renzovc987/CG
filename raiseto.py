import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
def raiseto(inp,rconst,constante):
    f,c=inp.shape
    for i in range(f):
        for j in range(c):
            r=constante*(pow(inp[i][j],rconst))
            if(r<0):
                inp[i][j]=0
            elif(r>255):
                inp[i][j]=255
            else:
                inp[i][j]=r
    cv.imshow('res2',inp)
    
b = cv.imread('men2.jpg',0)
raiseto(b,1.5,0.05)
