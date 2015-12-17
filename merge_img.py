import cv2

img1 = cv2.imread('e_profile.jpg')
img2 = cv2.imread('e_caption.png')

# img1 = cv2.imread('img1.png')
# img2 = cv2.imread('logo.png')

# height, width, depth = img1.shape
# print height, width, depth
#
# height, width, depth = img2.shape
# print height, width, depth


dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()