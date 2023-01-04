import numpy as np


def localAllignment(match,mismatch,gap,seq1,seq2):
    alignment_score=0
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

    
    start_point=np.where(matrix==np.max(matrix))
    start_c= start_point[1]
    start_r=start_point[0]
    align1 = ""
    align2 = ""




    start_point=np.where(matrix==np.max(matrix))
    start_c= start_point[1]
    start_r=start_point[0]



    while matrix[i][j]!=0:
        score = matrix[i][j]
        score_diag = matrix[i-1][j-1]
        score_up = matrix[i][j-1]
        score_left = matrix[i-1][j]

        if seq1[j-1] == seq2[i-1] and score == score_diag + match:
            align1 += seq1[j-1]
            align2 += seq2[i-1]
            i -= 1
            j -= 1
            alignment_score=alignment_score+match
        elif score == score_up + gap:
            align1 += seq1[j-1]
            align2 += "-"
            j -= 1
            alignment_score=alignment_score+gap
        elif score == score_left + gap:
            align1 += "-"
            align2 += seq2[i-1]
            i -= 1
            alignment_score=alignment_score+gap
        else:
            align1 += seq1[j-1]
            align2 += seq2[i-1]
            i -= 1
            j -= 1
            alignment_score=alignment_score+mismatch
 
    return [align1[::-1],align2[::-1],alignment_score]
