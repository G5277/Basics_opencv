import cv2 as cv


capture = cv.VideoCapture(0)

# Resolution change thingy just works on live webcam vids and not standalone vid fles
capture2 = capture
def change_reso(h, w):
    capture2.set(7,h)
    capture2.set(7,w)

while True:
    isTrue,frame = capture.read() 
    isTrue,frame2 = capture2.read()
    cv.imshow('Dog Video ', frame)
    cv.imshow('Dog Video 2', frame2)
    
    if cv.waitKey(20) & 0xFF == ord('e'):
        break
capture.release()
cv.destroyAllWindows()