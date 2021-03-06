import cv2
import numpy as np
def getAffineTransform(pts1,pts2):
  A=np.float32(np.concatenate((pts1,[[1],[1],[1]]),axis=1))
  pts2=np.float32(pts2)
  b1=pts2[:,0]
  b2=pts2[:,1]
  x=cv2.solve(A,b1)
  x2=cv2.solve(A,b2)
  return np.float32(np.concatenate((x[1],x2[1])).reshape(2,3) )
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
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
print(M)
res=warpaffine(img,M)
dst=cv2.warpAffine(img, M, (c, f))
cv2.imshow('res',res)
cv2.imshow('res2',dst)
