import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import PIL
from PIL import ImageDraw
import random



def get_dotplot(self,seq1,seq2):
    n = len(seq1)
    m = len(seq2)

        

    matrix = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            if seq1[i] == seq2[j]:
                matrix[i, j] = 1

    if n > 100 or m > 100:
        img = PIL.Image.new('RGB', (n, m), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        for i in range(n):
            for j in range(m):
                if matrix[i, j] == 1:
                    d.point((i, j), fill=(0, 0, 0))
        # img = img.resize((500, 500))
        img.save('dotplot.png')
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.mplgridlayout.addWidget(self.canvas, 0, 0, 1, 1)
        self.canvas.axes.clear()
        self.canvas.axes.set_title('Dotplot')
        self.canvas.axes.imshow(img, cmap='gray', interpolation=None)
        self.canvas.draw()
        return
    else:
        x, y = np.where(matrix == 1)

        plt.scatter(x, y, s=5, c='black')

        self.figure = plt.figure(figsize=(15, 5), facecolor='white')
        self.canvas = FigureCanvas(self.figure)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.mplgridlayout.addWidget(self.canvas, 0, 0, 1, 1)
        self.canvas.axes.clear()

        self.canvas.axes.scatter(x, y, s=5, c='black')
        self.canvas.axes.set_xticks(range(len(seq1)))
        self.canvas.axes.set_xticklabels(seq1)

        self.canvas.axes.set_yticks(range(len(seq2)))
        self.canvas.axes.set_yticklabels(seq2)
        
        self.canvas.axes.legend(('seq1', 'seq2'),loc='upper right') 
        self.canvas.axes.set_title('Dotplot')
        self.canvas.draw()