from PyQt5.QtWidgets import QMenu, QAction

class Morfologi(QMenu):
    def __init__(self, parent=None):
        super().__init__("Morfologi", parent)
        
        erosion = QMenu("Erosion", self)
        erosion.addAction(QAction("Square 3", self))
        erosion.addAction(QAction("Square 5", self))
        erosion.addAction(QAction("Cross 3", self))
        
        dilation = QMenu("Dilation", self)
        dilation.addAction(QAction("Square 3", self))
        dilation.addAction(QAction("Square 5", self))
        dilation.addAction(QAction("Cross 3", self))
        
        opening = QMenu("Opening", self)
        opening.addAction(QAction("Square 9", self))
        
        closing = QMenu("Opening", self)
        closing.addAction(QAction("Square 9", self))
        
        self.addMenu(erosion)
        self.addMenu(dilation)
        self.addMenu(opening)
        self.addMenu(closing)