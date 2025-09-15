from PIL import Image, ImageOps

#load image
image_path = 'Acara_5_6/img/6b75c7b1-1c2a-435a-8f88-6ebb804e7c77.jpg'
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
    
    # perkecil gambar
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)
    small_image = image.resize((new_width, new_height))
    
    # bikin canvas kosong dengan ukuran asli (RGBA biar transparan)
    result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    
    # hitung posisi supaya small_image ada di tengah
    left = (width - new_width) // 2
    top = (height - new_height) // 2
    
    # tempelkan gambar kecil ke canvas
    result.paste(small_image, (left, top))
    
    return result

# Contoh Penggunaan:
# Translasi gambar sejauh 50 piksel ke kanan dan
translated = translate_image(image, -90, -30)

# Rotasi gambar sebesar 90 derajat
rotated = rotate_image(image, 45)

# Flipping gambar secara horizontal
flipped_horizontal = flip_image(image, 'vertical')

# Zooming gambar dengan faktor s
zoomed = zoom_image(image, 0.5)

# Menyimpan hasil transformasi
translated.save('Acara_5_6/img/output/c/translated_image.jpg')
rotated.save('Acara_5_6/img/output/c/rotated_image.jpg')
flipped_horizontal.save('Acara_5_6/img/output/c/flipped_horizontal_image.jpg')
zoomed.save('Acara_5_6/img/output/c/zoomed_image.png')