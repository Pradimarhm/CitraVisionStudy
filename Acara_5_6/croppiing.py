from PIL import Image

#load image
image_path = 'Acara_5_6/img/Letmi.jpg'
image = Image.open(image_path)

#definisikan bounding box
left = 50
top = 50
right = 350
bottom = 250

# crop gamber
cropped_image = image.crop((left, top, right, bottom))

#simpan hasil cropping
cropped_image.save('Acara_5_6/img/output/cropped_image.jpg')