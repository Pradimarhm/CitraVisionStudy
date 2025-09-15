import cv2
import numpy as np

image = cv2.imread('Acara_3/img/daun.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
matriksSatu = np.ones(image.shape[:2],image.dtype)*100

citrapengurangan = cv2.subtract(gray, matriksSatu)
filename1 = 'Acara_3/img/output/CitraP1.jpeg'
filename2 = 'Acara_3/img/output/CitraP2.jpeg'
filename3 = 'Acara_3/img/output/CitraPenguranganahan.jpeg'

cv2.imwrite(filename1, gray)
cv2.imwrite(filename2, matriksSatu)
cv2.imwrite(filename3, citrapengurangan)
cv2.waitKey(0)
