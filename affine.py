import cv2
import numpy as np
def warpaffine(img,M):
    f,c,color=img.shape
    img2=np.zeros((f,c,3),np.uint8)
    ni=0
    nj=0
    A=np.float32([[M[0][0], M[0][1]], [M[1][0], M[1][1]]])
    B=np.float32([M[0][2],M[1][2]])
    R=np.float32([0,0])
    V=np.float32([0,0])
    for i in range(f):
        for j in range(c):
            ni=i
            nj=j
            V[0]=ni
            V[1]=nj
            R=np.dot(A,V)+B
            if(R[0]<f and R[1]<c and R[0]>0 and R[1]>0):
                img2[int(R[0])][int(R[1])][0]=img[i][j][0]
                img2[int(R[0])][int(R[1])][1]=img[i][j][1]
                img2[int(R[0])][int(R[1])][2]=img[i][j][2]
    return img2

img=cv2.imread('mario.jpg')
f=img.shape[0]
c=img.shape[1]
angulo=0.785398
scale=0.7
coseno=(np.cos(angulo))*scale
seno=(np.sin(angulo))*scale
px=f/2
py=c/2
bx=(1-coseno)*px-seno*py
by=seno*px+(1-seno)*py
M = [[coseno, seno,bx], [seno*(-1), coseno,by]]
res=warpaffine(img,M)
cv2.imshow('res',res)



        
        
