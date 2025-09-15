# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('Acara_5/img/daun.jpeg')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# matriks = np.ones(img.shape[:2],img.dtype)*255
# negasi = matriks-gray

# plt.hist(img.ravel(), 256, [0,256])
# plt.savefig('Acara_5/img/output/2/CitraHistI.jpeg')
# filename1 = 'Acara_5/img/output/2/CitraHistIImg.jpeg'
# cv2.imwrite(filename1, img)

# plt.hist(gray.ravel(), 256, [0,256])
# plt.savefig('Acara_5/img/output/2/CitraHistGray.jpeg')
# filename2 = 'Acara_5/img/output/2/CitraHistGrayImg.jpeg'
# cv2.imwrite(filename2, gray)

# plt.hist(negasi.ravel(), 256, [0,256])
# plt.savefig('Acara_5/img/output/2/CitraHistNegasi.jpeg')
# filename3 = 'Acara_5/img/output/2/CitraHistNegasiImg.jpeg'
# cv2.imwrite(filename3, negasi)

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Baca gambar asli
img = cv2.imread('Acara_5/img/daun.jpeg')

# Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Buat citra negatif dengan cara lain
negasi = cv2.bitwise_not(gray)

# === Histogram Gambar Asli ===
plt.figure()
hist_img = cv2.calcHist([img], [0], None, [256], [0,256]) \
         + cv2.calcHist([img], [1], None, [256], [0,256]) \
         + cv2.calcHist([img], [2], None, [256], [0,256])
plt.plot(hist_img)
plt.xlim([0,256])
plt.savefig('Acara_5/img/output/2/CitraHistI.jpeg')
cv2.imwrite('Acara_5/img/output/2/CitraHistIImg.jpeg', img)

# === Histogram Gambar Grayscale ===
plt.figure()
hist_gray = cv2.calcHist([gray], [0], None, [256], [0,256])
plt.plot(hist_gray)
plt.xlim([0,256])
plt.savefig('Acara_5/img/output/2/CitraHistGray.jpeg')
cv2.imwrite('Acara_5/img/output/2/CitraHistGrayImg.jpeg', gray)

# === Histogram Gambar Negatif ===
plt.figure()
hist_neg = cv2.calcHist([negasi], [0], None, [256], [0,256])
plt.plot(hist_neg)
plt.xlim([0,256])
plt.savefig('Acara_5/img/output/2/CitraHistNegasi.jpeg')
cv2.imwrite('Acara_5/img/output/2/CitraHistNegasiImg.jpeg', negasi)
