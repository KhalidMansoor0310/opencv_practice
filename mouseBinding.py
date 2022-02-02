import cv2 
import numpy as np

def mouseBind(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK():
        cv2.circle(img,(x,y),100,(0,0,100),3)


cv2.namedWindow(winname='res')
# img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('./images/1.jpg')
cv2.setMouseCallback("res",mouseBind)

while True:
    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()

