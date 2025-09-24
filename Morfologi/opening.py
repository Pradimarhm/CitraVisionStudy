import cv2

def opening_image(img, kernel):
    """
    Lakukan pembukaan standar (erosi + dilatasi).
    img: Gambar biner.
    kernel: Structuring element.
    """
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

def refine_object(obj_img, kernel_main, kernel_ellipse, iterations=2):
    """
    Penyempurnaan objek hingga tidak seperti semula (opening + closing berulang dengan kernel berbeda).
    Menggunakan opening sebagai basis, lalu closing (impor dari closing.py jika diperlukan).
    Kembalikan gambar yang disempurnakan.
    """
    # Mulai dengan opening untuk bersihkan noise
    opened = opening_image(obj_img, kernel_main)
    # Closing berulang dengan elips untuk smoothing drastis
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel_ellipse, iterations=iterations)
    # Opening lagi untuk rapikan
    refined = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel_ellipse, iterations=iterations)
    return refined