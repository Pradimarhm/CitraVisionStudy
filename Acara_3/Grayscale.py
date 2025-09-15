import cv2

image = cv2.imread('Acara_3/img/daun.jpeg')
imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filename1 = 'Acara_3/img/output/daun_gray.jpeg'
cv2.imwrite(filename1, imgGray)
cv2.waitKey(0)