import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import AlignIO
from Bio.SeqRecord import SeqRecord
from math import log
import Bio.SubsMat.MatrixInfo as matrices
import numpy as np
from sklearn.metrics import mutual_info_score
from Bio.Align import MultipleSeqAlignment
import time

import Bio.SubsMat.MatrixInfo as matrices

def mutual_info(sequences):
    # Calculate the MI between all pairs of positions in the alignment
    alignment_array = np.array(sequences)
    mi_total = 0
    for i in range(alignment_array.shape[1]):
        for j in range(i+1, alignment_array.shape[1]):
            mi = mutual_info_score(alignment_array[:, i], alignment_array[:, j])
            mi_total += mi

    print(f'Total MI: {mi_total}')
    return mi_total

# Define a function to calculate the SOP for a pair of sequences
def calc_sop(seq1, seq2, matrix):
    sop = 0
    for i in range(len(seq1)):
        sop += matrix[(seq1[i], seq2[i])]
    return sop

def sop(sequences):
    # Calculate the SOP for all pairs of sequences
    sop_total = 0
    blosum62 = matrices.blosum62
    for i in range(len(sequences)):
        for j in range(i+1, len(sequences)):
            sop = calc_sop(sequences[i], sequences[j], blosum62)
            sop_total += sop

    print(f'Total SOP: {sop_total}')
    return sop_total
    