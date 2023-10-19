'''
docstringggggg
'''

import cv2 as cv

# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cats',img)

def rescaleFrame(frame,scale = 0.2):
    w = int(frame.shape[1]*scale)
    h = int(frame.shape[0]*scale)

    dimensions = (w,h)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA  )

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cats',img)
img2 = rescaleFrame(img)
cv.imshow('Cats resized', img2)

cv.waitKey(0)