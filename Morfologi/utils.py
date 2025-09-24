import cv2
import numpy as np
import os

def load_or_create_image(path=None, is_object=True, size=(200, 200)):
    """
    Memuat gambar dari path (grayscale + threshold biner) atau buat sintetis.
    is_object: True untuk gambar objek, False untuk tulisan.
    size: Ukuran fallback sintetis.
    """
    if path and os.path.exists(path):
        img = cv2.imread(path, 0)  # Load grayscale
        if img is None:
            print(f"Warning: Gagal load {path}. Menggunakan gambar sintetis.")
            path = None
    if not path:
        # Fallback: Buat gambar sintetis
        if is_object:
            img = np.zeros(size, dtype=np.uint8)
            cv2.circle(img, (size[1]//2, size[0]//2), 40, 255, -1)  # Lingkaran
            cv2.rectangle(img, (size[1]//2 + 20, size[0]//4), (size[1]//2 + 70, size[0]//2), 255, -1)  # Persegi
            # Tambah noise ringan
            noise = np.random.randint(0, 2, size, dtype=np.uint8) * 255 * 0.1
            img = cv2.bitwise_or(img, noise.astype(np.uint8))
        else:
            h, w = size
            img = np.zeros((h, w * 1.5), dtype=np.uint8)  # Lebih lebar untuk tulisan
            cv2.putText(img, 'HELLO', (20, h//2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 2, 255, 3)
    # Threshold ke biner (hitam=0, putih=255)
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # Resize jika terlalu besar
    if img.shape[0] > size[0]:
        img = cv2.resize(img, size)
    return img

def create_kernel(shape=(5, 5), element_type=cv2.MORPH_RECT):
    """
    Buat structuring element (kernel).
    shape: Ukuran (misalnya (5,5) atau (11,11)).
    element_type: cv2.MORPH_RECT (persegi), cv2.MORPH_ELLIPSE (elips), dll.
    """
    if element_type == cv2.MORPH_ELLIPSE:
        return cv2.getStructuringElement(element_type, shape)
    else:
        return np.ones(shape, np.uint8)

def calculate_area(img):
    """Hitung luas area piksel putih (non-zero)."""
    return cv2.countNonZero(img)