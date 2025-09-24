from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QSlider, QSpinBox, QPushButton
)
from PyQt5.QtCore import Qt

class BrightnessContrastDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Brightness & Contrast")
        self.resize(400, 150)

        layout = QVBoxLayout(self)

        # ----- Brightness -----
        self.b_slider = QSlider(Qt.Horizontal)
        self.b_slider.setRange(-100, 100)
        self.b_spin = QSpinBox()
        self.b_spin.setRange(-100, 100)

        self.b_slider.valueChanged.connect(self.b_spin.setValue)
        self.b_spin.valueChanged.connect(self.b_slider.setValue)

        h_bright = QHBoxLayout()
        h_bright.addWidget(QLabel("Brightness"))
        h_bright.addWidget(self.b_slider)
        h_bright.addWidget(self.b_spin)
        layout.addLayout(h_bright)

        # ----- Contrast -----
        self.c_slider = QSlider(Qt.Horizontal)
        self.c_slider.setRange(-100, 100)
        self.c_spin = QSpinBox()
        self.c_spin.setRange(-100, 100)

        self.c_slider.valueChanged.connect(self.c_spin.setValue)
        self.c_spin.valueChanged.connect(self.c_slider.setValue)

        h_contrast = QHBoxLayout()
        h_contrast.addWidget(QLabel("Contrast"))
        h_contrast.addWidget(self.c_slider)
        h_contrast.addWidget(self.c_spin)
        layout.addLayout(h_contrast)

        # OK button
        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(self.accept)
        layout.addWidget(ok_btn)

    def get_values(self):
        return self.b_slider.value(), self.c_slider.value()
