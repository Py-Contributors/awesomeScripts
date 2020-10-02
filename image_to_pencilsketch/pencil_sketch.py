import cv2
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.image as mpimg

img = cv2.imread('image.jpg')
#plt.imshow(img)

conversion_pct = 0.20
height = int(conversion_pct*img.shape[0])
width = int(conversion_pct*img.shape[1])
dim = (width, height)
img_resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img_resized, cv2.COLOR_BGR2HSV)

inv = 255-gray 
gauss = cv2.GaussianBlur(inv,ksize=(15,15),sigmaX=0,sigmaY=0)

pencil = cv2.divide(gray,255-gauss,scale=256)


cv2.imshow('resized', img_resized)
cv2.imshow('gray', gray)
cv2.imshow('hsv', hsv)
cv2.imshow('pencil', pencil)

cv2.waitKey(0)
   
cv2.destroyAllWindows()
