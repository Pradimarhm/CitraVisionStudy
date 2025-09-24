from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtCore import pyqtSignal

class ImageProcessing(QMenu):
    histogramRequested = pyqtSignal()
    fuzzyRgbRequested = pyqtSignal()
    fuzzyGrayRequested = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__("Image Processing", parent)
        
        self.histogram_menu = QAction("Histogram Equlization", self)
        self.histogram_menu.triggered.connect(self.on_button_histogram_click)
        # self.addAction(self.btn_load)
        
        self.fuzzy_rgb_menu = QAction("Fuzzy Ke RGB", self)
        self.fuzzy_rgb_menu.triggered.connect(self.on_button_fuzzy_rgb_click)
        
        self.fuzzy_grayscale_menu = QAction("Fuzzy Grayscale", self)
        self.fuzzy_grayscale_menu.triggered.connect(self.on_button_fuzzy_gray_click)
        
        # histogram_menu = QAction("Histogram Equlization", self)
        # fuzzy_rgb_menu = QAction("Fuzzy He RGB", self)
        # fuzzy_grayscale_menu = QAction("Fuzzy Grayscale", self)
        
        self.addAction(self.histogram_menu)
        self.addAction(self.fuzzy_rgb_menu)
        self.addAction(self.fuzzy_grayscale_menu)
        
    def on_button_histogram_click(self):
        self.histogramRequested.emit()
    
    def on_button_fuzzy_rgb_click(self):
        self.fuzzyRgbRequested.emit()
    
    def on_button_fuzzy_gray_click(self):
        self.fuzzyGrayRequested.emit()