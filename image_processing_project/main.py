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
from PyQt5.QtCore import pyqtSignal


# from PyQt5.QtCore import pyqtSignal

# library dark mode
import qdarkstyle

import sys

import cv2
import  numpy as np

# import layout
from layout.topBar import top_bar

# import helper
from util.qimage_helper import numpy_to_qlabel
from util.qimage_helper import qlabel_to_numpy

# import method
from module.load_image import ImageLoader
from module.save_image import ImageSave
from module.histogram_input import histogramWindow
from module.histogram_output import histogramWindow_output
# from module.aritmetical import AritmeticalWindow

from module.filter import identify_filter
from module.filter import edge_detection_1
from module.filter import edge_detection_2
from module.filter import edge_detection_3
from module.filter import sharpen_filter
# from module.histogram_equalizer import HistogramEqualizer

from module.color.rgb import yellow_filter, orange_filter, ungu_filter, cyan_filter, abu_filter, coklat_filter, merah_filter
from module.color.rgb_to_gray import rgbToGray

from layout.view.brightness_coontras import BrightnessContrastDialog

class MainWindow(QMainWindow):
    aritmetical_triggered = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Processing App")
        
        self.setWindowIcon(QIcon("image_processing_project/assets/img/ptshp.png"))
        
        self.setGeometry(300,300,800,500)
        self.center()
        
        self.image_before = None
        
        # setup topbar
        menubar, file_menu, view_menu, color_menu, aritmetical_action, image_processing, filtering = top_bar(self)
        
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
        # self.image_process = HistogramEqualizer(self.label_before, self.label_after)
        
        # Intance loader color rgb
        self.image_yellow = yellow_filter(self.label_before, self.label_after)
        self.image_orange = orange_filter(self.label_before, self.label_after)
        self.image_ungu = ungu_filter(self.label_before, self.label_after)
        self.image_cyan = cyan_filter(self.label_before, self.label_after)
        self.image_abu = abu_filter(self.label_before, self.label_after)
        self.image_coklat = coklat_filter(self.label_before, self.label_after)
        self.image_merah = merah_filter(self.label_before, self.label_after)
        
        self.rgb_to_gray = rgbToGray(self.label_before, self.label_after)
        
        self.brcontras = BrightnessContrastDialog()

        # Hubungkan signal 
        file_menu.loadImageRequested.connect(self.image_loader.load)
        file_menu.saveImageRequested.connect(self.image_save.save_image)
        file_menu.exitRequested.connect(self.close_app)
        
        # penghubung sinyal rgb
        color_menu.kuningRequested.connect(self.image_yellow.yellow)
        color_menu.orangeRequested.connect(self.image_orange.orange)
        color_menu.unguRequested.connect(self.image_ungu.ungu)
        color_menu.cyanRequested.connect(self.image_cyan.cyan)
        color_menu.abuRequested.connect(self.image_abu.abu)
        color_menu.coklatRequested.connect(self.image_coklat.coklat)
        color_menu.merahRequested.connect(self.image_merah.merah)
        
        color_menu.brightnessContrasRequested.connect(self.open_brightness_dialog)
        
        color_menu.averageRequested.connect(self.rgb_to_gray.average)
        color_menu.lightnessRequested.connect(self.rgb_to_gray.lightness)
        color_menu.luminanceRequested.connect(self.rgb_to_gray.luminance)
        
        # sambungkan sinyal bitSelected ke handler
        color_menu.bitSelected.connect(self.apply_bit_depth)
        color_menu.inversContrasRequested.connect(self.apply_invers)
        color_menu.logBrightnessRequested.connect(self.apply_log_brightness)
        color_menu.gammaRequested.connect(self.apply_gamma_correction)
        
        # hubungkan dan tampilkan popup
        view_menu.showHistogramRequested.connect(self.show_histogram)
        view_menu.showHistogramOutputRequested.connect(self.show_histogram_output)
        
        self.image_path = None  # simpan path gambar yang di-load
        
        # image processing        
        # self.image_process = HistogramEqualizer(self.label_before, self.label_after)
        image_processing.histogramRequested.connect(self.apply_histogram_equalization)
        image_processing.fuzzyRgbRequested.connect(self.apply_fuzzy_ke_rgb)
        image_processing.fuzzyGrayRequested.connect(self.apply_fuzzy_ke_gray)


        
        # menubar, *_ , aritmetical_action = top_bar(self)
        # hubungkan action menu ke sinyal
        aritmetical_action.triggered.connect(self.aritmetical_triggered)
        # hubungkan sinyal ke slot proses gambar
        # setelah buat menubar & aritmetical_action di top_bar
        aritmetical_action.triggered.connect(self.apply_histogram_equalization)


        filtering.identifyRequested.connect(self.apply_identify)
        
        filtering.edge1Requested.connect(self.apply_edge1)
        filtering.edge2Requested.connect(self.apply_edge2)
        filtering.edge3Requested.connect(self.apply_edge3)
        
        filtering.sharpenRequested.connect(self.apply_sharpen)

        self.setStatusBar(QStatusBar(self))
        
    def load_image(self, path):
        self.image_path = path
        # tampilkan ke label_before (kode load kamu sebelumnya)
    
    # def open_aritmetical_window(self):
    #     dlg = AritmeticalWindow(self.label_before, self.label_after, self)
    #     dlg.exec_()

    # def open_histogram_equalizer(self):
    #     self.hist_eq = HistogramEqualizer(self.label_before, self.label_after)
    #     self.setCentralWidget(self.hist_eq)
    
    # FILTER 
    # identify
    def apply_identify(self):
        result = identify_filter(self.label_before)
        if result:
            self.show_pil_on_label(result, self.label_after)
        # if self.image_before is None:
        #     return
        # # 🔑 Panggil fungsi dari filters.py
        # result = identify_filter(self.label_before)
        # self.show_pil_on_label(result, self.label_after)
        
    def show_pil_on_label(self, pil_img, label):
        """Helper untuk menampilkan PIL image ke QLabel"""
        rgb = pil_img.convert("RGB")
        w, h = rgb.size
        data = rgb.tobytes("raw", "RGB")
        qimg = QImage(data, w, h, QImage.Format_RGB888)
        pix = QPixmap.fromImage(qimg)
        label.setPixmap(pix.scaled(
            label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))
    
    def apply_edge1(self):
        arr = qlabel_to_numpy(self.label_before)
        if arr is None: return
        result = edge_detection_1(arr)
        numpy_to_qlabel(result, self.label_after)

    def apply_edge2(self):
        arr = qlabel_to_numpy(self.label_before)
        if arr is None: return
        result = edge_detection_2(arr)
        numpy_to_qlabel(result, self.label_after)

    def apply_edge3(self):
        arr = qlabel_to_numpy(self.label_before)
        if arr is None: return
        result = edge_detection_3(arr)
        numpy_to_qlabel(result, self.label_after)
    
    def apply_sharpen(self):
        arr = qlabel_to_numpy(self.label_before)
        if arr is None:
            return
        result = sharpen_filter(arr)
        numpy_to_qlabel(result, self.label_after)
    
    
    # histogram
    def apply_histogram_equalization(self):
        pixmap = self.label_before.pixmap()
        if pixmap is None:
            QMessageBox.warning(self, "Peringatan", "Belum ada gambar di Original Image")
            return

        # QPixmap → QImage → numpy
        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()

        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())

        stride = qimg.bytesPerLine()  # jumlah byte per baris (bisa lebih besar dari w*3)
        arr = np.frombuffer(ptr, np.uint8).reshape((h, stride))

        # potong agar pas ke lebar sebenarnya (w * 3)
        arr = arr[:, : w * 3]
        img = arr.reshape((h, w, 3))
        # ------------------------------------------------------

        # Equalisasi hanya channel luminance
        ycrcb = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
        eq_rgb = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2RGB)

        # Tampilkan ke label_after
        h2, w2, ch = eq_rgb.shape
        bytes_per_line = ch * w2
        qimg_out = QImage(eq_rgb.data, w2, h2, bytes_per_line, QImage.Format_RGB888)
        self.label_after.setPixmap(
            QPixmap.fromImage(qimg_out).scaled(
                self.label_after.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )



    def fuzzy_ke_rgb(self, img):
        b, g, r = cv2.split(img)
        b_eq = cv2.equalizeHist(b)
        g_eq = cv2.equalizeHist(g)
        r_eq = cv2.equalizeHist(r)
        return cv2.merge([b_eq, g_eq, r_eq])

    def fuzzy_ke_gray(self, gray_img):
        return cv2.equalizeHist(gray_img)

    def apply_fuzzy_ke_rgb(self):
        pixmap = self.label_before.pixmap()
        if pixmap is None:
            QMessageBox.warning(self, "Peringatan", "Belum ada gambar di Original Image")
            return

        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        img = np.array(ptr, dtype=np.uint8).reshape((h, w, 3))

        # --- contoh fuzzy HE RGB ---
        # ini hanya placeholder sederhana,
        # ganti dengan algoritme fuzzy histogram equalization Anda
        img_fuzzy = self.fuzzy_ke_rgb(img)

        qimg_out = QImage(img_fuzzy.data, img_fuzzy.shape[1], img_fuzzy.shape[0],
                        img_fuzzy.shape[1] * 3, QImage.Format_RGB888)
        self.label_after.setPixmap(
            QPixmap.fromImage(qimg_out).scaled(
                self.label_after.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

    def apply_fuzzy_ke_gray(self):
        pixmap = self.label_before.pixmap()
        if pixmap is None:
            QMessageBox.warning(self, "Peringatan", "Belum ada gambar di Original Image")
            return

        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        img = np.array(ptr, dtype=np.uint8).reshape((h, w, 3))

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # --- contoh fuzzy HE Grayscale ---
        img_fuzzy = self.fuzzy_ke_gray(gray)

        img_rgb = cv2.cvtColor(img_fuzzy, cv2.COLOR_GRAY2RGB)
        qimg_out = QImage(img_rgb.data, img_rgb.shape[1], img_rgb.shape[0],
                        img_rgb.shape[1] * 3, QImage.Format_RGB888)
        self.label_after.setPixmap(
            QPixmap.fromImage(qimg_out).scaled(
                self.label_after.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

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
            

    # fungsi adjust brightness dan contrast
    def open_brightness_dialog(self):
        """Slot untuk membuka dialog Brightness/Contrast"""
        # from brightness_contrast_dialog import BrightnessContrastDialog
        dlg = BrightnessContrastDialog(self)
        if dlg.exec_():
            b, c = dlg.get_values()
            self.apply_bc(b, c)   # Pastikan ada fungsi apply_bc
            
    def adjust_brightness_contrast(self):
        dlg = BrightnessContrastDialog(self)
        if dlg.exec_():  # user klik OK
            b_val, c_val = dlg.get_values()
            self.apply_bc(b_val, c_val)

    def apply_bc(self, brightness, contrast):
        # --- ambil gambar dari label_before ---
        pixmap = self.label_before.pixmap()
        if pixmap is None:
            return

        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        img_rgb = np.array(ptr, dtype=np.uint8).reshape(h, w, 3)
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # --- terapkan brightness & contrast ---
        # brightness: -100..100 => beta
        # contrast: -100..100   => alpha (1 ± 0.01 * c)
        alpha = 1.0 + (contrast / 100.0)    # scale
        beta = brightness                  # shift
        adjusted = cv2.convertScaleAbs(img_bgr, alpha=alpha, beta=beta)

        # --- tampil ke label_after ---
        rgb = cv2.cvtColor(adjusted, cv2.COLOR_BGR2RGB)
        h2, w2, ch = rgb.shape
        bytes_per_line = ch * w2
        qimg2 = QImage(rgb.data, w2, h2, bytes_per_line, QImage.Format_RGB888)
        self.label_after.setPixmap(QPixmap.fromImage(qimg2))

    # bit depth
    def apply_bit_depth(self, bits):
        # Ambil QPixmap dari label
        pixmap = self.label_before.pixmap()
        if pixmap is None:
            return  # belum ada gambar

        # QPixmap -> QImage
        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()

        # QImage -> numpy array (RGB)
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        img_rgb = np.array(ptr, dtype=np.uint8).reshape(h, w, 3)

        # Sekarang img_rgb adalah array numpy, bisa diolah
        max_val = (2 ** bits) - 1
        norm = img_rgb / 255.0
        quantized = (norm * max_val).round().astype(np.uint8)
        result = (quantized * (255 // max_val)).astype(np.uint8)

        # Kembali ke QImage
        h2, w2, c = result.shape
        qimg_result = QImage(result.data, w2, h2, 3 * w2, QImage.Format_RGB888)

        # Tampilkan ke label_after
        self.label_after.setPixmap(QPixmap.fromImage(qimg_result))

    # invers 
    def apply_invers(self):
        # 1. Ambil pixmap dari label_before
        pixmap = self.label_before.pixmap()
        if pixmap is None:
            return  # Tidak ada gambar

        # 2. QPixmap -> QImage (RGB)
        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()

        # 3. QImage -> numpy array (RGB)
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        img_rgb = np.array(ptr, dtype=np.uint8).reshape(h, w, 3)

        # 4. Invers warna  (negatif): 255 - pixel
        inverted = 255 - img_rgb

        # 5. Tampilkan ke label_after
        h, w, ch = inverted.shape
        bytes_per_line = ch * w
        qimg_result = QImage(
            inverted.data, w, h, bytes_per_line, QImage.Format_RGB888
        )
        self.label_after.setPixmap(
            QPixmap.fromImage(qimg_result).scaled(
                self.label_after.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )
        
    # apply brightness log
    def apply_log_brightness(self):
        # Ambil QPixmap dari label_before
        pixmap = self.label_before.pixmap()
        if pixmap is None:
            return

        # QPixmap -> numpy array
        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        img_rgb = np.array(ptr).reshape(h, qimg.bytesPerLine(), 1)[:, :w*3].reshape(h, w, 3)

        # --- Transformasi log yang lebih jelas ---
        img_float = img_rgb.astype(np.float32)
        img_norm = img_float / 255.0  # normalisasi ke 0..1
        log_img = np.log1p(img_norm)  # log(1 + x)
        log_img = log_img / np.log1p(1)  # skalakan kembali ke 0..1
        log_img = np.uint8(log_img * 255)  # skala ke 0..255

        # QImage -> tampilkan di label_after
        bytes_per_line = 3 * w
        qimg_result = QImage(log_img.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.label_after.setPixmap(
            QPixmap.fromImage(qimg_result).scaled(
                self.label_after.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )
        
    def apply_gamma_correction(self, gamma=1.0):
        pixmap = self.label_before.pixmap()
        if pixmap is None:
            return

        # QPixmap -> numpy array
        qimg = pixmap.toImage().convertToFormat(QImage.Format_RGB888)
        w, h = qimg.width(), qimg.height()
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        img_rgb = np.array(ptr).reshape(h, qimg.bytesPerLine())[:, :w*3].reshape(h, w, 3)

        # Gamma correction
        img_float = img_rgb.astype(np.float32) / 255.0
        gamma_img = np.power(img_float, gamma)
        gamma_img = np.uint8(gamma_img * 255)

        # Tampilkan ke label_after
        bytes_per_line = 3 * w
        qimg_result = QImage(gamma_img.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.label_after.setPixmap(
            QPixmap.fromImage(qimg_result).scaled(
                self.label_after.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )


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
        
        