import cv2
import numpy as np

persegi = np.zeros((400,400),dtype="uint8")
cv2.rectangle(persegi,(60,60),(340,340),255,-1)

lingkaran = np.zeros((400,400),dtype="uint8")
cv2.circle(lingkaran, (200,200), 150, 255, -1)

operasiAND = cv2.bitwise_xor(persegi,lingkaran)

cv2.imshow("persegi", persegi)
cv2.imshow("lingkaran", lingkaran)
cv2.imshow("operasi and", operasiAND)
cv2.waitKey(0)