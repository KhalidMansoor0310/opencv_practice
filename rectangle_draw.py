import cv2
img = cv2.imread('./images/3.jpg',1)
# resize = cv2.resize(img,(500,500))

# rectangle drawing technique
# cv2.rectangle(img,(x1,y1),(x2,y2),color,thickness)
start_coardinates = (150,20)
end_coardinates = (300,200)
color = (255,130,100)
thickness = 7

rectangle = cv2.rectangle(img,start_coardinates,end_coardinates,color,thickness)
cv2.imshow('reactangle drawing technique',rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()