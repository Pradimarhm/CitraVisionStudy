# from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QMenu,
    QDesktopWidget,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
    QMessageBox,
)


# from PyQt5.QtCore import pyqtSignal

# library dark mode
import qdarkstyle

import sys

# import layout
from layout.topBar import top_bar

# import method
from module.load_image import ImageLoader
from module.save_image import ImageSave
from module.histogram_input import histogramWindow
from module.histogram_output import histogramWindow_output

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Processing App")
        
        self.setWindowIcon(QIcon("image_processing_project/assets/img/ptshp.png"))
        
        self.setGeometry(300,300,800,500)
        self.center()
        
        # setup topbar
        menubar, file_menu, view_menu = top_bar(self)
        
        # Label untuk gambar
        self.label_before = QLabel("Original Image")
        self.label_after = QLabel("Perubahan")

        self.label_before.setAlignment(Qt.AlignCenter)
        self.label_after.setAlignment(Qt.AlignCenter)
        
        # bikin label bisa melar
        self.label_before.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label_after.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.label_after.setStyleSheet("border: 1px dashed white; ")
        self.label_before.setStyleSheet("border: 1px dashed white; ")
        
        # Layout gambar
        img_layout = QHBoxLayout()
        img_layout.addWidget(self.label_before)
        img_layout.addWidget(self.label_after)
        
        # Layout utama
        mainbox = QVBoxLayout()
        mainbox.addLayout(img_layout)
        # mainbox.addLayout(buttonbox)
        
        # Bungkus ke QWidget baru sebagai central widget
        central_widget = QWidget()
        central_widget.setLayout(mainbox)
        self.setCentralWidget(central_widget)
        
        # Instance loader
        self.image_loader = ImageLoader(self.label_before, self.label_after)
        self.image_save = ImageSave(self.label_after, self.label_before)

        # Hubungkan signal 
        file_menu.loadImageRequested.connect(self.image_loader.load)
        file_menu.saveImageRequested.connect(self.image_save.save_image)
        file_menu.exitRequested.connect(self.close_app)
        
        # hubungkan dan tampilkan popup
        view_menu.showHistogramRequested.connect(self.show_histogram)
        view_menu.showHistogramOutputRequested.connect(self.show_histogram_output)
        
        self.image_path = None  # simpan path gambar yang di-load

        self.setStatusBar(QStatusBar(self))
        
    def load_image(self, path):
        self.image_path = path
        # tampilkan ke label_before (kode load kamu sebelumnya)

    def show_histogram(self):
        print(">> Signal diterima: buka histogram")
        if self.image_loader.file_path:
            self.hist_win = histogramWindow(self.image_loader.file_path, self)
            self.hist_win.show()
        else:
            print("!! Belum ada gambar yang diload")
            
    def show_histogram_output(self):
        print(">> Signal diterima: buka histogram")
        if self.label_after:
            self.hist_win = histogramWindow_output(self.label_after, self)
            self.hist_win.show()
        else:
            print("!! Belum ada gambar yang diload")
        
    def center(self):
        qr = self.geometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def close_app(self):
        reply = QMessageBox.question(
            self, "Konfirmasi", "Yakin mau keluar aplikasi?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()

# app = QApplication(sys.argv)
app = QApplication([])
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

window = MainWindow()

# window = QWidget()
window.show()

app.exec()


        
        # toolbar = QToolBar("My main toolbar")
        # self.addToolBar(toolbar)
        
        
        # menubar = self.menuBar()
        
        # file_menu = menubar.addMenu("File")
        # view_menu = menubar.addMenu("View")
        # color_menu = menubar.addMenu("Colors")
        # about_menu = menubar.addMenu("Tentang")
        # image_processing_menu = menubar.addMenu("Image Processing")
        # aritmetical_menu = menubar.addMenu("Aritmetical Operation")
        # filter_menu = menubar.addMenu("Filter")
        # edge_detection_menu = menubar.addMenu("Edge Detection")
        # morfologi_menu = menubar.addMenu("Morfologi")
        
        # colors submenu
        
        # rgb_submenu = QMenu("RGB", self)
        # # item subsubmenu rgb
        # yellow_action = QAction("Kuning",self)
        # orange_action = QAction("Orange",self)
        # cyan_action = QAction("Cyan",self)
        # purple_action = QAction("Ungu",self)
        # grey_action = QAction("abu-abu",self)
        # coklat_action = QAction("Coklat",self)
        # red_action = QAction("Merah",self)
        
        # rgb_submenu.addAction(yellow_action)
        # rgb_submenu.addAction(orange_action)
        # rgb_submenu.addAction(cyan_action)
        # rgb_submenu.addAction(purple_action)
        # rgb_submenu.addAction(grey_action)
        # rgb_submenu.addAction(coklat_action)
        # rgb_submenu.addAction(red_action)
        
        
        # rgb_to_gray_submenu = QMenu("RGB to Grayscale", self)
        # # item subsubmenu rgb to gray
        # average_action = QAction("Average", self)
        # lightness_action = QAction("Lightness", self)
        # luminance_action = QAction("Luminance", self)
        
        # rgb_to_gray_submenu.addAction(average_action)
        # rgb_to_gray_submenu.addAction(lightness_action)
        # rgb_to_gray_submenu.addAction(luminance_action)
        
        # brightness_submenu = QMenu("Brightness", self)
        # # item subsubmenu brightness
        # contras_action = QAction("Contrast", self)
        # brightness_submenu.addAction(contras_action)
        
        # brightness_contrast_submenu = QAction("Brightness - Contrast", self)
        # Invers_submenu = QAction("Invers", self)
        # log_brightness_submenu = QAction("Log Brightness", self)
        
        # bit_depth_submenu = QMenu("Bit Depth", self)
        # # item subsubmenu bit depth
        # onebit_action = QAction("1 bit", self)
        # twobit_action = QAction("2 bit", self)
        # threebit_action = QAction("3 bit", self)
        # fourbit_action = QAction("4 bit", self)
        # fivebit_action = QAction("5 bit", self)
        # sixbit_action = QAction("6 bit", self)
        # sevenbit_action = QAction("7 bit", self)
        
        # bit_depth_submenu.addAction(onebit_action)
        # bit_depth_submenu.addAction(twobit_action)
        # bit_depth_submenu.addAction(threebit_action)
        # bit_depth_submenu.addAction(fourbit_action)
        # bit_depth_submenu.addAction(fivebit_action)
        # bit_depth_submenu.addAction(sixbit_action)
        # bit_depth_submenu.addAction(sevenbit_action)
        
        # gamma_submenu = QAction("Gamma Correction", self)
        
        
        # color_menu.addMenu(rgb_submenu)
        # color_menu.addMenu(rgb_to_gray_submenu)
        # color_menu.addMenu(brightness_submenu)
        # color_menu.addAction(brightness_contrast_submenu)
        # color_menu.addAction(Invers_submenu)
        # color_menu.addAction(log_brightness_submenu)
        # color_menu.addMenu(bit_depth_submenu)
        # color_menu.addAction(gamma_submenu)
        
        # open_action = QAction(QIcon(), "open", self)
        # open_action.setStatusTip("Open Image")
        
        # toolbar.addAction(open_action)
        
        