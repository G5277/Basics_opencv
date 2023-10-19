# used a lot in IR 
# especially while masking

import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

# BITWISE AND == RETURNS INTERSECTION OF TWO IMAGES
b_and = cv.bitwise_and(rectangle,circle)
cv.imshow('B and',b_and)

# BITWISE OR == RETURNS UNION OF TWO IMAGES
b_or = cv.bitwise_or(rectangle,circle)
cv.imshow('B or',b_or)


# BITWISE XOR == RETURNS NON- INTERSECTING REGIONS OF TWO IMAGES
b_Xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('B Xor',b_Xor)


# BITWISE NOT == RETURNS IMAGE WITH INVERTED BINARY COLOR
b_not_r = cv.bitwise_not(rectangle)
b_not_c = cv.bitwise_not(circle)
cv.imshow('B not r',b_not_r)
cv.imshow('B not c',b_not_c)



cv.waitKey(0)