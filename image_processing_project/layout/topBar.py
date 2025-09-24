from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QDialog, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

from layout.toppBar.color_menu import ColorMenu
from layout.toppBar.image_processing import ImageProcessing
from layout.toppBar.filter import Filter
from layout.toppBar.edge_detection import EdgeDirection
from layout.toppBar.morfologi import Morfologi
from layout.toppBar.file import File
from layout.toppBar.view import View

from view.tentang import TentangDialog

def top_bar(parent):
    
    menubar = parent.menuBar()
        
    file_menu = File(parent)
    menubar.addMenu(file_menu)
    
    view_menu = View(parent)
    menubar.addMenu(view_menu)
    
    color_menu = ColorMenu(parent)
    menubar.addMenu(color_menu)
    
    about_action = QAction("Tentang", parent)
    about_action.triggered.connect(lambda: open_tentang(parent))
    menubar.addAction(about_action)
    
    image_processing = ImageProcessing(parent)
    menubar.addMenu(image_processing)
    
    aritmetical_action = QAction("Aritmetical Operation", parent)
    menubar.addAction(aritmetical_action)
    # aritmetical_menu.addction
    
    filtering = Filter(parent)
    menubar.addMenu(filtering)
    
    edge_direction = EdgeDirection(parent)
    menubar.addMenu(edge_direction)
    
    morfologi = Morfologi(parent)
    menubar.addMenu(morfologi)
    
    # return menubar
    return menubar, file_menu, view_menu, color_menu, aritmetical_action, image_processing, filtering

def open_tentang(parent):
    dialog = TentangDialog(parent)
    dialog.setModal(True)
    dialog.exec_()
