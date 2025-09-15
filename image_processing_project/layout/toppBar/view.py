from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtCore import pyqtSignal

class View(QMenu):
    showHistogramRequested = pyqtSignal()
    showHistogramOutputRequested = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__("View", parent)
        
        histogram = QMenu("Histogram", self)
        self.btn_histogram_input = QAction("Input", self)
        self.btn_histogram_input.triggered.connect(self.on_histogram_click)
        histogram.addAction(self.btn_histogram_input)
        
        self.btn_histogram_output = QAction("Output", self)
        self.btn_histogram_output.triggered.connect(self.on_histogram_output_click)
        histogram.addAction(self.btn_histogram_output)
        
        self.addMenu(histogram)
        
    def on_histogram_click(self):
        self.showHistogramRequested.emit()
    
    def on_histogram_output_click(self):
        self.showHistogramOutputRequested.emit()
