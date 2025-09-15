from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor
from PyQt5.QtCore import pyqtSignal


def colorize_icon(path, color):
    pixmap = QPixmap(path)
    painter = QPainter(pixmap)
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), QColor(color))
    painter.end()
    return QIcon(pixmap)

class File(QMenu):
    loadImageRequested = pyqtSignal()
    saveImageRequested = pyqtSignal()
    exitRequested = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__("File", parent)
        
        self.btn_load = QAction(colorize_icon("image_processing_project/assets/icon/folder-alt-svgrepo-com.svg", "#ffffff"), "Buka", self)
        self.btn_load.triggered.connect(self.on_button_click)
        self.addAction(self.btn_load)
        
        self.btn_save = QAction(colorize_icon("image_processing_project/assets/icon/save-floppy-svgrepo-com.svg", "#ffffff"), "Save", self)
        self.btn_save.triggered.connect(self.on_button_save_click)
        self.addAction(self.btn_save)
        
        self.btn_exit = QAction(colorize_icon("image_processing_project/assets/icon\out-svgrepo-com.svg", "#ffffff"), "Keluar", self)
        self.btn_exit.triggered.connect(self.on_button_exit_click)
        self.addAction(self.btn_exit)
        
    def on_button_click(self):
        self.loadImageRequested.emit()
        
    def on_button_save_click(self):
        self.saveImageRequested.emit()
    
    def on_button_exit_click(self):
        self.exitRequested.emit()