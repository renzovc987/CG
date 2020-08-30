import cv2
import numpy as np
from matplotlib import pyplot as plt
def exponencial(inp,bconst,constante):
    f,c,color=inp.shape
    for i in range(f):
        for j in range(c):
            r1=constante*(pow(bconst,inp[i][j][0])-1)
            r2=constante*(pow(bconst,inp[i][j][1])-1)
            r3=constante*(pow(bconst,inp[i][j][2])-1)
            if(r1<0):
                inp[i][j][0]=0
            elif(r1>255):
                inp[i][j][0]=255
            else:
                inp[i][j][0]=r1
            if(r2<0):
                inp[i][j][1]=0
            elif(r2>255):
                inp[i][j][1]=255
            else:
                inp[i][j][1]=r2
            if(r3<0):
                inp[i][j][2]=0
            elif(r3>255):
                inp[i][j][2]=255
            else:
                inp[i][j][2]=r3
    return inp
def contraste(inp):
    f,c,color=inp.shape
    c1=np.min(inp)
    d=np.max(inp)
    for i in range(f):
        for j in range(c):
            inp[i][j][0]=((inp[i][j][0]-c1)*((255)/(d-c1)))
            inp[i][j][1]=((inp[i][j][1]-c1)*((255)/(d-c1)))
            inp[i][j][2]=((inp[i][j][2]-c1)*((255)/(d-c1)))
    return inp
def dilation(img,kernel):
    f,c=img.shape
    img2=np.zeros((f,c),np.uint8)
    for i in range(1,f-1):
        for j in range(1,c-1):
            sm=[kernel[0][0]*img[i-1][j-1],kernel[0][1]*img[i-1][j],kernel[0][2]*img[i-1][j+1],
                kernel[1][0]*img[i][j-1],kernel[1][1]*img[i][j],kernel[1][2]*img[i][j+1],
                kernel[2][0]*img[i+1][j-1],kernel[2][1]*img[i+1][j],kernel[2][2]*img[i+1][j+1]]
            img2[i][j]=np.max(sm)
    return img2
def erosion(img,kernel):
    f,c=img.shape
    img2=np.zeros((f,c),np.uint8)
    for i in range(1,f-1):
        for j in range(1,c-1):
            sm=[kernel[0][0]*img[i-1][j-1],kernel[0][1]*img[i-1][j],kernel[0][2]*img[i-1][j+1],
                kernel[1][0]*img[i][j-1],kernel[1][1]*img[i][j],kernel[1][2]*img[i][j+1],
                kernel[2][0]*img[i+1][j-1],kernel[2][1]*img[i+1][j],kernel[2][2]*img[i+1][j+1]]
            img2[i][j]=np.min(sm)
    return img2
def opening(img,kernel):
    img1=erosion(img,kernel)
    img2=dilation(img1,kernel)
    return img2

def closing(img,kernel):
    img1=dilation(img,kernel)
    img2=erosion(img1,kernel)
    return img2
def escala_grises(img):
    f,c,color=img.shape
    for i in range(f):
        for j in range(c):
            promedio=(int(img[i][j][0])+int(img[i][j][1])+int(img[i][j][2]))/3
            img[i][j]=promedio
    return img
def colorear(imgb,imgc):
    f,c=imgb.shape
    imgb=cv2.cvtColor(imgb,cv2.COLOR_GRAY2RGB)
    for i in range(f):
        for j in range(c):
            if(imgb[i][j][0]==0 and imgb[i][j][1]==0 and imgb[i][j][2]==0):
                imgb[i][j][0]=imgc[i][j][0]
                imgb[i][j][1]=imgc[i][j][1]
                imgb[i][j][2]=imgc[i][j][2]
    return imgb
                
#img=cv2.imread('testl2.jpg',0)
#img=cv2.resize(img ,(500,500))
#height, width = img.shape
#img =cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)
#kernel=np.ones((3,3),np.uint8)
#blur=closing(img,kernel)
#blur=erosion(img,kernel)
img2 = cv2.imread('testl2.jpg',0)
img3 = cv2.imread('testl2.jpg')
gray = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,10)
img4 =  colorear(gray,img3)
cv2.imshow('res',img4)


