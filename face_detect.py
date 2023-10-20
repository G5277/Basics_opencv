import cv2 as cv

img = cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('face',img)

# GrayScale the image

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray face',gray)

# Haarcascade - to read those 33000 lines of code
h_c = cv.CascadeClassifier('haarcascade_default.xml')

# now for detection
rect = h_c.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=1)

# print number of faces found
print(f'Number of faces found = {len(rect)}')

for(x,y,w,h) in rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=1)

cv.imshow('Detected Faces', img)

cv.waitKey(0)