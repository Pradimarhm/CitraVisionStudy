import cv2

imgGray = cv2.imread('Acara_3/img/daun.jpeg', cv2.IMREAD_GRAYSCALE)
# imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filename1 = 'Acara_3/img/output/daun_gray2.jpeg'
cv2.imwrite(filename1, imgGray)
cv2.waitKey(0)