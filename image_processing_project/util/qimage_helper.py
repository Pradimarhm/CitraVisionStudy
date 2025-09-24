from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import numpy as np
import cv2

def qlabel_to_numpy(label):
    """Ambil gambar RGB numpy dari QLabel (pixmap)."""
    pixmap = label.pixmap()
    if pixmap is None:
        return None
    qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
    w, h = qimg.width(), qimg.height()
    ptr = qimg.bits()
    ptr.setsize(qimg.byteCount())
    arr = np.array(ptr, dtype=np.uint8).reshape((h, w, 3))
    return arr

def numpy_to_qlabel(arr, label):
    """Tampilkan numpy RGB/gray ke QLabel."""
    if arr.ndim == 2:  # grayscale
        arr = cv2.cvtColor(arr, cv2.COLOR_GRAY2RGB)
    h, w, ch = arr.shape
    bytes_per_line = ch * w
    qimg = QImage(arr.data, w, h, bytes_per_line, QImage.Format_RGB888)
    pix = QPixmap.fromImage(qimg)
    label.setPixmap(
        pix.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    )
