from PyQt5.QtWidgets import QMenu, QAction

class Filter(QMenu):
    def __init__(self, parent=None):
        super().__init__("Filter", parent)
        
        identify_menu = QAction("Identify", self)
        
        edge_detection_menu = QMenu("Edge Detection", self)
        for i in range(1, 4):
            edge_detection_menu.addAction(QAction(f"Edge Detection {i}", self))
        
        sharpen_menu = QAction("Sharpen",self)
        
        gausian_blur_menu = QMenu("Gausian Blur", self)
        gausian_blur_menu.addAction(QAction("Gausian Blur 3x3", self))
        gausian_blur_menu.addAction(QAction("Gausian Blur 5x5", self))
        
        unshap_masking_menu = QAction("Unshap Masking", self)
        average_filter_menu = QAction("Average Filter", self)
        lowpass_filter_menu = QAction("Low Pass Filter", self)
        highpass_filter_menu = QAction("High Pass Filter", self)
        bandstop_filter_menu = QAction("Bandstop Filter", self)
        
        self.addAction(identify_menu)
        self.addMenu(edge_detection_menu)
        self.addAction(sharpen_menu)
        self.addMenu(gausian_blur_menu)
        self.addAction(unshap_masking_menu)
        self.addAction(average_filter_menu)
        self.addAction(lowpass_filter_menu)
        self.addAction(highpass_filter_menu)
        self.addAction(bandstop_filter_menu)