import numpy as np
import cv2
import matplotlib.pyplot as plt

def fuzzy_membership_function(x, mean, stddev):
    return np.exp((-(x - mean) ** 2)/(2 * (stddev ** 2)))

def fuzzy_histogram_equalization(image, block_size=16):
    #konfersi gambar ke grayscale jika diperlukan
    if len (image.shape)==3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    
    #dapatkan dimensi gambar
    height , width = image.shape
    
    #buat gambar yang telah di equalize
    equalized_image = np.zeros_like(image, dtype=np.uint8)
    
    #ukuran block
    block_height = block_size
    block_width = block_size
    
    for y in range(0, height, block_height):
        for x in range(0, width, block_width):
            #definisikan batas blok
            block = image[y:y+block_height, x:x+block_width]
            if block.size == 0:
                continue
            
            #hitung histogram lokal 
            hist, bins = np.histogram(block.flatten(), bins=256, range=[0,256])
            cdf = hist.cumsum()
            cdf_normalized = cdf * 255 / cdf[-1]
            equalized_block = np.interp(block.flatten(), bins[:-1], cdf_normalized).reshape(block.shape)
            
            #hitung keanggotaan fuzzy
            mean = np.mean(equalized_block)
            stddev = np.std(equalized_block) if np.std(equalized_block) > 0 else 1
            membership = fuzzy_membership_function(equalized_block, mean, stddev)

            # normalisasi membership ke 0-255
            membership_norm = cv2.normalize(membership, None, 0, 255, cv2.NORM_MINMAX)

            # gabungkan hasil HE dengan fuzzy membership (bisa diatur bobotnya)
            fuzzy_block = 0.6 * equalized_block + 0.4 * membership_norm

            
            #terapkan penyesuaian kontras fuzzy
            equalized_image[y:y+block_height, x:x+block_width] = np.clip(fuzzy_block, 0, 255)
            
    return equalized_image
    
#path ke gambar
image_path = 'image_processing_project/assets/img/aw.jpg'

#memuat gambar
image = cv2.imread(image_path)

#melakukan histogram equalizationm
fhe_image = fuzzy_histogram_equalization(image)

#menampilkan gambar asli dan gambar yang telah di equalize
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Gambar Asli')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Gambar setelah Equalization')
plt.imshow(fhe_image, cmap='gray')
plt.axis('off')

plt.show()