import numpy as np
import cv2
# Let's load a simple image with 3 black squares 
image = cv2.imread('test.jpg') 
# Grayscale 
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
# Find Canny edges
orig=image.copy()
blurred=cv2.GaussianBlur(gray,(5,5),0)
edged=cv2.Canny(blurred,30,50)
corners = cv2.goodFeaturesToTrack(edged, 40, 0.01, 40)
corners = np.int0(corners)
maximox=0
maximoy=0
minimox=10000
minimoy=10000
i=0
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(edged,(x,y),3,255,-1)
    
cv2.imshow('res',edged)
        






