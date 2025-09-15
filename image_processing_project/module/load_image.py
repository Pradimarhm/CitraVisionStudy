import cv2
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

class ImageLoader:
    def __init__(self, label_before: QWidget, label_after: QWidget = None):
        self.label_before = label_before
        self.label_after = label_after
        self.file_path = None
        self.cv_gray = None

    def load(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Pilih Gambar", "", "Image Files (*.jpeg *.jpg *.png *.bmp)"
        )
        if not file_path:
            return
        
        self.file_path = file_path
        
        # Baca dengan OpenCV
        cv_image = cv2.imread(file_path)
        cv_image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        self.cv_gray = cv2.cvtColor(cv_image_rgb, cv2.COLOR_RGB2GRAY)

        # Convert ke QPixmap
        h, w, ch = cv_image_rgb.shape
        bytes_per_line = ch * w
        qimg = QImage(cv_image_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)

        # Tampilkan ke label_before
        self.label_before.setPixmap(
            QPixmap.fromImage(qimg).scaled(
                self.label_before.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )

        # # Kalau ada label_after → tampilkan grayscale juga
        if self.label_after is not None:
            h, w = self.cv_gray.shape
            bytes_per_line = w
            qimg_gray = QImage(self.cv_gray.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
            self.label_after.setPixmap(
                QPixmap.fromImage(qimg_gray).scaled(
                    self.label_after.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
            )
