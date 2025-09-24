import cv2

def erode_image(img, kernel, iterations=1):
    """
    Lakukan erosi standar.
    img: Gambar biner.
    kernel: Structuring element.
    iterations: Jumlah iterasi (default 1-2 untuk kontraksi sedang).
    """
    return cv2.erode(img, kernel, iterations=iterations)