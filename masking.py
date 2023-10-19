import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/Cat.jpg')
cv.imshow('Cats',img)

img2 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('Cats Gray',img2)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

mask = cv.circle(blank, (img.shape[1]//2 - 120,img.shape[0]//2),100,255,-1)
cv.imshow('Mask', mask)

masked = cv.bitwise_or(img,img2,mask = mask)
cv.imshow('Masked',masked)

cv.waitKey(0)