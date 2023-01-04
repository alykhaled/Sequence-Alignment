import Bio
from localalign import localAllignment
from globalalign import globalAllignment
from Bio import AlignIO
from PIL import Image
import io
from Bio.Phylo.TreeConstruction import MultipleSeqAlignment
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from muscle import muscle
import matplotlib.pyplot as plt
from Bio import Phylo
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

def phylogenetic_tree(self):


    # Read the multiple sequence alignment
    alignment = AlignIO.read("./data/aligned.fasta", "fasta")

    # Create the MultipleSeqAlignment object
    msa = MultipleSeqAlignment(alignment)

    # Calculate the distance matrix
    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(msa)

    # Construct the phylogenetic tree using the neighbor-joining method
    constructor = DistanceTreeConstructor(calculator, 'nj')
    tree = constructor.build_tree(msa)

    self.figure = plt.figure(figsize=(15, 5), facecolor='white')
    self.canvas = FigureCanvas(self.figure)
    self.canvas.axes = self.canvas.figure.add_subplot(111)
    self.mplgridlayout.addWidget(self.canvas, 0, 0, 1, 1)
    self.canvas.axes.clear()

    # Print the phylogenetic tree in Newick format
    print(tree.format("newick"))
    Phylo.draw(tree, axes=self.canvas.axes,do_show=False)

    # Show the plot
    self.canvas.axes.set_title('Phylogenetic Tree')
    self.canvas.draw()