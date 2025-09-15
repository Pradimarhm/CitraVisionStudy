from PyQt5.QtWidgets import QMenu, QAction

class ImageProcessing(QMenu):
    def __init__(self, parent=None):
        super().__init__("Image Processing", parent)
        
        histogram_menu = QAction("Histogram Equlization", self)
        fuzzy_rgb_menu = QAction("Fuzzy He RGB", self)
        fuzzy_grayscale_menu = QAction("Fuzzy Grayscale", self)
        
        self.addAction(histogram_menu)
        self.addAction(fuzzy_rgb_menu)
        self.addAction(fuzzy_grayscale_menu)