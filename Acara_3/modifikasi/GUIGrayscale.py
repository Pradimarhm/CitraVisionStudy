# import cv2

# image = cv2.imread('Acara_3/img/daun.jpeg')
# imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# filename1 = 'Acara_3/img/output/daun_gray.jpeg'
# cv2.imwrite(filename1, imgGray)
# cv2.waitKey(0)

import sys
import cv2
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import qdarkstyle

class GrayConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image to Grayscale Converter")
        self.setGeometry(200, 200, 800, 400)

        # Variabel
        self.file_path = None
        self.cv_gray = None

        # Label untuk gambar
        self.label_before = QLabel("Original Image")
        self.label_after = QLabel("Grayscale Image")

        self.label_before.setAlignment(Qt.AlignCenter)
        self.label_after.setAlignment(Qt.AlignCenter)

        # Tombol
        self.btn_import = QPushButton("Pilih Gambar")
        self.btn_import.setStyleSheet("padding: 10px 20px;")
        
        self.btn_save = QPushButton("Simpan Hasil")
        self.btn_save.setStyleSheet("padding: 10px 20px;")
        self.btn_save.setEnabled(False)  # disable sebelum ada gambar

        # Layout tombol
        buttonbox = QHBoxLayout()
        buttonbox.addWidget(self.btn_import)
        buttonbox.addWidget(self.btn_save)

        # Layout gambar
        img_layout = QHBoxLayout()
        img_layout.addWidget(self.label_before)
        img_layout.addWidget(self.label_after)

        # Layout utama
        mainbox = QVBoxLayout()
        mainbox.addLayout(img_layout)
        mainbox.addLayout(buttonbox)

        self.setLayout(mainbox)

        # Event handler
        self.btn_import.clicked.connect(self.load_image)
        self.btn_save.clicked.connect(self.save_image)

    def load_image(self):
        # Pilih file gambar
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Pilih Gambar", "", "Image Files (*.jpg *.jpeg *.png *.bmp)"
        )
        if not file_path:
            return

        self.file_path = file_path

        # Baca gambar dengan OpenCV
        cv_img = cv2.imread(file_path)
        cv_img_rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        self.cv_gray = cv2.cvtColor(cv_img_rgb, cv2.COLOR_RGB2GRAY)

        # Tampilkan original
        h, w, ch = cv_img_rgb.shape
        bytes_per_line = ch * w
        qimg = QImage(cv_img_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.label_before.setPixmap(QPixmap.fromImage(qimg).scaled(350, 350, Qt.KeepAspectRatio))

        # Tampilkan grayscale
        h, w = self.cv_gray.shape
        qimg_gray = QImage(self.cv_gray.data, w, h, w, QImage.Format_Grayscale8)
        self.label_after.setPixmap(QPixmap.fromImage(qimg_gray).scaled(350, 350, Qt.KeepAspectRatio))

        # Aktifkan tombol save
        self.btn_save.setEnabled(True)

    def save_image(self):
        if self.cv_gray is None:
            return

        # Tentukan nama file output
        folder, name = os.path.split(self.file_path)
        output_path = os.path.join(folder, "gray_" + name)

        cv2.imwrite(output_path, self.cv_gray)
        QMessageBox.information(self, "Berhasil", f"Gambar grayscale disimpan di:\n{output_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    
    window = GrayConverter()
    window.show()
    sys.exit(app.exec_())

