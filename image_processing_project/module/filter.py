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

def gaussian_blur_3x3(img):
    """
    Apply Gaussian blur dengan kernel 3x3 pada numpy array gambar (BGR atau RGB).
    Input: numpy array (H, W, 3) atau grayscale.
    Output: numpy array yang sudah di-blur.
    """
    if img is None or len(img.shape) == 0:
        return img
    blurred = cv2.GaussianBlur(img, (3, 3), sigmaX=0.5)
    return blurred

def gaussian_blur_5x5(img):
    """
    Apply Gaussian blur dengan kernel 5x5 pada numpy array gambar (BGR atau RGB).
    Input: numpy array (H, W, 3) atau grayscale.
    Output: numpy array yang sudah di-blur.
    """
    if img is None or len(img.shape) == 0:
        return img
    blurred = cv2.GaussianBlur(img, (5, 5), sigmaX=0.8)
    return blurred

def unsharp_masking(img, strength=1.5):
    """
    Apply Unsharp Masking dengan kernel Gaussian 5x5 pada numpy array gambar (RGB atau BGR).
    Input: numpy array (H, W, 3) atau grayscale.
    Output: numpy array yang sudah di-sharpen.
    strength: Faktor penguatan detail (default 1.5; lebih tinggi = lebih tajam).
    """
    if img is None or len(img.shape) == 0:
        return img
    
    # Gaussian blur untuk dapatkan blurred version
    blurred = cv2.GaussianBlur(img, (7, 7), sigmaX=0.8)
    
    # Hitung detail: original - blurred
    detail = cv2.subtract(img, blurred)
    
    # Sharpen: original + (strength * detail)
    sharpened = cv2.addWeighted(img, 1.0, detail, strength, 0)
    
    return sharpened

def average_filter(img):
    """
    Apply Average (Mean) Filter dengan kernel 5x5 pada numpy array gambar (RGB atau BGR).
    Input: numpy array (H, W, 3) atau grayscale.
    Output: numpy array yang sudah di-blur dengan average.
    """
    if img is None or len(img.shape) == 0:
        return img
    
    # Average filter menggunakan cv2.blur (kernel uniform)
    blurred = cv2.blur(img, (9, 9))
    
    return blurred

def ideal_low_pass_filter(img, D0):
    """
    Apply Ideal Low-Pass Filter dengan cutoff radius D0 pada numpy array gambar.
    Input: numpy array (H, W, 3) untuk RGB/BGR atau (H, W) untuk grayscale.
    Output: numpy array yang sudah di-filter (low-pass).
    D0: Cutoff radius (frekuensi tinggi > D0 dibuang).
    """
    if img is None or len(img.shape) == 0:
        return img
    
    # Jika grayscale, shape (H, W); jika RGB, (H, W, 3)
    is_color = len(img.shape) == 3
    
    if is_color:
        # Apply per channel untuk warna
        channels = cv2.split(img)
        filtered_channels = []
        for channel in channels:
            filtered = _apply_lpf_single_channel(channel, D0)
            filtered_channels.append(filtered)
        result = cv2.merge(filtered_channels)
    else:
        # Grayscale
        result = _apply_lpf_single_channel(img, D0)
    
    return np.uint8(result)

