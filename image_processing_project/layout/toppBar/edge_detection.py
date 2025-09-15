from PyQt5.QtWidgets import QMenu, QAction

class EdgeDirection(QMenu):
    def __init__(self, parent=None):
        super().__init__("Edge Detection", parent)
        
        self.addAction(QAction("Prewitt", self))
        self.addAction(QAction("Sobel", self))