import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def thresholdingvivas(inp):
    f, c = inp.shape
    for i in range(f):
        for j in range(c):
            if(inp[i][j]>=195):
                inp[i][j]=0
    cv.imshow('vivas',inp)
def thresholdingmuertas(inp):
    f, c = inp.shape
    for i in range(f):
        for j in range(c):
            if(inp[i][j]<=150):
                inp[i][j]=0
    cv.imshow('muertas',inp)
def thresholdingcolores(inp):
    f, c ,color = inp.shape
    for i in range(f):
        for j in range(c):
            if(img[i][j][0]<=121 or img[i][j][1]<=144 or img[i][j][2]<=184):
                inp[i][j][0]=0
                inp[i][j][1]=0
                inp[i][j][2]=0
    cv.imshow('colores',inp)

    
img = cv.imread('thresh2.png', cv.IMREAD_GRAYSCALE)
hist = cv.calcHist([img], [0], None, [256], [0, 256])
thresholdingmuertas(img)
plt.plot(hist, color='gray')
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()
