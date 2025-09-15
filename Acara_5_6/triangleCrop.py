from PIL import Image, ImageDraw

def crop_triangle(image_path, output):
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
    
     # koordinat segitiga sama sisi
    triangle = [
        (size // 2, 0),         # titik atas
        (0, size),              # kiri bawah
        (size, size)            # kanan bawah
    ]
    draw.polygon(triangle, fill=255)
    
    # tempel gambar ke mask
    result = Image.new("RGBA", (size, size))
    result.paste(img_cropped, (0,0), mask)
    
    # simpan hasil
    result.save(output)
    
crop_triangle('Acara_5_6/img/Letmi.jpg', 'Acara_5_6/img/output/trinagle_cropped_image.png')