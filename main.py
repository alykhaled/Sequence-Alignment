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
from plots.seqIdentity import sequence_identity_plot
# from stats import sop


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        #Load the UI Page
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('ui_seq_alignment.ui', self)
        self.browse_button.clicked.connect(self.browse)
        self.view_alignment_button.clicked.connect(self.align)
        self.dotplot_button.clicked.connect(self.plot_dotplot)
        self.phylo_tree_button.clicked.connect(self.plot_phylogenetic)
        self.seq_logo_button.clicked.connect(self.plot_sequence_logo)
        self.seq_identity_button.clicked.connect(self.plot_sequence_identity)
        self.save_alignment_button.clicked.connect(self.save_alignment)
        self.enter_seq_text.textChanged.connect(self.validateFasta)
        self.sequences = []
        self.alignment_score=0
        self.validateFasta()
        
    def browse(self):
        try:
            self.fname = QFileDialog.getOpenFileName(self, 'Open file', ''," files (*.fasta)")
            with open(self.fname[0], 'r') as f:
                data = f.read()
            chosen_file = magic.from_file(self.fname[0],mime=True)
            self.enter_seq_text.setText(f'{str(data)}')
        except:
            msg = QMessageBox() 
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please choose correct file or enter sequence')
            msg.setWindowTitle("Error")
            msg.exec_()
    
    def validateFasta(self):
        with open('temp.fasta', 'w') as f:
            f.write(self.enter_seq_text.toPlainText())

        self.sequences = list(SeqIO.parse('temp.fasta', 'fasta'))
        if len(self.sequences) > 2:
            self.view_alignment_button.setEnabled(True)
            self.save_alignment_button.setEnabled(True)

            self.local_radio_button.setEnabled(False)
            self.global_radio_button.setEnabled(False)
            self.match_score_box.setEnabled(False)
            self.mismatch_score_box.setEnabled(False)
            self.gap_score_box.setEnabled(False)

            self.dotplot_button.setEnabled(False)
            self.phylo_tree_button.setEnabled(True)
            self.seq_logo_button.setEnabled(True)

        elif len(self.sequences) == 2:
            self.view_alignment_button.setEnabled(True)
            self.save_alignment_button.setEnabled(True)

            self.local_radio_button.setEnabled(True)
            self.global_radio_button.setEnabled(True)
            self.match_score_box.setEnabled(True)
            self.mismatch_score_box.setEnabled(True)
            self.gap_score_box.setEnabled(True)

            self.dotplot_button.setEnabled(True)
            self.phylo_tree_button.setEnabled(False)
            self.seq_logo_button.setEnabled(True)

        else:
            self.view_alignment_button.setEnabled(False)
            self.save_alignment_button.setEnabled(False)

            self.local_radio_button.setEnabled(False)
            self.global_radio_button.setEnabled(False)
            self.match_score_box.setEnabled(False)
            self.mismatch_score_box.setEnabled(False)
            self.gap_score_box.setEnabled(False)

            self.dotplot_button.setEnabled(False)
            self.phylo_tree_button.setEnabled(False)
            self.seq_logo_button.setEnabled(False)

    
    def align(self):
        if len(self.sequences) > 2: 
            multiple_alignment = muscle('./temp.fasta')
            with open('./data/aligned.fasta', 'r') as f:
                aligned_seq_raw = f.read()
            self.aligned_seq_text.setText(f'{str(aligned_seq_raw)}')

            self.local_radio_button.setEnabled(False)
            self.global_radio_button.setEnabled(False)
            self.match_score_box.setEnabled(False)
            self.mismatch_score_box.setEnabled(False)
            self.gap_score_box.setEnabled(False)

        elif len(self.sequences) == 2: 
            match_score = int(self.match_score_box.value())
            mismatch_score = int(self.mismatch_score_box.value())
            gap_score = int(self.gap_score_box.value())

            if self.local_radio_button.isChecked():
                localaligned= localAllignment(match_score,mismatch_score,gap_score,self.sequences[0].seq,self.sequences[1].seq)
                aligned_seq = (localaligned[0],localaligned[1])
                self.alignment_score=localaligned[2]
            else:
                globalaligned= globalAllignment(match_score,mismatch_score,gap_score,self.sequences[0].seq,self.sequences[1].seq)
                aligned_seq = (globalaligned[0],globalaligned[1])
                self.alignment_score=globalaligned[2]

            alignedFasta = ">"+self.sequences[0].id + "\n" + aligned_seq[0] + "\n\n" + ">"+self.sequences[1].id + "\n" + aligned_seq[1]
            self.aligned_seq_text.setText(f'{str(alignedFasta)}') 

            print(self.alignment_score)
            with open('./data/alig.fasta', 'w+') as f: # save and overwrite in saved_seq fasta file
                f.write(self.aligned_seq_text.toPlainText())

            self.disp_alignment_score.setText(f'{(self.alignment_score)}')


    def plot_dotplot(self):
        if len(self.sequences)==2:
            dotplot(self,aligned_seq[0],aligned_seq[1]) 
        else:
            msg = QMessageBox() 
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Number of sequences exceeds 2')
            msg.setWindowTitle("Error")
            msg.exec_() 

    def plot_phylogenetic(self):
        if len(self.sequences)>2:
            phylogenetic_tree(self) 
        else:
            msg = QMessageBox() 
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Number of sequences less than 2')
            msg.setWindowTitle("Error")
            msg.exec_()

    def plot_sequence_logo(self):
        # if len(self.sequences)>2:
        sequence_logo(self)
        # else:
        #     msg = QMessageBox() 
        #     msg.setIcon(QMessageBox.Critical)
        #     msg.setText("Error")
        #     msg.setInformativeText('Number of sequences less than 2')
        #     msg.setWindowTitle("Error")
        #     msg.exec_()

    def plot_sequence_identity(self):
        sequence_identity_plot(self)

    def save_alignment(self):
        with open('./data/saved_sequence.fasta', 'w+') as f: # save and overwrite in saved_seq fasta file
            f.write(self.aligned_seq_text.toPlainText())
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Success")
        msg.setInformativeText('Alignment saved successfully')
        msg.setWindowTitle("Success")
        msg.exec_()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.setStyleSheet(qdarktheme.load_stylesheet())
stylesheet = qdarktheme.load_stylesheet(border="sharp")
w.show()
sys.exit(app.exec_())