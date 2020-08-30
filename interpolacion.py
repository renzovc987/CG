import cv2
import numpy as np


def interp(img):
    f,c=img.shape
    imag2 = np.zeros((f,c,3),np.uint8)
    for i in range(f):
        for j in range(c):
            ni = i * 2
            nj = j * 2
            if(i+1<f and j+1<c):
                promedio=(int(img[i][j])+int(img[i+1][j])+int(img[i][j+1])+int(img[i+1][j+1])/4)
                if(promedio>255):
                    promedio=255
            if(ni+1<f and nj+1<c and i+1<f and j+1<c):
                imag2[ni][nj] = promedio
                imag2[ni+1][nj] = promedio
                imag2[ni][nj+1] = promedio
                imag2[ni+1][nj+1] = promedio
    return imag2

def pixel_rep(img):
    f,c=img.shape
    imag2 =  np.zeros((f,c,3),np.uint8)
    for i in range(f):
        for j in range(c):
            ni=i*2
            nj=j*2
            if(ni+1<f and nj+1<c):
                imag2[ni][nj] = img[i][j]
                imag2[ni+1][nj] = img[i][j]
                imag2[ni][nj+1] = img[i][j]
                imag2[ni+1][nj+1] = img[i][j]
    return imag2

img=cv2.imread('mario.jpg',0)
res=interp(img)
cv2.imshow('res',res)
