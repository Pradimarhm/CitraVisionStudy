# layout/color_menu.py
from PyQt5.QtWidgets import QMenu, QAction

class ColorMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__("Colors", parent)

        # --- RGB Submenu ---
        rgb_submenu = QMenu("RGB", self)
        rgb_submenu.addAction(QAction("Kuning", self))
        rgb_submenu.addAction(QAction("Orange", self))
        rgb_submenu.addAction(QAction("Cyan", self))
        rgb_submenu.addAction(QAction("Ungu", self))
        rgb_submenu.addAction(QAction("Abu-abu", self))
        rgb_submenu.addAction(QAction("Coklat", self))
        rgb_submenu.addAction(QAction("Merah", self))

        # --- RGB to Gray Submenu ---
        rgb_to_gray_submenu = QMenu("RGB to Grayscale", self)
        rgb_to_gray_submenu.addAction(QAction("Average", self))
        rgb_to_gray_submenu.addAction(QAction("Lightness", self))
        rgb_to_gray_submenu.addAction(QAction("Luminance", self))

        # --- Brightness Submenu ---
        brightness_submenu = QMenu("Brightness", self)
        brightness_submenu.addAction(QAction("Contrast", self))

        # --- Bit Depth Submenu ---
        bit_depth_submenu = QMenu("Bit Depth", self)
        for i in range(1, 8):
            bit_depth_submenu.addAction(QAction(f"{i} bit", self))

        # Tambahin semua ke Color Menu
        self.addMenu(rgb_submenu)
        self.addMenu(rgb_to_gray_submenu)
        self.addMenu(brightness_submenu)
        self.addAction(QAction("Brightness - Contrast", self))
        self.addAction(QAction("Invers", self))
        self.addAction(QAction("Log Brightness", self))
        self.addMenu(bit_depth_submenu)
        self.addAction(QAction("Gamma Correction", self))
