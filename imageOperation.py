import cv2

img = cv2.imread('./images/1.jpg',1)

print(f'size of an image is {img.size} the shape of an image is {img.shape} ')
# splitting the channels of an image 
b,g,r = cv2.split(img)

cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)
cv2.imshow('Operation on images',img)

# Merging the images channel again 
cv2.imshow('Merge the image again',cv2.merge([b,g,r]))

cv2.waitKey()
cv2.destroyAllWindows()