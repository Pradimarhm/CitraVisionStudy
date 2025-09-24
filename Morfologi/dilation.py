import cv2

def dilate_image(img, kernel, iterations=1):
    """
    Lakukan dilatasi standar.
    img: Gambar biner.
    kernel: Structuring element.
    iterations: Jumlah iterasi (default 1-2 untuk efek sedang).
    """
    return cv2.dilate(img, kernel, iterations=iterations)

def expand_text_area(text_img, kernel, target_multiplier=2, max_iterations=10):
    """
    Perluas area tulisan hingga ~target_multiplier x lipat dari asli menggunakan dilatasi dinamis.
    Kembalikan gambar yang diperluas dan jumlah iterations.
    """
    original_area = cv2.countNonZero(text_img)
    target_area = original_area * target_multiplier
    expanded = text_img.copy()
    iterations = 0
    while cv2.countNonZero(expanded) < target_area and iterations < max_iterations:
        expanded = cv2.dilate(expanded, kernel, iterations=1)
        iterations += 1
    return expanded, iterations