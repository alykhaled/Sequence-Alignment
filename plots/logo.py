import matplotlib.pyplot as plt
import weblogo
from PIL import Image
import io
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

def sequence_logo(self):

    # Load a multiple sequence alignment in FASTA format
    with open("./data/alig.fasta", "r") as f:
        alignment = weblogo.read_seq_data(f)

    # Generate the sequence logo
    logo_options = weblogo.LogoOptions()
    logodata = weblogo.LogoData.from_seqs(alignment)
    logo_options.title = "Multiple Sequence Alignment"
    logo_format = weblogo.LogoFormat(logodata, logo_options)

    eps = weblogo.eps_formatter(logodata, logo_format)

    pic = io.BytesIO(eps)
    img = Image.open(pic)

    self.figure = plt.figure()
    self.canvas = FigureCanvas(self.figure)
    self.canvas.axes = self.canvas.figure.add_subplot(111)
    self.mplgridlayout.addWidget(self.canvas, 0, 0, 1, 1)
    self.canvas.axes.clear()
    # Remove the axes
    self.canvas.axes.set_axis_off()

    self.canvas.axes.set_title('Sequence Logo')

    plt.imshow(img, cmap='gray', interpolation=None)

    self.canvas.draw()