from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QSlider, QMainWindow, QApplication, QLabel, QToolButton, QFileDialog,QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
import sys  # We need sys so that we can pass argv to QApplication
import qdarktheme
import magic
import Bio
from Bio import SeqIO
from localalign import localAllignment
from globalalign import globalAllignment
from muscle import muscle
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import numpy as np
import random
from plots.dotplot import dotplot
from plots.logo import sequence_logo
from plots.phylogenetic import phylogenetic_tree

from stats import percent_identity_two
#error messg maybe add in try except?
# msg = QMessageBox() 
# msg.setIcon(QMessageBox.Critical)
# msg.setText("Error")
# msg.setInformativeText('Please choose working image')
# msg.setWindowTitle("Error")
# msg.exec_()

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        #Load the UI Page
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('ui_seq_alignment.ui', self)


        self.browse_button.clicked.connect(self.browse)
        self.view_alignment_button.clicked.connect(self.align)
        self.sequences = []
        self.imported=0

    # We will use bio python for the phylogenetic tree
    # We already did dot plot
    # Need to do sequence
    # Dol ana el katbhm
    # Lhe
    # let try https://en.wikipedia.org/wiki/Sequence_logo 
    # Or Dot plot
    def browse(self):
        try:
            self.fname = QFileDialog.getOpenFileName(self, 'Open file', ''," files (*.fasta)")
            with open(self.fname[0], 'r') as f:
                data = f.read()
            chosen_file = magic.from_file(self.fname[0],mime=True)

            self.sequences = list(Bio.SeqIO.parse(self.fname[0], "fasta"))

            self.enter_seq_text.setText(f'{str(data)}')

            self.imported=1
        except:

            msg = QMessageBox() 
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please choose correct file or enter sequence')
            msg.setWindowTitle("Error")
            msg.exec_()




        # else:

        #     self.sequences = list(Bio.SeqIO.parse(self.enter_seq_text.value))
    

    def align(self):

       if self.imported==0 and self.enter_seq_text.value !="": 
        self.sequences = list(Bio.SeqIO.parse(self.enter_seq_text.value, "fasta")) #probably wrong needs path lol


        if len(self.sequences) > 2: 
            multiple_alignment = muscle(self.fname[0])
            with open('./data/alig.fasta', 'r') as f:
                self.aligned_seq = f.read()
            self.aligned_seq_text.setText(f'{str(self.aligned_seq)}')  

            # sequence_logo(self) 
            phylogenetic_tree(self)
            percent_identity_two()

            

        elif len(self.sequences) == 2:
            match_score = int(self.match_score_box.value())
            mismatch_score = int(self.mismatch_score_box.value())
            gap_score = int(self.gap_score_box.value())

            localaligned = localAllignment(match_score,mismatch_score,gap_score,self.sequences[0].seq,self.sequences[1].seq)
            globalaligned = globalAllignment(match_score,mismatch_score,gap_score,self.sequences[0].seq,self.sequences[1].seq)
            if self.local_radio_button.isChecked():
                self.aligned_seq = localaligned
            else:
                self.aligned_seq = globalaligned

            data = self.aligned_seq[0] + '\n' + self.aligned_seq[1]
            self.aligned_seq_text.setText(f'{str(data)}') 

            dotplot(self,self.aligned_seq[0],self.aligned_seq[1])   

        


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.setStyleSheet(qdarktheme.load_stylesheet())
stylesheet = qdarktheme.load_stylesheet(border="sharp")
w.show()
sys.exit(app.exec_())