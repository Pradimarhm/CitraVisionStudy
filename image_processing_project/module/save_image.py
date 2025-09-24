import os
import cv2
from PyQt5.QtWidgets import (
    QMessageBox
)

from PyQt5.QtWidgets import QFileDialog, QWidget
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.QtCore import Qt

class ImageSave:
    def __init__(self, parent: QWidget, label_before: QWidget, label_after: QWidget = None):
        # Variabel
        self.parent = parent  # biar bisa pakai QMessageBox dengan parent window
        self.label_before = label_before
        self.label_after = label_after
        self.file_path = None
    
    def save_image(self):
        if self.label_after and self.label_after.pixmap() and not self.label_after.pixmap().isNull():
            pixmap = self.label_after.pixmap()
            print(">> Menyimpan gambar hasil edit...")
        elif self.label_before and self.label_before.pixmap():
            pixmap = self.label_before.pixmap()
            print(">> Menyimpan gambar asli...")
        else:
            QMessageBox.warning(self.parent, "Peringatan", "Tidak ada gambar yang bisa disimpan.")
            return

        save_path, _ = QFileDialog.getSaveFileName(self.parent, "Simpan Gambar", "", "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg)")
        if not save_path:
            return  # user batal

        if pixmap.save(save_path):
            QMessageBox.information(self.parent, "Berhasil", f"Gambar berhasil disimpan:\n{save_path}")
        else:
            QMessageBox.critical(self.parent, "Error", "Gagal menyimpan gambar.")
