import cv2
import numpy as np
import matplotlib.pyplot as plt

# membaca citra dari path gambar
image_path = 'P4/img/duar.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) #membaca grayscale

# 1. Region Glowing
def region_growing(img, seed_point, threshold):
    h, w = img.shape
    segmented = np.zeros((h,w), dtype=np.uint8)
    segmented[seed_point] = 255
    region_intensity = img[seed_point]
    
    to_check = [seed_point]
    
    while to_check:
        current_point = to_check.pop(0)
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                x, y = current_point[0  ] + dx, current_point[1] + dy
                if 0 <= x < h and 0 <= y <w and segmented[x,y] == 0:
                    if abs(int(img[x, y]) - int(region_intensity)) <= threshold:
                        segmented[x,y] = 255
                        to_check.append((x,y))
                        
    return segmented

seed = (10,10)
threshold_value = 20
segmented_image = region_growing(image,seed, threshold_value)

#2. K-Means Clustering (K + 2)
def kmeans_clustering(image, k):
    pixel_values = image.reshape(-1, 1)
    pixel_values = np.float32(pixel_values)
    # definisikan kriteria untuk algoritm k-measn
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # ubah label menjadi citra hasil klaster
    centers = np.uint8(centers)
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image.shape)
    
    return segmented_image

segmented_image_kmeans = kmeans_clustering(image, 2)

# 3. watershed segmentation
def watershed_segmentation(image):
    # menggunakan tresholding untuk binerlisasi
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV  + cv2.THRESH_OTSU)
    
    # mengubah moroflogi untuk menghilangkan noise
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    
    # Tentukan sure background dan sure foreground
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    
    # label unknow region
    sure_fg = np.uint8(sure_fg)
    unknow = cv2.subtract(sure_bg, sure_fg)
    
    # label maker
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknow == 255] = 0
    
    # watershed
    markers = cv2.watershed(cv2.cvtColor(image, cv2.COLOR_GRAY2BGR), markers)
    image[markers == -1] = [255]
    
    return image

watershed_iamge = watershed_segmentation(image)

# 4. Global thresholding (T = 100)
def global_tresholding(image, treshold_value):
    _, binary_image = cv2.threshold(image, treshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

global_treshold_image = global_tresholding(image, 100)

# 5. Adaptive global_tresholding
def adaptive_thresholding(image):
    adaptive_thresh_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    adaptive_thresh_gausian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return adaptive_thresh_mean, adaptive_thresh_gausian

adaptive_thresh_mean, adaptive_thresh_gausian = adaptive_thresholding(image)

# plot semua hasil secara bersamaan
plt.figure(figsize=(15, 10))

# original image
plt.subplot(3, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('original image')

# Region Growing result
plt.subplot(3, 2, 2)
plt.imshow(segmented_image, cmap='gray')
plt.title('region growing')

# k-mean clustering result
plt.subplot(3, 2, 3)
plt.imshow(segmented_image_kmeans, cmap='gray')
plt.title('K-means Clustering')

# watershed result
plt.subplot(3,2,4)
plt.imshow(watershed_iamge, cmap='gray')
plt.title('Watershed Segmentation')

# Global Thersholding result
plt.subplot(3,2,5)
plt.imshow(global_treshold_image, cmap='gray')
plt.title('Global Tresholding')

# Adaptive Thersholding result
plt.subplot(3,2,6)
plt.imshow(adaptive_thresh_mean, cmap='gray')
plt.title('Adaptive Tresholding (Mean)')

plt.tight_layout()
plt.show()