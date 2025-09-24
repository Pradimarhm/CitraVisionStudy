from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtCore import pyqtSignal

class Filter(QMenu):
    identifyRequested = pyqtSignal()
    
    edge1Requested = pyqtSignal()
    edge2Requested = pyqtSignal()
    edge3Requested = pyqtSignal()
    
    sharpenRequested = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__("Filter", parent)
        
        # identify_menu = QAction("Identify", self)
        self.identify_menu = QAction("Identify", self)
        self.identify_menu.triggered.connect(self.identify_menu_click)
        
        edge_detection_menu = QMenu("Edge Detection", self)
        # for i in range(1, 4):
        #     edge_detection_menu.addAction(QAction(f"Edge Detection {i}", self))
        self.edge_1 = QAction("Edge Detection 1", self)
        self.edge_1.triggered.connect(self.edge1_menu_click)
        edge_detection_menu.addAction(self.edge_1)
        
        self.edge_2 = QAction("Edge Detection 2", self)
        self.edge_2.triggered.connect(self.edge2_menu_click)
        edge_detection_menu.addAction(self.edge_2)
        
        self.edge_3 = QAction("Edge Detection 3", self)
        self.edge_3.triggered.connect(self.edge3_menu_click)
        edge_detection_menu.addAction(self.edge_3)
        
        self.sharpen_menu = QAction("Sharpen",self)
        self.sharpen_menu.triggered.connect(self.sharpen_menu_clicked)
        
        gausian_blur_menu = QMenu("Gausian Blur", self)
        gausian_blur_menu.addAction(QAction("Gausian Blur 3x3", self))
        gausian_blur_menu.addAction(QAction("Gausian Blur 5x5", self))
        
        unshap_masking_menu = QAction("Unshap Masking", self)
        average_filter_menu = QAction("Average Filter", self)
        lowpass_filter_menu = QAction("Low Pass Filter", self)
        highpass_filter_menu = QAction("High Pass Filter", self)
        bandstop_filter_menu = QAction("Bandstop Filter", self)
        
        self.addAction(self.identify_menu)
        self.addMenu(edge_detection_menu)
        self.addAction(self.sharpen_menu)
        self.addMenu(gausian_blur_menu)
        self.addAction(unshap_masking_menu)
        self.addAction(average_filter_menu)
        self.addAction(lowpass_filter_menu)
        self.addAction(highpass_filter_menu)
        self.addAction(bandstop_filter_menu)
        
    def identify_menu_click(self):
        self.identifyRequested.emit()
    
    # edge
    def edge1_menu_click(self):
        self.edge1Requested.emit()
        
    def edge2_menu_click(self):
        self.edge2Requested.emit()
        
    def edge3_menu_click(self):
        self.edge3Requested.emit()
    
    def sharpen_menu_clicked(self):
        self.sharpenRequested.emit()