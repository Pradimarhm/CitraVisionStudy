# import cv2
# import numpy as np
# from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
# from PyQt5.QtGui import QImage, QPixmap

# class HistogramEqualizer(QWidget):
    
    
#     def __init__(self, label_before, label_after):
#         super().__init__()
#         self.label_before = label_before
#         self.label_after = label_after
#         self.setup_ui()

#     def setup_ui(self):
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel("Histogram Equalization"))
#         btn = QPushButton("Apply Equalization")
#         btn.clicked.connect(self.apply_equalization)
#         layout.addWidget(btn)
#         self.setLayout(layout)

#     def qpixmap_to_numpy(self, pixmap: QPixmap):
#         """Konversi QPixmap ke numpy array RGB aman."""
#         if pixmap is None:
#             return None

#         qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
#         w, h = qimg.width(), qimg.height()
#         bytes_per_line = qimg.bytesPerLine()
#         ptr = qimg.bits()
#         ptr.setsize(qimg.byteCount())
#         # gunakan bytesPerLine supaya tidak error reshape
#         arr = np.frombuffer(ptr, np.uint8).reshape((h, bytes_per_line))
#         arr = arr[:, :w * 3].reshape((h, w, 3))
#         return arr

#     def numpy_to_qpixmap(self, arr: np.ndarray):
#         h, w, ch = arr.shape
#         bytes_per_line = ch * w
#         qimg = QImage(arr.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         return QPixmap.fromImage(qimg)

#     def apply_equalization(self):
#         pix = self.label_before.pixmap()
#         if pix is None:
#             return

#         img_rgb = self.qpixmap_to_numpy(pix)
#         # ubah ke grayscale
#         gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
#         # histogram equalization
#         eq = cv2.equalizeHist(gray)
#         # kembali ke RGB supaya bisa ditampilkan di QLabel
#         eq_rgb = cv2.cvtColor(eq, cv2.COLOR_GRAY2RGB)

#         self.label_after.setPixmap(self.numpy_to_qpixmap(eq_rgb))
