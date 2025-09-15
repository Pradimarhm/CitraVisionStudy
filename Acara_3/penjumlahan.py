import cv2
import numpy as np

image = cv2.imread('Acara_3/img/daun.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
matriksSatu = np.ones(image.shape[:2],image.dtype)*100

citrapenjumlahan = cv2.add(gray, matriksSatu)
filename1 = 'Acara_3/img/output/Citra1.jpeg'
filename2 = 'Acara_3/img/output/Citra2.jpeg'
filename3 = 'Acara_3/img/output/CitraPenjumlahan.jpeg'

cv2.imwrite(filename1, gray)
cv2.imwrite(filename2, matriksSatu)
cv2.imwrite(filename3, citrapenjumlahan)
cv2.waitKey(0)
