from PIL import Image, ImageTk, ImageEnhance

def to_grayscale(img):
    return img.convert("L")  # L = grayscale