
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('CelulasRatones1.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('CelulasRatones2.png', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('celulas_saludables_muertas_ratones.png', cv2.IMREAD_GRAYSCALE)
res = cv2.imread('celulas_saludables_muertas_ratones.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('celulas_saludable_muertas_ratone.png', img3)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
histG = cv2.calcHist([img3], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

height, width = img3.shape
for i in range(height):
    for j in range(width):
        if(img3[i][j]>=195):
            res[i][j]=0
        

cv2.imshow('Porfaa',res)

plt.plot(hist, color='gray' )
plt.plot(hist2, color='red' )
plt.plot(histG, color='blue' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()