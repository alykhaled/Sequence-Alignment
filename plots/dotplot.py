import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import random


def dotplot(self,seq1,seq2):
    n = len(seq1)
    m = len(seq2)

    matrix = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            if seq1[i] == seq2[j]:
                matrix[i, j] = 1

    x, y = np.where(matrix == 1)

    plt.scatter(x, y, s=5, c='black')

    self.figure = plt.figure(figsize=(15, 5), facecolor='white')
    self.canvas = FigureCanvas(self.figure)
    self.canvas.axes = self.canvas.figure.add_subplot(111)
    self.mplgridlayout.addWidget(self.canvas, 0, 0, 1, 1)
#     plt.axis('on')
    self.canvas.axes.clear()

    self.canvas.axes.scatter(x, y, s=5, c='black')
    self.canvas.axes.set_xticks(range(len(seq1)))
    self.canvas.axes.set_xticklabels(seq1)

    self.canvas.axes.set_yticks(range(len(seq2)))
    self.canvas.axes.set_yticklabels(seq2)
    
    self.canvas.axes.legend(('seq1', 'seq2'),loc='upper right') 
    self.canvas.axes.set_title('Dotplot')
    self.canvas.draw()

    # self.mplgridlayout.canvas.axes.clear()

    # self.mplgridlayout.canvas.axes.scatter(x, y, s=5, c='black')
    # self.mplgridlayout.canvas.axes.set_xticks(range(len(seq1)))
    # self.mplgridlayout.canvas.axes.set_xticklabels(seq1)

    # self.mplgridlayout.canvas.axes.set_yticks(range(len(seq2)))
    # self.mplgridlayout.canvas.axes.set_yticklabels(seq2)
    
    # self.mplgridlayout.canvas.axes.legend(('seq1', 'seq2'),loc='upper right') 
    # self.mplgridlayout.canvas.axes.set_title('Dotplot')
    # self.mplgridlayout.canvas.draw()

    # self.figure = plt.figure(figsize=(15, 5), facecolor='black')
#     
#     self.gridLayout_15.addWidget(self.canvas, 0, 0, 1, 1)
#     plt.axis('on')
#     plt.bar(range(range_hist[0], range_hist[1] + 1),
#             histogram,
#             color='blue')
#     self.canvas.draw()