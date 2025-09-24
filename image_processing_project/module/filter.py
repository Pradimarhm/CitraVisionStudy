# filters.py
import numpy as np
import cv2
from PIL import Image
from PyQt5.QtGui import QImage

def label_to_pil(label):
    """
    Ambil isi QLabel (QPixmap) dan konversi ke PIL.Image
    """
    pixmap = label.pixmap()
    if pixmap is None:
        return None

    qimg = pixmap.toImage().convertToFormat(QImage.Format_RGBA8888)
    width = qimg.width()
    height = qimg.height()
    ptr = qimg.bits()
    ptr.setsize(qimg.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  # RGBA

    # Buang alpha kalau tidak perlu
    return Image.fromarray(arr[..., :3], mode="RGB")

def identify_filter(label_before):
    """
    Contoh: konversi grayscale + deteksi tepi.
    Input  : PIL.Image
    Output : PIL.Image (grayscale edges)
    """
    # PIL -> numpy (RGB)
    
    pil_image = label_to_pil(label_before)
    if pil_image is None:
        return None
    
    arr = np.array(pil_image)
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    # numpy -> PIL grayscale
    return Image.fromarray(edges)

def edge_detection_1(arr):
    # Canny
    return cv2.Canny(arr, 100, 200)

def edge_detection_2(arr):
    # Sobel
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
    sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    mag = cv2.magnitude(sx, sy)
    return cv2.convertScaleAbs(mag)

def edge_detection_3(arr):
    # Laplacian
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    return cv2.convertScaleAbs(lap)

def sharpen_filter(arr):
    """
    arr: numpy array RGB
    return: numpy array RGB hasil sharpen
    """
    # Kernel sharpen sederhana
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]], dtype=np.float32)
    sharpened = cv2.filter2D(arr, -1, kernel)
    return sharpened