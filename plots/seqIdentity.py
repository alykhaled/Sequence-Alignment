from Bio.SeqRecord import SeqRecord
from Bio.Align.Applications import ClustalwCommandline
from Bio.AlignIO import read as alignread
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import matplotlib.pyplot as plt
from Bio import Phylo
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

def sequence_identity_plot(self):
    alignment = alignread("./data/aligned.fasta", "fasta")
    identity = calculate_percent_identity(alignment)

    # Create a new figure and set up the x- and y-axes

    # Plot the percentage of identity at each position

    # Add labels and a title to the plot

    self.figure = plt.figure(figsize=(15, 5), facecolor='white')
    self.canvas = FigureCanvas(self.figure)
    self.canvas.axes = self.canvas.figure.add_subplot(111)
    self.mplgridlayout.addWidget(self.canvas, 0, 0, 1, 1)
    self.canvas.axes.clear()

    self.canvas.axes.plot(identity)
    self.canvas.axes.set_xlabel('Position in alignment')
    self.canvas.axes.set_ylabel('Percent identity')
    self.canvas.axes.set_title('Sequence identity plot')
    self.canvas.draw()

def calculate_percent_identity(alignment):
  num_positions = len(alignment[0])
  identity = []
  for i in range(num_positions):
    num_identical = 0
    for j in range(len(alignment) - 1):
      if alignment[j][i] == alignment[j+1][i]:
        num_identical += 1
    identity.append(num_identical / len(alignment))
  return identity

