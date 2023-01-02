from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QSlider, QMainWindow, QApplication, QLabel, QToolButton, QFileDialog,QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
import sys  # We need sys so that we can pass argv to QApplication
import qdarktheme


class MainWindow(QtWidgets.QMainWindow):
    
    

    def __init__(self, *args, **kwargs):
        #Load the UI Page
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('ui_seq_alignment.ui', self)





app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.setStyleSheet(qdarktheme.load_stylesheet())
stylesheet = qdarktheme.load_stylesheet(border="sharp")
w.show()
sys.exit(app.exec_())