import cv2
import numpy as np

image = cv2.imread('Acara_3/img/daun.jpeg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

matriks = np.ones(image.shape[:2],image.dtype)*255

citranegiatif = matriks-gray

filename1 = 'Acara_3/img/output/daun_negative.jpeg'
cv2.imwrite(filename1, citranegiatif)
cv2.waitKey(0)

