import numpy as np
import argparse
parser = argparse.ArgumentParser(
                    prog = 'Sequence Alignment',
                    description = 'Global/Local Align two sequences according to match,mismatch and gap scores',
                    epilog = 'Thanks')

parser.add_argument('seq1')
parser.add_argument('seq2')
parser.add_argument('match')
parser.add_argument('mismatch')
parser.add_argument('gap')
parser.add_argument('-l', '--local', action='store_true')

args = parser.parse_args()
seq1, seq2, match, mismatch, gap, local = args.seq1, args.seq2, int(args.match), int(args.mismatch), int(args.gap), args.local
print("Sequence 1: ", seq1)
print("Sequence 2: ", seq2)
print("Match: ", match)
print("Mismatch: ", mismatch)
print("Gap: ", gap)

# seq1 = "CTATTGACGTA"
# seq2 = "CTATGAAA"
# match = 5
# mismatch = -2
# gap = -4
# local = False
def globalAllignment(match,mismatch,gap,seq1,seq2):
    matrix = [[0 for x in range( len(seq1)+1)] for y in range(len(seq2)+1)]

    # Fill in the first row and column
    for i in range(len(seq1)+1):
        matrix[0][i] = i*gap
    for i in range(len(seq2)+1):
        matrix[i][0] = i*gap

    for i in range(len(seq2)):
        for j in range(len(seq1)):
            if seq2[i] == seq1[j]:
                score = match
            else:
                score = mismatch
            matrix[i+1][j+1] = max(matrix[i][j+1] + gap, matrix[i+1][j] + gap, matrix[i][j] + score)
            
    i = len(seq2)
    j = len(seq1)
    align1 = ""
    align2 = ""

    while i > 0 and j > 0:
        score = matrix[i][j]
        score_diag = matrix[i-1][j-1]
        score_up = matrix[i][j-1]
        score_left = matrix[i-1][j]

        if seq1[j-1] == seq2[i-1] and score == score_diag + match:
            align1 += seq1[j-1]
            align2 += seq2[i-1]
            i -= 1
            j -= 1
        elif score == score_up + gap:
            align1 += seq1[j-1]
            align2 += "-"
            j -= 1
        elif score == score_left + gap:
            align1 += "-"
            align2 += seq2[i-1]
            i -= 1
        else:
            align1 += seq1[j-1]
            align2 += seq2[i-1]
            i -= 1
            j -= 1
    return (align1[::-1],align2[::-1])

def localAllignment(match,mismatch,gap,seq1,seq2):
    matrix = [[0 for x in range( len(seq1)+1)] for y in range(len(seq2)+1)]

    # Fill in the first row and column
    for i in range(len(seq1)+1):
        matrix[0][i] = 0
    for i in range(len(seq2)+1):
        matrix[i][0] = 0

    maxR, maxC = 0,0
    maxValue = -np.inf
    for i in range(len(seq2)):
        for j in range(len(seq1)):
            if seq2[i] == seq1[j]:
                score = match
            else:
                score = mismatch
            matrix[i+1][j+1] = max(matrix[i][j+1] + gap, matrix[i+1][j] + gap, matrix[i][j] + score,0)
            
            if matrix[i+1][j+1] > maxValue:
                maxValue = matrix[i+1][j+1]
                maxR = i+1
                maxC = j+1
    # Traceback
    # i = len(seq2)
    # j = len(seq1)
    i = maxR
    j = maxC
    align1 = ""
    align2 = ""

    while i > 0 and j > 0:
        score = matrix[i][j]
        score_diag = matrix[i-1][j-1]
        score_up = matrix[i][j-1]
        score_left = matrix[i-1][j]

        if seq1[j-1] == seq2[i-1] and score == score_diag + match:
            align1 += seq1[j-1]
            align2 += seq2[i-1]
            i -= 1
            j -= 1
        elif score == score_up + gap:
            align1 += seq1[j-1]
            align2 += "-"
            j -= 1
        elif score == score_left + gap:
            align1 += "-"
            align2 += seq2[i-1]
            i -= 1
        else:
            align1 += seq1[j-1]
            align2 += seq2[i-1]
            i -= 1
            j -= 1
    return (align1[::-1],align2[::-1])

if local:
    print("Local Alignment")
    alignedSeq1, alignedSeq2 = localAllignment(match,mismatch,gap,seq1,seq2)
    print(alignedSeq1)
    print(alignedSeq2)
else:
    print("Global Alignment")
    alignedSeq1, alignedSeq2 = globalAllignment(match,mismatch,gap,seq1,seq2)
    print(alignedSeq1)
    print(alignedSeq2)

