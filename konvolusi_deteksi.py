import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color, filters, feature
from scipy.ndimage import convolve
import cv2

# Load image chelsea dan ubah ke grayscale
image = data.chelsea()
image_gray = color.rgb2gray(image)

# Kernel 5x5 contoh (Gaussian blur kernel)
kernel_5x5 = np.array([
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1]
], dtype=np.float32)
kernel_5x5 /= kernel_5x5.sum()

# a. Konvolusi manual dengan padding refleksi
def manual_convolve(image, kernel):
    pad_size = kernel.shape[0] // 2
    # Padding dengan mode 'reflect'
    padded = np.pad(image, pad_size, mode='reflect')
    output = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded[i:i+kernel.shape[0], j:j+kernel.shape[1]]
            output[i, j] = np.sum(region * kernel)
    return output

conv_manual = manual_convolve(image_gray, kernel_5x5)

# b. Konvolusi otomatis dengan scipy.ndimage.convolve dengan mode reflect
conv_auto = convolve(image_gray, kernel_5x5, mode='reflect')

# Deteksi tepi

# a. Sobel kernel 5x5 (gunakan kernel Sobel yang diperbesar)
# Sobel 3x3 standar
sobel_x_3x3 = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=np.float32)

# Membuat kernel Sobel 5x5 dengan interpolasi (contoh sederhana)
sobel_x_5x5 = np.array([
    [-2, -1, 0, 1, 2],
    [-3, -2, 0, 2, 3],
    [-4, -3, 0, 3, 4],
    [-3, -2, 0, 2, 3],
    [-2, -1, 0, 1, 2]
], dtype=np.float32)
sobel_y_5x5 = sobel_x_5x5.T

# Hitung gradien x dan y dengan konvolusi
grad_x = convolve(image_gray, sobel_x_5x5, mode='reflect')
grad_y = convolve(image_gray, sobel_y_5x5, mode='reflect')
sobel_edge = np.hypot(grad_x, grad_y)
sobel_edge = sobel_edge / sobel_edge.max()

# b. Deteksi tepi Canny dengan threshold 150-250
# Canny membutuhkan citra uint8
image_uint8 = (image_gray * 255).astype(np.uint8)
canny_edge = cv2.Canny(image_uint8, threshold1=150, threshold2=250)

# c. Deteksi Prewitt kernel 5x5
# Prewitt 3x3 standar
prewitt_x_3x3 = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=np.float32)

# Membuat kernel Prewitt 5x5 (contoh sederhana)
prewitt_x_5x5 = np.array([
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2]
], dtype=np.float32)
prewitt_y_5x5 = prewitt_x_5x5.T

grad_x_prewitt = convolve(image_gray, prewitt_x_5x5, mode='reflect')
grad_y_prewitt = convolve(image_gray, prewitt_y_5x5, mode='reflect')
prewitt_edge = np.hypot(grad_x_prewitt, grad_y_prewitt)
prewitt_edge = prewitt_edge / prewitt_edge.max()

# Visualisasi hasil dengan skema warna berbeda
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
ax = axes.ravel()

ax[0].imshow(image_gray, cmap='gray')
ax[0].set_title('Original Grayscale')
ax[0].axis('off')

ax[1].imshow(conv_manual, cmap='gray')
ax[1].set_title('Manual Convolution 5x5')
ax[1].axis('off')

ax[2].imshow(conv_auto, cmap='gray')
ax[2].set_title('Automatic Convolution 5x5')
ax[2].axis('off')

ax[3].imshow(sobel_edge, cmap='inferno')  # skema warna berbeda
ax[3].set_title('Sobel Edge 5x5 (Inferno)')
ax[3].axis('off')

ax[4].imshow(canny_edge, cmap='plasma')  # skema warna berbeda
ax[4].set_title('Canny Edge (150-250) (Plasma)')
ax[4].axis('off')

ax[5].imshow(prewitt_edge, cmap='viridis')  # skema warna berbeda
ax[5].set_title('Prewitt Edge 5x5 (Viridis)')
ax[5].axis('off')

plt.tight_layout()
plt.show()
