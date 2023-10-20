import numpy as np
import cv2 as cv

h_c = cv.CascadeClassifier('haarcascade_default.xml')

people = ['Ben Afflek','Elton John','Jerry Seinfeld','Madonna','Mindy Kaling']
# features = np.load('features.npy')
# labels =  np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('Resources/Faces/val/elton_john/2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person',gray)

# Detect face in image

faces_rect =  h_c.detectMultiScale(gray,1.1,4)
for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label,confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence} ')
    cv.putText(img, str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow('Detected Facee' ,img)

cv.waitKey(0)