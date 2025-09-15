from PIL import Image

def clipping(intensitas):
    if intensitas < 0:
        return 0
    if intensitas > 255:
        return 255
    return intensitas

def atur_pencerahan(nilai_pencerahan, nama_setelah_disave):
    citra = Image.open('Acara_3/img/daun.jpeg')
    pixels = citra.load()
    
    ukuran_horizontal = citra.size[0]
    ukuran_vertikal = citra.size[1]
    
    for x in range(ukuran_horizontal):
        for y in range(ukuran_vertikal):
            R = clipping(pixels[x,y][0]+nilai_pencerahan)
            G = clipping(pixels[x,y][1]+nilai_pencerahan)
            B = clipping(pixels[x,y][2]+nilai_pencerahan)
            pixels[x,y] = (R, G, B)
    
    citra.save(nama_setelah_disave)
    
atur_pencerahan(80, 'Acara_3/img/output/daun_clipping.jpeg')