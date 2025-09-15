import tkinter as tk
from tkinter import Menu, filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance
import cv2

# improt file
from imageProcess import grayscale
from imageProcess import brightness
import filemanager


# Variabel global
img_path = None
img_original = None
img_display = None
panel = None

# Fungsi buka gambar
def do_open_image():
    global img_original, img_display
    img = filemanager.open_image()
    if img:
        img_original = img
        img_display = img_original
        show_image(img_display)

# fungsi save image
# def do_save_image():
    

# Tampilkan gambar ke panel Tkinter
def show_image(img):
    global panel
    # Batas ukuran tampilan
    max_width, max_height = 400, 300

    # Ambil ukuran asli
    w, h = img.size
    ratio = min(max_width / w, max_height / h)
    new_w, new_h = int(w * ratio), int(h * ratio)

    # Resize dengan rasio yang benar
    img_resized = img.resize((new_w, new_h))
    tk_img = ImageTk.PhotoImage(img_resized)

    if panel is None:
        panel = tk.Label(root, image=tk_img)
        panel.image = tk_img
        # panel.pack(side="right", padx=10, pady=10)
        panel.place(relx=0.5, rely=0.5, anchor="center")
    else:
        panel.configure(image=tk_img)
        panel.image = tk_img

# Convert ke grayscale
def rgb_to_gray():
    global img_display
    if img_original:
        img_display = grayscale.to_grayscale(img_original)
        show_image(img_display)
    else:
        messagebox.showerror("Error", "Buka gambar dulu!")

# Adjust brightness
def do_brightness():
    global img_display
    if img_original:
        img_display = brightness.adjust_brightness(img_original)
        show_image(img_display)
    else:
        messagebox.showerror("Error", "Buka gambar dulu!")

# Main window
root = tk.Tk()
root.title("Image Processing App")
root.geometry("800x500")

# Menu bar
menubar = Menu(root)

# File menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=do_open_image)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Colors menu
colors_menu = Menu(menubar, tearoff=0)
colors_menu.add_command(label="RGB to Grayscale", command=rgb_to_gray)
colors_menu.add_command(label="Brightness", command=do_brightness)
menubar.add_cascade(label="Image Processing", menu=colors_menu)

root.config(menu=menubar)
root.mainloop()

# # Colors menu
# colors_menu = Menu(menubar, tearoff=0)
# colors_menu.add_command(label="RGB to Grayscale", command=rgb_to_gray)
# colors_menu.add_command(label="Brightness", command=brightness)
# colors_menu.add_command(label="Contrast")
# colors_menu.add_command(label="Brightness - Contrast")
# colors_menu.add_command(label="Inverse")
# colors_menu.add_command(label="Log Brightness")
# colors_menu.add_command(label="Bit Depth")
# colors_menu.add_command(label="Gamma Correction")

# menubar.add_cascade(label="Colors", menu=colors_menu)

# # Add other menus (File, View, etc.)
# menubar.add_cascade(label="File")
# menubar.add_cascade(label="View")
# menubar.add_cascade(label="Image Processing")
# menubar.add_cascade(label="Arithmetical Operation")
# menubar.add_cascade(label="Filter")
# menubar.add_cascade(label="Edge Detection")
# menubar.add_cascade(label="Morfologi")

# root.config(menu=menubar)
# root.mainloop()
