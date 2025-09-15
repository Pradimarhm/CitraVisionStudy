import cv2
from matplotlib import pyplot as plt

#fungsi untuk menampilkan histogram citra
def view_histogram_citra(image_path):
    #membaca citra dari path 
    image = cv2.imread(image_path)
    
    #konversi citra dari BGR (format default cv2) ke RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    #memisahkan kanal warna
    chanels = ('r', 'g', 'b')
    colors = ('red', 'green', 'blue')
    
    plt.figure(figsize=(10,5))
    
    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)
        plt.xlim(0, 256)
    
    plt.title('Histogram untuk setiap kanal warna')
    plt.xlabel('Intensitas Pixel')
    plt.ylabel('Jumlah Pixel')
    plt.show()
    
#path ke citra
path = 'image_processing_project/assets/img/download.jpg'

#menampilkan histogram
view_histogram_citra(path)