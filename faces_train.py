#pylint:disable=no-member

import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']

DIR = r'C:\Users\user\Desktop\Projects\practice\Resources\Faces\train'
# Haarcascade - to read those 33000 lines of code
h_c = cv.CascadeClassifier('haarcascade_default.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            

            # now for detection
            rect = h_c.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for(x,y,w,h) in rect:

               faces_roi = gray[y:y+h,x:x+w]
               features.append(faces_roi)
               labels.append(label)

create_train()
print('Training Done')

# print(f'length of features = {len(features)}')
# print(f'length of labels = {len(labels)}')

# Set features and labels
features = np.array(features,dtype = 'object') 
labels = np.array(labels)

# Instantiating the face recogniser
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Now train the face recognizer on the features list and labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)