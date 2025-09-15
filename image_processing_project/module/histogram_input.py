from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure
import cv2
import matplotlib.pyplot as plt

class histogramWindow(QMainWindow):
    def __init__(self, image_path, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Histogram Input")
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
        self.plot_histogram(image_path)
        
    def plot_histogram(self, image_path):
        img = cv2.imread(image_path, cv2.IMREAD_COLOR_RGB)
        
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.hist(img.ravel(), bins=256, range=[0,256], color='blue')
        ax.set_title('Histogram Input')
        ax.set_xlabel('Intensitas')
        ax.set_ylabel('Frekuensi')
        
        self.figure.tight_layout()
        self.canvas.draw()