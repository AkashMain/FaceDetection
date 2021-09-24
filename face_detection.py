import cv2 as cv

#cap=cv.VideoCapture('C:\Code From VScode\Python\OpenCV\Videos\dog_video.mp4')
cap=cv.VideoCapture(0)
haar_cascade=cv.CascadeClassifier('haar_face.xml')

while True:

    isTrue,frame = cap.read()
    #frame = cv.cvtColor(frame,0)
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    face_rectangle = haar_cascade.detectMultiScale(gray,1.3,3)    

    if (len(face_rectangle) > 0):
        (x,y,a,b) = face_rectangle[0]
        frame = cv.rectangle(frame,(x,y),(x+a,y+b),(0,255,0),2)

    cv.imshow('Frame',frame)
    if cv.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv.destroyAllWindows()

