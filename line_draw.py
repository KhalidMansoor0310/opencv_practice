import cv2
img = cv2.imread('./images/2.jpg',0)
resize = cv2.resize(img,(500,500))

# line drawing technique
# syntax 
# cv2.line(img,(x1_startCoardinate,y1_startCoardinate),
# (x2_startCoardinate,y2_startCoardinate),color in bgr,thickness)
line = cv2.line(resize,(100,100),(400,100),(0,0,255),6)

cv2.imshow("line drawing",line)
cv2.waitKey(0)
cv2.destroyAllWindows()