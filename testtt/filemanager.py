from tkinter import filedialog, messagebox
from PIL import Image

def open_image():
    path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp ")]
    )
    if path:
        return Image.open(path)
    return None

def save_image(img):
    if img:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("BMP files", "*.bmp")]
        )
        if file_path:
            img.save(file_path)
            messagebox.showinfo("Success", f"Gambar berhasil disimpan ke:\n{file_path}")
    else:
        messagebox.showerror("Error", "Tidak ada gambar untuk disimpan!")
