import cv2
img = cv2.imread('./images/1.jpg',1)
print(img.shape)
print(img.size)

b,g,r = cv2.split(img)

b = 0



print(b)
cv2.imshow('image',cv2.resize(b,(800,300)))
cv2.imshow('image',cv2.resize(g,(800,300)))
cv2.imshow('image',cv2.resize(r,(800,300)))



cv2.waitKey(0)
cv2.destroyAllWindows()