def _apply_lpf_single_channel(channel, D0):
    """Helper: Apply LPF pada single channel (grayscale atau satu channel RGB)."""
    h, w = channel.shape
    
    # Padding agar ukuran genap (untuk FFT efisien)
    pad_h = h + (h % 2)
    pad_w = w + (w % 2)
    padded = cv2.copyMakeBorder(channel, 0, pad_h - h, 0, pad_w - w, cv2.BORDER_CONSTANT, value=0)
    
    # FFT 2D
    f = np.fft.fft2(padded)
    fshift = np.fft.fftshift(f)  # Shift ke pusat
    
    # Buat mask ideal low-pass
    rows, cols = padded.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.uint8)
    y, x = np.ogrid[:rows, :cols]
    mask_distance = np.sqrt((x - ccol)**2 + (y - crow)**2)
    mask[mask_distance <= D0] = 1
    
    # Kalikan spectrum dengan mask
    fshift_filtered = fshift * mask
    
    # Inverse FFT
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)  # Ambil magnitude (real part dominan)
    
    # Crop padding dan normalize ke 0-255
    center_h, center_w = img_back.shape[0] // 2, img_back.shape[1] // 2
    cropped = img_back[:h, :w] if h % 2 == 0 else img_back[1:h+1, :w]
    if w % 2 != 0:
        cropped = cropped[:, 1:w+1]
    normalized = cv2.normalize(cropped, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    
    return normalized

# Fungsi wrapper untuk 5x5 equivalent (D0=5)
def low_pass(img):
    return ideal_low_pass_filter(img, D0=3)

def ideal_high_pass_filter(img, D0):
    """
    Apply Ideal High-Pass Filter dengan cutoff radius D0 pada numpy array gambar.
    Input: numpy array (H, W, 3) untuk RGB/BGR atau (H, W) untuk grayscale.
    Output: numpy array yang sudah di-filter (high-pass).
    D0: Cutoff radius (frekuensi rendah <= D0 dibuang).
    """
    if img is None or len(img.shape) == 0:
        return img
    
    # Jika grayscale, shape (H, W); jika RGB, (H, W, 3)
    is_color = len(img.shape) == 3
    
    if is_color:
        # Apply per channel untuk warna
        channels = cv2.split(img)
        filtered_channels = []
        for channel in channels:
            filtered = _apply_hpf_single_channel(channel, D0)
            filtered_channels.append(filtered)
        result = cv2.merge(filtered_channels)
    else:
        # Grayscale
        result = _apply_hpf_single_channel(img, D0)
    
    return np.uint8(result)

def _apply_hpf_single_channel(channel, D0):
    """Helper: Apply HPF pada single channel (grayscale atau satu channel RGB)."""
    h, w = channel.shape
    
    # Padding agar ukuran genap (untuk FFT efisien)
    pad_h = h + (h % 2)
    pad_w = w + (w % 2)
    padded = cv2.copyMakeBorder(channel, 0, pad_h - h, 0, pad_w - w, cv2.BORDER_CONSTANT, value=0)
    
    # FFT 2D
    f = np.fft.fft2(padded)
    fshift = np.fft.fftshift(f)  # Shift ke pusat
    
    # Buat mask ideal high-pass
    rows, cols = padded.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.ones((rows, cols), np.uint8)  # Mulai dengan 1 (high-pass: potong low freq)
    y, x = np.ogrid[:rows, :cols]
    mask_distance = np.sqrt((x - ccol)**2 + (y - crow)**2)
    mask[mask_distance <= D0] = 0  # Set 0 untuk frekuensi rendah (<= D0)
    
    # Kalikan spectrum dengan mask
    fshift_filtered = fshift * mask
    
    # Inverse FFT
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)  # Ambil magnitude (real part dominan)
    
    # Crop padding dan normalize ke 0-255
    center_h, center_w = img_back.shape[0] // 2, img_back.shape[1] // 2
    cropped = img_back[:h, :w] if h % 2 == 0 else img_back[1:h+1, :w]
    if w % 2 != 0:
        cropped = cropped[:, 1:w+1]
    normalized = cv2.normalize(cropped, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    
    return normalized

# Fungsi wrapper untuk 5x5 equivalent (D0=5)
def high_pass(img):
    return ideal_high_pass_filter(img, D0=5)

def ideal_bandstop_filter(img, D1, D2):
    """
    Apply Ideal Bandstop Filter dengan inner radius D1 dan outer radius D2 pada numpy array gambar.
    Input: numpy array (H, W, 3) untuk RGB/BGR atau (H, W) untuk grayscale.
    Output: numpy array yang sudah di-filter (bandstop).
    D1: Inner radius (batas bawah band yang diremehkan).
    D2: Outer radius (batas atas band yang diremehkan; D2 > D1).
    """
    if img is None or len(img.shape) == 0:
        return img
    
    # Jika grayscale, shape (H, W); jika RGB, (H, W, 3)
    is_color = len(img.shape) == 3
    
    if is_color:
        # Apply per channel untuk warna
        channels = cv2.split(img)
        filtered_channels = []
        for channel in channels:
            filtered = _apply_bsf_single_channel(channel, D1, D2)
            filtered_channels.append(filtered)
        result = cv2.merge(filtered_channels)
    else:
        # Grayscale
        result = _apply_bsf_single_channel(img, D1, D2)
    
    return np.uint8(result)

def _apply_bsf_single_channel(channel, D1, D2):
    """Helper: Apply Bandstop pada single channel (grayscale atau satu channel RGB)."""
    h, w = channel.shape
    
    # Padding agar ukuran genap (untuk FFT efisien)
    pad_h = h + (h % 2)
    pad_w = w + (w % 2)
    padded = cv2.copyMakeBorder(channel, 0, pad_h - h, 0, pad_w - w, cv2.BORDER_CONSTANT, value=0)
    
    # FFT 2D
    f = np.fft.fft2(padded)
    fshift = np.fft.fftshift(f)  # Shift ke pusat
    
    # Buat mask ideal bandstop
    rows, cols = padded.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.ones((rows, cols), np.uint8)  # Mulai dengan 1 (pertahankan semua)
    y, x = np.ogrid[:rows, :cols]
    mask_distance = np.sqrt((x - ccol)**2 + (y - crow)**2)
    # Set 0 untuk band yang diremehkan (D1 <= distance <= D2)
    mask[(mask_distance >= D1) & (mask_distance <= D2)] = 0
    
    # Kalikan spectrum dengan mask
    fshift_filtered = fshift * mask
    
    # Inverse FFT
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)  # Ambil magnitude (real part dominan)
    
    # Crop padding dan normalize ke 0-255
    cropped = img_back[:h, :w] if h % 2 == 0 else img_back[1:h+1, :w]
    if w % 2 != 0:
        cropped = cropped[:, 1:w+1]
    normalized = cv2.normalize(cropped, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    
    return normalized

# Fungsi wrapper untuk 5x5 equivalent (D1=2, D2=5)
def bandstop(img):
    return ideal_bandstop_filter(img, D1=2, D2=5)
