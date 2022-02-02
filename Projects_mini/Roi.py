import cv2
path = "C:/Users/khalid mansoor/Desktop/opencv_install/images/1.jpg"

img = cv2.imread(path,1)

#(190,25) (330,140)
#img[y1:y2,x1:x2]

# region of interest 
roi = img[25:140,190:330] 

# find the diference of y2-y1 and x2-x1
# img[25:140,330:370] = roi
img1 = cv2.imread('C:/Users/khalid mansoor/Desktop/opencv_install/images/2.jpg')
# replacing 2nd image head on first image 
roi = img1[20:220,180:390]
img[25:140,190:330] = roi
cv2.imshow("orignal",img)

cv2.waitKey(0)
cv2.destroyAllWindows()