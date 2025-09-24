# layout/color_menu.py
from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor
from PyQt5.QtCore import pyqtSignal

class ColorMenu(QMenu):
    kuningRequested = pyqtSignal()
    orangeRequested = pyqtSignal()
    cyanRequested = pyqtSignal()
    unguRequested = pyqtSignal()
    abuRequested = pyqtSignal()
    coklatRequested = pyqtSignal()
    merahRequested = pyqtSignal()
    
    averageRequested = pyqtSignal()
    lightnessRequested = pyqtSignal()
    luminanceRequested = pyqtSignal()
    
    brightnessContrasRequested = pyqtSignal()
    bitSelected = pyqtSignal(int)
    inversContrasRequested = pyqtSignal()
    logBrightnessRequested = pyqtSignal()
    gammaRequested = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__("Colors", parent)

        # --- RGB Submenu ---
        rgb_submenu = QMenu("RGB", self)
        
        self.btn_kuning = QAction('Kuning', self)
        self.btn_kuning.triggered.connect(self.on_button_kuning_click)
        rgb_submenu.addAction(self.btn_kuning)
        
        self.btn_orange = QAction('Orange', self)
        self.btn_orange.triggered.connect(self.on_button_orange_click)
        rgb_submenu.addAction(self.btn_orange)
        
        self.btn_Cyan = QAction('Cyan', self)
        self.btn_Cyan.triggered.connect(self.on_button_cyan_click)
        rgb_submenu.addAction(self.btn_Cyan)
        
        self.btn_Ungu = QAction('Ungu', self)
        self.btn_Ungu.triggered.connect(self.on_button_ungu_click)
        rgb_submenu.addAction(self.btn_Ungu)
        
        self.btn_Abu = QAction('Abu-Abu', self)
        self.btn_Abu.triggered.connect(self.on_button_abu_click)
        rgb_submenu.addAction(self.btn_Abu)
        
        self.btn_Coklat = QAction('Coklat', self)
        self.btn_Coklat.triggered.connect(self.on_button_coklat_click)
        rgb_submenu.addAction(self.btn_Coklat)
        
        self.btn_Merah = QAction('Merah', self)
        self.btn_Merah.triggered.connect(self.on_button_merah_click)
        rgb_submenu.addAction(self.btn_Merah)
        
        # rgb_submenu.addAction(QAction("Orange", self))
        # rgb_submenu.addAction(QAction("Cyan", self))
        # rgb_submenu.addAction(QAction("Ungu", self))
        # rgb_submenu.addAction(QAction("Abu-abu", self))
        # rgb_submenu.addAction(QAction("Coklat", self))
        # rgb_submenu.addAction(QAction("Merah", self))

        # --- RGB to Gray Submenu ---
        rgb_to_gray_submenu = QMenu("RGB to Grayscale", self)
        
        self.btn_Average = QAction('Average', self)
        self.btn_Average.triggered.connect(self.on_buttona_average_click)
        rgb_to_gray_submenu.addAction(self.btn_Average)
        
        self.btn_Lightness = QAction('Lightness', self)
        self.btn_Lightness.triggered.connect(self.on_buttona_lightness_click)
        rgb_to_gray_submenu.addAction(self.btn_Lightness)
        
        self.btn_Luminance = QAction('Luminance', self)
        self.btn_Luminance.triggered.connect(self.on_buttona_luminance_click)
        rgb_to_gray_submenu.addAction(self.btn_Luminance)
        
        # rgb_to_gray_submenu.addAction(QAction("Average", self))
        # rgb_to_gray_submenu.addAction(QAction("Lightness", self))
        # rgb_to_gray_submenu.addAction(QAction("Luminance", self))

        # --- Brightness Submenu ---
        brightness_submenu = QMenu("Brightness", self)
        brightness_submenu.addAction(QAction("Contrast", self))

        # --- Bit Depth Submenu ---
        bit_depth_submenu = QMenu("Bit Depth", self)
        for i in range(1, 8):
            # bit_depth_submenu.addAction(QAction(f"{i} bit", self))
            action = QAction(f"{i} bit", parent)
            action.triggered.connect(lambda _, b=i: self.bitSelected.emit(b))
            bit_depth_submenu.addAction(action)

        # Tambahin semua ke Color Menu
        self.addMenu(rgb_submenu)
        self.addMenu(rgb_to_gray_submenu)
        self.addMenu(brightness_submenu)
        
        # self.addAction(QAction("Brightness - Contrast", self))
        
        self.btn_brgight_contras = QAction('Brightness - Contrast', self)
        self.btn_brgight_contras.triggered.connect(self.on_buttona_brightness_contras_click)
        self.addAction(self.btn_brgight_contras)
        
        self.btn_invers = QAction('Invers', self)
        self.btn_invers.triggered.connect(self.on_buttona_invers_click)
        self.addAction(self.btn_invers)
        
        self.btn_log_brightness = QAction('Log Brightness', self)
        self.btn_log_brightness.triggered.connect(self.on_buttona_log_brightness_click)
        self.addAction(self.btn_log_brightness)
        
        self.addMenu(bit_depth_submenu)
        
        self.btn_gamma = QAction('Gamma Correction', self)
        self.btn_gamma.triggered.connect(self.on_buttona_gamma_click)
        self.addAction(self.btn_gamma)
        
        # self.addAction(QAction("Invers", self))
        # self.addAction(QAction("Log Brightness", self))
        # self.addAction(QAction("Gamma Correction", self))
    
    def on_button_kuning_click(self):
        self.kuningRequested.emit()
    
    def on_button_orange_click(self):
        self.orangeRequested.emit()
        
    def on_button_cyan_click(self):
        self.cyanRequested.emit()
        
    def on_button_ungu_click(self):
        self.unguRequested.emit()
        
    def on_button_abu_click(self):
        self.abuRequested.emit()
        
    def on_button_coklat_click(self):
        self.coklatRequested.emit()
        
    def on_button_merah_click(self):
        self.merahRequested.emit()
        
        
    def on_buttona_average_click(self):
        self.averageRequested.emit()
        
    def on_buttona_lightness_click(self):
        self.lightnessRequested.emit()
        
    def on_buttona_luminance_click(self):
        self.luminanceRequested.emit()
        
    def on_buttona_brightness_contras_click(self):
        self.brightnessContrasRequested.emit()
        
    
    def on_buttona_invers_click(self):
        self.inversContrasRequested.emit()


    def on_buttona_log_brightness_click(self):
        self.logBrightnessRequested.emit()
        
    def on_buttona_gamma_click(self):
        self.gammaRequested.emit()