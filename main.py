from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QSlider, QMainWindow, QApplication, QLabel, QToolButton, QFileDialog,QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
import sys  # We need sys so that we can pass argv to QApplication
import qdarktheme
import magic
from Bio import SeqIO
from localalign import localAllignment
from globalalign import globalAllignment
from muscle import muscle


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
        self.sequences = []

    # We will use bio python for the phylogenetic tree
    # We already did dot plot
    # Need to do sequence
    # Dol ana el katbhm
    # Lhe
    # let try https://en.wikipedia.org/wiki/Sequence_logo 
    # Or Dot plot
    def browse(self):
        #match_score , mismatch_score, gap_score
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', ''," files (*.fasta *.txt )")
        chosen_file = magic.from_file(self.fname[0],mime=True)

        self.sequences = list(SeqIO.parse(self.fname[0], "fasta"))
    
        match_score = int(self.match_score_text.toPlainText())
        mismatch_score = int(self.mismatch_score_text.toPlainText())
        gap_score = int(self.gap_score_text.toPlainText())
        # Metrics to test the multiple sequenc
        # I asked chatGPT and he said Percentage of Identical Pairs and Percentage of Conserved Pairs 
        # How to calculate Percentage of Identical Pairs of multiple sequence alignment ?
        '''
        To calculate the percentage of identical pairs in a multiple sequence alignment, you can follow these steps:

            1- Align the sequences using a multiple sequence alignment algorithm.
            2- For each pair of aligned sequences, compare each position in the alignment. If the residues at a given position are the same, increment a count of identical pairs.
            3- Divide the count of identical pairs by the total number of pairs in the alignment and multiply by 100 to get the percentage of identical pairs.
        ''' 

        

        if len(self.sequences) > 2: 
            multiple_alignment = muscle(self.fname[0])
            self.aligned_seq_text = multiple_alignment
            # Let's assume we have an MSA stored in a list of strings called 'sequences'
            num_identical_pairs = 0
            num_total_pairs = len(multiple_alignment) * (len(multiple_alignment) - 1) / 2
            
            #Percent identity is calculated by dividing the number 
            #of nucleotide matches in the alignment by the total number of nucleotides (matched or mismatched)
            for i in range(len(multiple_alignment)): # Loop in every sequence
                for j in range(i + 1, len(multiple_alignment)): # Loop in every other sequence
                    for k in range(len(multiple_alignment[i])): # Loop in every position
                        if multiple_alignment[i][k] == multiple_alignment[j][k]: # If the residues at a given position are the same, increment a count of identical pairs.
                            num_identical_pairs += 1

            percentage_identical_pairs = (num_identical_pairs / num_total_pairs) * 100

        elif len(self.sequences) == 2:
            localaligned = localAllignment(match_score,mismatch_score,gap_score,self.sequences[0].seq,self.sequences[1].seq)
            globalaligned = globalAllignment(match_score,mismatch_score,gap_score,self.sequences[0].seq,self.sequences[1].seq)
            if self.local_radio_button.isChecked():
                self.aligned_seq_text = localaligned
            else:
                self.aligned_seq_text = globalaligned

                
        #cursor parking
        #-----------#
        #           #
        #           #                    
        #-----------#
        # Stick man #      
        #-----------#
        #     0     #
        #    /|\    # 
        #    / \    #                    
        #-----------#
    # Guess th 

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.setStyleSheet(qdarktheme.load_stylesheet())
stylesheet = qdarktheme.load_stylesheet(border="sharp")
w.show()
sys.exit(app.exec_())