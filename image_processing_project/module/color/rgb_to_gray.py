import cv2
import numpy as np

from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

class rgbToGray:
    def __init__(self, label_before: QWidget, label_after: QWidget = None):
        self.label_before = label_before
        self.label_after = label_after
        self.file_path = None
        self.cv_gray = None

    def average(self):
        # ambil pixmap dari label
        pixmap = self.label_before.pixmap()
        if pixmap is None:
            return  # belum ada gambar di label

        # convert QPixmap -> QImage
        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()

        # QImage -> numpy array (RGB)
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        img_rgb = np.array(ptr, dtype=np.uint8).reshape(h, w, 3)
        
        # cv_image_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
        self.cv_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        # Jika ingin persis "average":
        b,g,r = cv2.split(img_rgb)
        self.gray_avg = ((r.astype(np.float32)+g+b)/3).astype(np.uint8)

        # # Kalau ada label_after → tampilkan grayscale juga
        if self.label_after is not None:
            h, w = self.gray_avg.shape
            bytes_per_line = w
            qimg_gray = QImage(self.gray_avg.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
            self.label_after.setPixmap(
                QPixmap.fromImage(qimg_gray).scaled(
                    self.label_after.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
            )
            
    def lightness(self):
        # ambil pixmap dari label
        pixmap = self.label_before.pixmap()
        if pixmap is None:
            return  # belum ada gambar di label

        # convert QPixmap -> QImage
        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()

        # QImage -> numpy array (RGB)
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        img_rgb = np.array(ptr, dtype=np.uint8).reshape(h, w, 3)
        
        # cv_image_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
        self.cv_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        # Jika ingin persis "average":
        b,g,r = cv2.split(img_rgb)
        maxc = np.maximum.reduce([r,g,b])
        minc = np.minimum.reduce([r,g,b])
        self.gray_light = ((maxc + minc) / 2).astype(np.uint8)

        # # Kalau ada label_after → tampilkan grayscale juga
        if self.label_after is not None:
            h, w = self.gray_light.shape
            bytes_per_line = w
            qimg_gray = QImage(self.gray_light.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
            self.label_after.setPixmap(
                QPixmap.fromImage(qimg_gray).scaled(
                    self.label_after.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
            )
    
    def luminance(self):
        # ambil pixmap dari label
        pixmap = self.label_before.pixmap()
        if pixmap is None:
            return  # belum ada gambar di label

        # convert QPixmap -> QImage
        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()

        # QImage -> numpy array (RGB)
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        img_rgb = np.array(ptr, dtype=np.uint8).reshape(h, w, 3)
        
        # cv_image_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
        self.cv_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        # Jika ingin persis "average":
        b,g,r = cv2.split(img_rgb)
        self.gray_lum = (0.299*r + 0.587*g + 0.114*b).astype(np.uint8)

        # # Kalau ada label_after → tampilkan grayscale juga
        if self.label_after is not None:
            h, w = self.gray_lum.shape
            bytes_per_line = w
            qimg_gray = QImage(self.gray_lum.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
            self.label_after.setPixmap(
                QPixmap.fromImage(qimg_gray).scaled(
                    self.label_after.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
            )
