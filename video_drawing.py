from turtle import color
import cv2
import datetime

cap = cv2.VideoCapture('videos/Cars - 1900.mp4')
while True:
    ret,frame = cap.read()
    # resize = cv2.resize(frame,(500,500))
    # cv2.putText(frame,text,org,fontFace,fontScale,color,thickness)
    text = "Width" + str(cap.get(3)) + '   Height:'+ str(cap.get(4)) + str(datetime.datetime.now())
    org  = (100,100)
    fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL
    fontScale = 1
    color=(0,0,255)
    thickness = 2
    text = cv2.putText(frame,text,org,fontFace,fontScale,color,thickness)
    cv2.imshow('Video',text)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()