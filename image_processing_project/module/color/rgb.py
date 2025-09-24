import os
import cv2
import numpy as np

from PyQt5.QtWidgets import (
    QMessageBox
)

from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

class yellow_filter:
    def __init__(self, label_before: QWidget, label_after: QWidget = None):
        # self.parent = parent
        self.label_before = label_before
        self.label_after = label_after
        self.file_path = None
        # self.image = None
        
    def yellow(self):
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

        # ubah ke BGR agar sama dengan OpenCV
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # filter kuning
        yellow_layer = np.full_like(img_bgr, (0, 255, 255))
        result = cv2.addWeighted(img_bgr, 0.5, yellow_layer, 0.5, 0)

        # tampilkan ke label_after
        self._display(result, self.label_after)

    def _display(self, img, label):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qimg = QImage(cv2.cvtColor(img, cv2.COLOR_BGR2RGB).data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(
            QPixmap.fromImage(qimg).scaled(
                label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )
        

class orange_filter:
    def __init__(self, label_before: QWidget, label_after: QWidget = None):
        # self.parent = parent
        self.label_before = label_before
        self.label_after = label_after
        self.file_path = None
        # self.image = None
        
    def orange(self):
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

        # ubah ke BGR agar sama dengan OpenCV
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # filter 
        orange_layer = np.full_like(img_bgr, (0, 165, 255))
        result = cv2.addWeighted(img_bgr, 0.5, orange_layer, 0.5, 0)

        # tampilkan ke label_after
        self._display(result, self.label_after)

    def _display(self, img, label):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qimg = QImage(cv2.cvtColor(img, cv2.COLOR_BGR2RGB).data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(
            QPixmap.fromImage(qimg).scaled(
                label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )

class cyan_filter:
    def __init__(self, label_before: QWidget, label_after: QWidget = None):
        # self.parent = parent
        self.label_before = label_before
        self.label_after = label_after
        self.file_path = None
        # self.image = None
        
    def cyan(self):
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

        # ubah ke BGR agar sama dengan OpenCV
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # filter 
        layer = np.full_like(img_bgr, (255, 255, 0))
        result = cv2.addWeighted(img_bgr, 0.5, layer, 0.5, 0)

        # tampilkan ke label_after
        self._display(result, self.label_after)

    def _display(self, img, label):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qimg = QImage(cv2.cvtColor(img, cv2.COLOR_BGR2RGB).data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(
            QPixmap.fromImage(qimg).scaled(
                label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )
        
class ungu_filter:
    def __init__(self, label_before: QWidget, label_after: QWidget = None):
        # self.parent = parent
        self.label_before = label_before
        self.label_after = label_after
        self.file_path = None
        # self.image = None
        
    def ungu(self):
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

        # ubah ke BGR agar sama dengan OpenCV
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # filter 
        layer = np.full_like(img_bgr, (255, 0, 255))
        result = cv2.addWeighted(img_bgr, 0.5, layer, 0.5, 0)

        # tampilkan ke label_after
        self._display(result, self.label_after)

    def _display(self, img, label):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qimg = QImage(cv2.cvtColor(img, cv2.COLOR_BGR2RGB).data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(
            QPixmap.fromImage(qimg).scaled(
                label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )
        
class abu_filter:
    def __init__(self, label_before: QWidget, label_after: QWidget = None):
        # self.parent = parent
        self.label_before = label_before
        self.label_after = label_after
        self.file_path = None
        # self.image = None
        
    def abu(self):
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

        # ubah ke BGR agar sama dengan OpenCV
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # filter 
        layer = np.full_like(img_bgr, (128,128,128))
        result = cv2.addWeighted(img_bgr, 0.5, layer, 0.5, 0)

        # tampilkan ke label_after
        self._display(result, self.label_after)

    def _display(self, img, label):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qimg = QImage(cv2.cvtColor(img, cv2.COLOR_BGR2RGB).data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(
            QPixmap.fromImage(qimg).scaled(
                label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )
        
class coklat_filter:
    def __init__(self, label_before: QWidget, label_after: QWidget = None):
        # self.parent = parent
        self.label_before = label_before
        self.label_after = label_after
        self.file_path = None
        # self.image = None
        
    def coklat(self):
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

        # ubah ke BGR agar sama dengan OpenCV
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # filter 
        layer = np.full_like(img_bgr, (42, 42, 165))
        result = cv2.addWeighted(img_bgr, 0.5, layer, 0.5, 0)

        # tampilkan ke label_after
        self._display(result, self.label_after)

    def _display(self, img, label):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qimg = QImage(cv2.cvtColor(img, cv2.COLOR_BGR2RGB).data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(
            QPixmap.fromImage(qimg).scaled(
                label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )
        
class merah_filter:
    def __init__(self, label_before: QWidget, label_after: QWidget = None):
        # self.parent = parent
        self.label_before = label_before
        self.label_after = label_after
        self.file_path = None
        # self.image = None
        
    def merah(self):
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

        # ubah ke BGR agar sama dengan OpenCV
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # filter 
        layer = np.full_like(img_bgr, (0, 0, 255))
        result = cv2.addWeighted(img_bgr, 0.5, layer, 0.5, 0)

        # tampilkan ke label_after
        self._display(result, self.label_after)

    def _display(self, img, label):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qimg = QImage(cv2.cvtColor(img, cv2.COLOR_BGR2RGB).data, w, h, bytes_per_line, QImage.Format_RGB888)
        label.setPixmap(
            QPixmap.fromImage(qimg).scaled(
                label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )