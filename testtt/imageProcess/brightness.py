from PIL import Image, ImageTk, ImageEnhance

def adjust_brightness(img):
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(1.5)