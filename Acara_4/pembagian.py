import cv2
import numpy as np

image = cv2.imread('Acara_4\img\daun.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
matriksSatu = np.ones(image.shape[:2],image.dtype)*100

citrapembagian = cv2.divide(gray,matriksSatu)
filename = 'Acara_4\img\output\pembagian\kali_daun.jpeg'
filename3 = 'Acara_4\img\output\pembagian\daun3.jpeg'
filename2 = 'Acara_4\img\output\pembagian\daun2.jpeg'
cv2.imwrite(filename, citrapembagian)
cv2.imwrite(filename2, matriksSatu)
cv2.imwrite(filename3, image)
cv2.waitKey(0)