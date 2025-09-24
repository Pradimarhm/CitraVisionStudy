import matplotlib.pyplot as plt
import cv2
import numpy as np

# Impor modul-modul
from utils import load_or_create_image, create_kernel, calculate_area
from dilation import dilate_image, expand_text_area
from erotion import erode_image
from opening import opening_image, refine_object
from closing import closing_image

# Path gambar (sesuaikan jika perlu)
OBJECT_PATH = 'Morfologi/img/436fcb7a-a3f4-44db-adfc-2ae57e2a73ce.jpg'
TEXT_PATH = 'Morfologi/img/847081ba-1dce-4bf2-8339-960e02f9ed32.jpg'

# Load gambar
print("Memuat gambar...")
object_img = load_or_create_image(OBJECT_PATH, is_object=True)
text_img = load_or_create_image(TEXT_PATH, is_object=False)

# Kernel
kernel_main = create_kernel((5, 5))  # Bisa ganti ke (11,11)
kernel_ellipse = create_kernel((7, 7), cv2.MORPH_ELLIPSE)

print("Luas area tulisan asli:", calculate_area(text_img))
print("Luas area objek asli:", calculate_area(object_img))

# 1. Operasi pada Gambar Objek
print("\n=== OPERASI PADA GAMBAR OBJEK ===")
dilated_obj = dilate_image(object_img, kernel_main, iterations=1)
eroded_obj = erode_image(object_img, kernel_main, iterations=1)
opening_obj = opening_image(object_img, kernel_main)
closing_obj = closing_image(object_img, kernel_main)
refined_obj = refine_object(object_img, kernel_main, kernel_ellipse)
print("Luas area objek setelah penyempurnaan:", calculate_area(refined_obj))

# 2. Operasi pada Gambar Tulisan
print("\n=== OPERASI PADA GAMBAR TULISAN ===")
dilated_text = dilate_image(text_img, kernel_main, iterations=1)
eroded_text = erode_image(text_img, kernel_main, iterations=1)
opening_text = opening_image(text_img, kernel_main)
closing_text = closing_image(text_img, kernel_main)
expanded_text, iterations_expand = expand_text_area(text_img, kernel_main)
print("Iterations dilatasi untuk 2x lipat:", iterations_expand)
print("Luas area tulisan setelah perluasan:", calculate_area(expanded_text))

# 3. Visualisasi Hasil (2 baris x 6 kolom)
fig, axes = plt.subplots(2, 6, figsize=(24, 8))

# Gambar Objek (baris 0)
axes[0, 0].imshow(object_img, cmap='gray'); axes[0, 0].set_title('Objek Asli')
axes[0, 1].imshow(dilated_obj, cmap='gray'); axes[0, 1].set_title('Dilasi Objek')
axes[0, 2].imshow(eroded_obj, cmap='gray'); axes[0, 2].set_title('Erosi Objek')
axes[0, 3].imshow(opening_obj, cmap='gray'); axes[0, 3].set_title('Pembukaan Objek')
axes[0, 4].imshow(closing_obj, cmap='gray'); axes[0, 4].set_title('Penutupan Objek')
axes[0, 5].imshow(refined_obj, cmap='gray'); axes[0, 5].set_title('Penyempurnaan Objek')

# Gambar Tulisan (baris 1)
axes[1, 0].imshow(text_img, cmap='gray'); axes[1, 0].set_title('Tulisan Asli')
axes[1, 1].imshow(dilated_text, cmap='gray'); axes[1, 1].set_title('Dilasi Tulisan')
axes[1, 2].imshow(eroded_text, cmap='gray'); axes[1, 2].set_title('Erosi Tulisan')
axes[1, 3].imshow(opening_text, cmap='gray'); axes[1, 3].set_title('Pembukaan Tulisan')
axes[1, 4].imshow(closing_text, cmap='gray'); axes[1, 4].set_title('Penutupan Tulisan')
axes[1, 5].imshow(expanded_text, cmap='gray'); axes[1, 5].set_title('Perluasan 2x Tulisan')

for ax in axes.flat:
    ax.axis('off')
plt.tight_layout()
plt.show()

# Simpan hasil
cv2.imwrite('refined_object.png', refined_obj)
cv2.imwrite('expanded_text.png', expanded_text)
print("\nHasil disimpan: refined_object.png dan expanded_text.png")