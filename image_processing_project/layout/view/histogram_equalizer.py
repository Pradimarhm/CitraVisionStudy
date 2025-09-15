import cv2
from matplotlib import pyplot as plt

#path ke gambar
image_path = 'image_processing_project/assets/img/download.jpg'

#memuat gambar
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#melakukan histogram equalizationm
equalization_image = cv2.equalizeHist(image)

#menampilkan gambar asli dan gambar yang telah di equalize
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Gambar Asli')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Gambar setelah Equalization')
plt.imshow(equalization_image, cmap='gray')
plt.axis('off')

plt.show()