import cv2

img = cv2.imread('C:/Users/bhagy/OneDrive/Pictures/Desktop/internship/image1.jpeg')
resized = cv2.resize(img, (300, 300))

cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()