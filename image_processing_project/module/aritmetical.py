# module/aritmetical.py
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
    QPushButton, QComboBox, QStatusBar
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2, numpy as np


class AritmeticalWindow(QDialog):
    """
    Menampilkan 3 kotak gambar:
      - Input 1 : otomatis ambil dari label_before (MainWindow)
      - Input 2 : otomatis ambil dari label_after  (MainWindow)
      - Output  : hasil operasi aritmetika
    """
    def __init__(self, label_before_main: QLabel, label_after_main: QLabel, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Aritmetical Operation")
        self.resize(1000, 500)

        # referensi label dari MainWindow
        self.main_before = label_before_main
        self.main_after  = label_after_main

        # ===== Layout utama =====
        main_layout = QVBoxLayout(self)
        hbox = QHBoxLayout()

        # Frame Input 1
        self.frame_in1 = self.create_frame("Input 1 (Before)")
        self.label_in1 = self.frame_in1.findChild(QLabel, "img_label")
        hbox.addWidget(self.frame_in1)

        # Frame Input 2
        self.frame_in2 = self.create_frame("Input 2 (After)")
        self.label_in2 = self.frame_in2.findChild(QLabel, "img_label")
        hbox.addWidget(self.frame_in2)

        # Frame Output
        self.frame_out = self.create_frame("Output")
        self.label_out = self.frame_out.findChild(QLabel, "img_label")
        hbox.addWidget(self.frame_out)

        main_layout.addLayout(hbox)

        # Combo operasi + tombol proses
        self.combo = QComboBox()
        self.combo.addItems(["Add", "Subtract", "Multiply", "Divide"])
        btn = QPushButton("Process")
        btn.clicked.connect(self.process_operation)

        main_layout.addWidget(self.combo)
        main_layout.addWidget(btn)

        # Status bar
        self.status = QStatusBar()
        main_layout.addWidget(self.status)

        # langsung tampilkan gambar awal
        self.refresh_inputs()

    # ------------------------------------------------------------------
    def create_frame(self, title: str) -> QFrame:
        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        layout = QVBoxLayout(frame)

        lbl_title = QLabel(title, alignment=Qt.AlignCenter)
        img_label = QLabel(objectName="img_label")
        img_label.setFixedSize(300, 300)
        img_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(lbl_title)
        layout.addWidget(img_label, alignment=Qt.AlignCenter)
        return frame

    def refresh_inputs(self):
        """Tampilkan ulang gambar input dari MainWindow."""
        if self.main_before.pixmap():
            self.label_in1.setPixmap(self.main_before.pixmap())
        if self.main_after.pixmap():
            self.label_in2.setPixmap(self.main_after.pixmap())

    def qpixmap_to_numpy(self, pixmap: QPixmap) -> np.ndarray:
        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())

        stride = qimg.bytesPerLine()  # jumlah byte per baris termasuk padding
        arr = np.frombuffer(ptr, np.uint8).reshape((h, stride))
        arr = arr[:, : w * 3]         # buang padding di tiap baris
        arr = arr.reshape((h, w, 3))  # sekarang ukurannya pas
        return cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)



    def show_image(self, label: QLabel, img: np.ndarray):
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
        pix = QPixmap.fromImage(qimg).scaled(
            label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        label.setPixmap(pix)

    def process_operation(self):
        # pastikan input ada
        pix1 = self.main_before.pixmap()
        pix2 = self.main_after.pixmap()
        if pix1 is None or pix2 is None:
            self.status.showMessage("Label input kosong.")
            return

        img1 = self.qpixmap_to_numpy(pix1)
        img2 = self.qpixmap_to_numpy(pix2)
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

        op = self.combo.currentText()
        if op == "Add":
            out = cv2.add(img1, img2)
        elif op == "Subtract":
            out = cv2.subtract(img1, img2)
        elif op == "Multiply":
            out = cv2.multiply(img1, img2)
        else:  # Divide
            out = cv2.divide(img1.astype(np.float32) + 1e-5,
                             img2.astype(np.float32) + 1e-5)
            out = np.clip(out, 0, 255).astype(np.uint8)

        self.show_image(self.label_out, out)
        self.status.showMessage(f"Operation {op} selesai.")
