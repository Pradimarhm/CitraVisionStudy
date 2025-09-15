from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure
from PyQt5.QtGui import QImage

import cv2
import matplotlib.pyplot as plt
import numpy as np

class histogramWindow_output(QMainWindow):
    def __init__(self, label_after, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Histogram Output")
        self.setGeometry(100, 100, 600, 400)
        
        # QWidget untuk central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Layoout
        layout = QVBoxLayout(central_widget)
        # self.setLayout(layout)
        
        # figure mathplotib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        
        # Tambah toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        # susun ke layout
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        
        # tampilan histogram
        self.plot_histogram(label_after)
        
    def plot_histogram(self, label_after):
        # img = cv2.imread(image_path, cv2.IMREAD_COLOR_RGB)
        pixmap = label_after.pixmap()
        if pixmap is None:
            print("Label tidak memiliki gambar.")
            return
        
        # Konversi QPixmap -> QImage
        qimg = pixmap.toImage()
        qimg = qimg.convertToFormat(QImage.Format.Format_RGB888)
        
        # Konversi QImage -> numpy array
        width = qimg.width()
        height = qimg.height()
        ptr = qimg.bits()
        ptr.setsize(height * width * 3)  # RGB888 -> 3 channel
        img = np.array(ptr).reshape(height, width, 3)  # shape (H, W, 3)
        
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.hist(img.ravel(), bins=256, range=[0,256], color='blue')
        ax.set_title('Histogram Output')
        ax.set_xlabel('Intensitas')
        ax.set_ylabel('Frekuensi')
        
        self.figure.tight_layout()
        self.canvas.draw()