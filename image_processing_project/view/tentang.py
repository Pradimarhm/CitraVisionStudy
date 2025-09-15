from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QDialog, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
# import sys

class TentangDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tentang Aplikasi")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ini adalah hasil dari tugas atau project aplikasi \npemrosesan citra. Dibuat dengan PyQt5."))
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)