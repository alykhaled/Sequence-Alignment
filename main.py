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

from stats import sop


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        #Load the UI Page
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('ui_seq_alignment.ui', self)


        self.browse_button.clicked.connect(self.browse)
        self.view_alignment_button.clicked.connect(self.align)
        self.dotplot_button.clicked.connect(self.plot_dotplot)
        self.phylo_tree_button.clicked.connect(self.plot_phylogenetic)
        self.seq_logo_button.clicked.connect(self.plot_sequence)
        self.sequences = []
        # self.imported=0

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
            # self.sequences = list(Bio.SeqIO.parse(self.fname[0], "fasta"))
            self.enter_seq_text.setText(f'{str(data)}')
            # self.imported=1
        except:
            msg = QMessageBox() 
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please choose correct file or enter sequence')
            msg.setWindowTitle("Error")
            msg.exec_()
    

    def align(self):
        
        try:

            with open('temp.fasta', 'w') as f:
                f.write(self.enter_seq_text.toPlainText())

            self.sequences = list(Bio.SeqIO.parse('temp.fasta', "fasta"))
            if len(self.sequences) > 2: 
                multiple_alignment = muscle('./temp.fasta')
                with open('./data/alig.fasta', 'r') as f:
                    self.aligned_seq = f.read()
                self.aligned_seq_text.setText(f'{str(self.aligned_seq)}')  

                sop()
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

                alignedFasta = ">"+self.sequences[0].id + "\n" + self.aligned_seq[0] + "\n\n" + ">"+self.sequences[1].id + "\n" + self.aligned_seq[1]
                self.aligned_seq_text.setText(f'{str(alignedFasta)}') 

                # dotplot(self,self.aligned_seq[0],self.aligned_seq[1]) 

        except:
            msg = QMessageBox() 
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please Enter Sequences')
            msg.setWindowTitle("Error")
            msg.exec_()

    def plot_dotplot(self):
        if len(self.aligned_seq)==2:
            dotplot(self,self.aligned_seq[0],self.aligned_seq[1]) 
        else:
            msg = QMessageBox() 
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Number of sequences exceeds 2')
            msg.setWindowTitle("Error")
            msg.exec_() 

    def plot_phylogenetic(self):
        if len(self.aligned_seq)>2:
            phylogenetic_tree(self) 
        else:
            msg = QMessageBox() 
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Number of sequences less than 2')
            msg.setWindowTitle("Error")
            msg.exec_()

    def plot_sequence(self):
        if len(self.aligned_seq)>2:
            sequence_logo(self)
        else:
            msg = QMessageBox() 
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Number of sequences less than 2')
            msg.setWindowTitle("Error")
            msg.exec_()



    

        


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.setStyleSheet(qdarktheme.load_stylesheet())
stylesheet = qdarktheme.load_stylesheet(border="sharp")
w.show()
sys.exit(app.exec_())