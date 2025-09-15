import cv2
import numpy as np

image = cv2.imread('Acara_4\img\daun.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
matriksSatu = np.ones(image.shape[:2],image.dtype)*100

citraperkalian = cv2.multiply(gray,matriksSatu)
filename = 'Acara_4\img\output\perkalian\kali_daun.jpeg'
filename3 = 'Acara_4\img\output\perkalian\daun3.jpeg'
filename2 = 'Acara_4\img\output\perkalian\daun2.jpeg'
cv2.imwrite(filename, citraperkalian)
cv2.imwrite(filename2, matriksSatu)
cv2.imwrite(filename3, image)
cv2.waitKey(0)