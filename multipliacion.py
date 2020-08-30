import cv2
import numpy as np
def contraste(inp):
    f,c,color=inp.shape
    c1=np.min(inp)
    d=np.max(inp)
    for i in range(f):
        for j in range(c):
            inp[i][j][0]=round((inp[i][j][0]-c1)*((255)/(d-c1)))
            inp[i][j][1]=round((inp[i][j][1]-c1)*((255)/(d-c1)))
            inp[i][j][2]=round((inp[i][j][2]-c1)*((255)/(d-c1)))
    return inp
def multi(img1,constante):
    f,c,color=img1.shape
    for i in range(f):
        for j in range(c):
            r1=int(img1[i][j][0])*constante
            r2=int(img1[i][j][1])*constante
            r3=int(img1[i][j][2])*constante
            if(r1<0):
                img1[i][j][0]=0
            elif(r1>255):
                img1[i][j][0]=255
            else:
                img1[i][j][0]=r1
            if(r2<0):
                img1[i][j][1]=0
            elif(r2>255):
                img1[i][j][1]=255
            else:
                img1[i][j][1]=r2
            if(r3<0):
                img1[i][j][2]=0   
            elif(r3>255):
                img1[i][j][2]=255
            else:
                img1[i][j][2]=r3
    return img1

img1=cv2.imread('tigre.jpeg')
img1=cv2.resize(img1,(400,400))                  
img2=contraste(img1)
cv2.imshow('res1',img1)
cv2.imshow('res2',img2)
