import matplotlib.pyplot as plt
import weblogo
from PIL import Image
import io
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.widgets import Slider
import numpy as np

def sequence_logo(self):

    # Load a multiple sequence alignment in FASTA format
    with open("./data/aligned.fasta", "r") as f:
        alignment = weblogo.read_seq_data(f)

    # Generate the sequence logo
    logo_options = weblogo.LogoOptions()
    logodata = weblogo.LogoData.from_seqs(alignment)
    logo_options.title = "Multiple Sequence Alignment"
    logo_format = weblogo.LogoFormat(logodata, logo_options)

    eps = weblogo.eps_formatter(logodata, logo_format)

    pic = io.BytesIO(eps)
    img = Image.open(pic)
    # Save the sequence logo as a PNG image
    img.save("./data/logo.png")
    img = np.array(img)


    self.figure = plt.figure()
    self.canvas = FigureCanvas(self.figure)
    self.canvas.axes = self.canvas.figure.add_subplot(111)
    self.mplgridlayout.addWidget(self.canvas, 0, 0, 1, 1)
    self.canvas.axes.clear()


    self.canvas.axes.set_title('Sequence Logo')

    self.canvas.axes.imshow(img, cmap='gray', interpolation=None)

    self.canvas.draw()