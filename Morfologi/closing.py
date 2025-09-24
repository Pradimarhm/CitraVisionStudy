import cv2

def closing_image(img, kernel):
    """
    Lakukan penutupan standar (dilatasi + erosi).
    img: Gambar biner.
    kernel: Structuring element.
    """
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)