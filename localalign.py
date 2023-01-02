import numpy as np

# download muslce and install it on your computer


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