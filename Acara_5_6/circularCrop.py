from PIL import Image, ImageDraw

def crop_circle(image_path, output):
    # buka gambar
    img = Image.open(image_path).convert("RGBA")
    
    # ambil ukuran terkecil dari gambar
    size = min(img.size)
    
    # rezise gambar asli
    left = (img.width - size) // 2
    top = (img.height - size) // 2
    right = left + size
    bottom = top + size
    img_cropped = img.crop((left, top, right, bottom))
    
    # buat lingkaran
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0,0, size, size), fill=255)
    
    # tempel gambar ke mask
    result = Image.new("RGBA", (size, size))
    result.paste(img_cropped, (0,0), mask)
    
    # simpan hasil
    result.save(output)
    
crop_circle('Acara_5_6/img/perguruaninggi.jpg', 'Acara_5_6/img/output/circular_cropped_image.png')