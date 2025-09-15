from PIL import Image, ImageOps

#load image
image_path = 'Acara_5_6/img/download.jpg'
image = Image.open(image_path)

def translate_image(image, x_shift, y_shift):
    Width, height, = image.size
    translation_matrix = (1, 0, x_shift, 0, 1, y_shift)
    translated_image = image.transform((Width, height), Image.AFFINE, translation_matrix)
    return translated_image

# 2. Rotasi (Rotation)
def rotate_image(image, angle):
    rotated_image = image.rotate (angle, expand=True)
    return rotated_image

# 3. Flipping (Refleksi)
def flip_image(image, mode='horizontal'):
    if mode == 'horizontal':
        flipped_image = ImageOps.mirror(image)
    elif mode == 'vertical':
        flipped_image = ImageOps.flip(image)
    return flipped_image

# 4. Zooming (Scaling)
def zoom_image(image, zoom_factor):
    width, height = image.size
    zoomed_image = image.resize((int(width * zoom_factor), int (height * zoom_factor)))
    # ambil bagian tengah dengan ukuran asli
    left = (zoomed_image.width - width) // 2
    top = (zoomed_image.height - height) // 2
    right = left + width
    bottom = top + height
    return zoomed_image.crop((left, top, right, bottom))
    # return zoomed_image

# Contoh Penggunaan:
# Translasi gambar sejauh 50 piksel ke kanan dan
translated = translate_image(image, 50, 30)

# Rotasi gambar sebesar 90 derajat
rotated = rotate_image(image, 90)

# Flipping gambar secara horizontal
flipped_horizontal = flip_image(image, 'horizontal')

# Zooming gambar dengan faktor s
zoomed = zoom_image(image, 1.5)

# Menyimpan hasil transformasi
translated.save('Acara_5_6/img/output/translated_image.jpg')
rotated.save('Acara_5_6/img/output/rotated_image.jpg')
flipped_horizontal.save('Acara_5_6/img/output/flipped_horizontal_image.jpg')
zoomed.save('Acara_5_6/img/output/zoomed_image.jpg')