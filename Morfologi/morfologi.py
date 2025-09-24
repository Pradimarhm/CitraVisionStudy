import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Fungsi untuk memuat/membuat gambar objek (biner: hitam=0, putih=255)
def create_object_image(path=None):
    if path and os.path.exists(path):
        img = cv2.imread(path, 0)  # Load grayscale
        if img is None:
            print(f"Warning: Gagal load {path}. Menggunakan gambar sintetis.")
            path = None
    if not path:
        # Fallback: Buat gambar sintetis
        img = np.zeros((200, 200), dtype=np.uint8)
        cv2.circle(img, (100, 100), 40, 255, -1)  # Lingkaran
        cv2.rectangle(img, (120, 50), (170, 100), 255, -1)  # Persegi
        # Tambah noise ringan
        noise = np.random.randint(0, 2, (200, 200), dtype=np.uint8) * 255 * 0.1
        img = cv2.bitwise_or(img, noise.astype(np.uint8))
    # Threshold ke biner
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return img

# Fungsi untuk memuat/membuat gambar tulisan (biner)
def create_text_image(path=None):
    if path and os.path.exists(path):
        img = cv2.imread(path, 0)  # Load grayscale
        if img is None:
            print(f"Warning: Gagal load {path}. Menggunakan gambar sintetis.")
            path = None
    if not path:
        # Fallback: Buat gambar sintetis
        img = np.zeros((200, 300), dtype=np.uint8)
        cv2.putText(img, 'HELLO', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, 255, 3)
    # Threshold ke biner
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return img

# Load gambar dari path (atau fallback ke sintetis)
object_img = create_object_image('Morfologi/img/raoul-droog-yMSecCHsIBc-unsplash.jpg')
text_img = create_text_image('Morfologi/img/LOREM.png')

# Resize jika gambar terlalu besar untuk visualisasi (opsional, sesuaikan)
object_img = cv2.resize(object_img, (1000, 1000)) if object_img.shape[0] > 200 else object_img
text_img = cv2.resize(text_img, (1000, 1000)) if text_img.shape[0] > 200 else text_img

# Kernel utama (bisa diganti ke np.ones((11,11), np.uint8) untuk efek lebih besar)
kernel_main = np.ones((11, 11), np.uint8)

# Kernel alternatif untuk penyempurnaan objek (elips untuk smoothing berbeda)
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))

print("Luas area tulisan asli:", cv2.countNonZero(text_img))
print("Luas area objek asli:", cv2.countNonZero(object_img))

# 1. Operasi pada Gambar Objek
print("\n=== OPERASI PADA GAMBAR OBJEK ===")
# Dilatasi (iterations disesuaikan untuk ekspansi sedang)
dilated_obj = cv2.dilate(object_img, kernel_main, iterations=1)

# Erosi (iterations untuk kontraksi)
eroded_obj = cv2.erode(object_img, kernel_main, iterations=1)

# Pembukaan
opening_obj = cv2.morphologyEx(object_img, cv2.MORPH_OPEN, kernel_main)

# Penutupan
closing_obj = cv2.morphologyEx(object_img, cv2.MORPH_CLOSE, kernel_main)

# Penyempurnaan objek hingga tidak seperti semula (opening + closing berulang dengan kernel elips)
refined_obj = cv2.morphologyEx(opening_obj, cv2.MORPH_CLOSE, kernel_ellipse, iterations=1)
refined_obj = cv2.morphologyEx(refined_obj, cv2.MORPH_OPEN, kernel_ellipse, iterations=1)
# refined_obj = cv2.morphologyEx(opening_obj, cv2.MORPH_CLOSE, kernel_main, iterations=1)
# refined_obj = cv2.morphologyEx(refined_obj, cv2.MORPH_OPEN, kernel_main, iterations=1)

print("Luas area objek setelah penyempurnaan:", cv2.countNonZero(refined_obj))

# 2. Operasi pada Gambar Tulisan
print("\n=== OPERASI PADA GAMBAR TULISAN ===")
# Dilatasi
dilated_text = cv2.dilate(text_img, kernel_main, iterations=1)

# Erosi
eroded_text = cv2.erode(text_img, kernel_main, iterations=1)

# Pembukaan
opening_text = cv2.morphologyEx(text_img, cv2.MORPH_OPEN, kernel_main)

# Penutupan
closing_text = cv2.morphologyEx(text_img, cv2.MORPH_CLOSE, kernel_main)

# Perluasan area tulisan hingga ~2x lipat (dilatasi dinamis)
original_area = cv2.countNonZero(text_img)
target_area = original_area * 2
expanded_text = text_img.copy()
iterations = 0
while cv2.countNonZero(expanded_text) < target_area and iterations < 10:  # Batasi iterations
    expanded_text = cv2.dilate(expanded_text, kernel_main, iterations=1)
    iterations += 1
print("Iterations dilatasi untuk 2x lipat:", iterations)
print("Luas area tulisan setelah perluasan:", cv2.countNonZero(expanded_text))

# 3. Visualisasi Hasil (diperbaiki: 2 baris x 6 kolom untuk menghindari overlap)
fig, axes = plt.subplots(2, 6, figsize=(24, 8))

# Gambar Objek (baris 0)
axes[0, 0].imshow(object_img, cmap='gray')
axes[0, 0].set_title('Objek Asli')
axes[0, 1].imshow(dilated_obj, cmap='gray')
axes[0, 1].set_title('Dilasi Objek')
axes[0, 2].imshow(eroded_obj, cmap='gray')
axes[0, 2].set_title('Erosi Objek')
axes[0, 3].imshow(opening_obj, cmap='gray')
axes[0, 3].set_title('Pembukaan Objek')
axes[0, 4].imshow(closing_obj, cmap='gray')
axes[0, 4].set_title('Penutupan Objek')
axes[0, 5].imshow(refined_obj, cmap='gray')  # Penyempurnaan di kolom 5
axes[0, 5].set_title('Penyempurnaan Objek')

# Gambar Tulisan (baris 1)
axes[1, 0].imshow(text_img, cmap='gray')
axes[1, 0].set_title('Tulisan Asli')
axes[1, 1].imshow(dilated_text, cmap='gray')
axes[1, 1].set_title('Dilasi Tulisan')
axes[1, 2].imshow(eroded_text, cmap='gray')
axes[1, 2].set_title('Erosi Tulisan')
axes[1, 3].imshow(opening_text, cmap='gray')
axes[1, 3].set_title('Pembukaan Tulisan')
axes[1, 4].imshow(closing_text, cmap='gray')  # Tambah closing untuk lengkap
axes[1, 4].set_title('Penutupan Tulisan')
axes[1, 5].imshow(expanded_text, cmap='gray')  # Perluasan di kolom 5
axes[1, 5].set_title('Perluasan 2x Tulisan')

for ax in axes.flat:
    ax.axis('off')
plt.tight_layout()
plt.show()

# Simpan hasil jika diperlukan (opsional)
cv2.imwrite('refined_object.png', refined_obj)
cv2.imwrite('expanded_text.png', expanded_text)
print("\nHasil disimpan: refined_object.png dan expanded_text.png")
