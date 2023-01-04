from Bio import SeqIO
from math import log
from collections import Counter



def percent_identity():
    fasta_read = open("./data/aligned.fasta")

    sequences = list(SeqIO.parse(fasta_read, "fasta"))
    sequences = [str(record.seq) for record in sequences]
    num_identical_pairs = 0
    num_total_pairs = len(sequences) * (len(sequences) - 1) / 2

    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):
            for k in range(len(sequences[i])):
                if sequences[i][k] == sequences[j][k]:
                    num_identical_pairs += 1

    percentage_identical_pairs = (num_identical_pairs / (num_total_pairs*len(sequences[0]))) * 100
    return percentage_identical_pairs

def sum_of_pairs():
    fasta_read = open("./data/aligned.fasta")
    records= [i for i in SeqIO.parse(fasta_read,'fasta')] # loop over the sequences and place each in a variable
    sequences = [str(record.seq) for record in records]
    sop_total = 0

    #setting match score with 3, and mismatch with -1
    pair_scores = {'AA':3, 'CC':3, 'GG':3, 'TT':3, 'AT':-1, 'AG':-1, 'AC':-1, 'GA':-1, 'GC':-1, 'GT':-1, 'TC':-1, 'TA':-1, 'TG':-1, 'CA':-1, 'CT':-1, 'CG':-1}
    #calculate sop for each pair of sequences
    for i in range(len(sequences)):
        for j in range(i+1, len(sequences)):
            sop = calc_sop(sequences[i], sequences[j], pair_scores)
            sop_total += sop

    print(f'Total SOP: {sop_total}')
    return sop_total

    # Afunction to calculate the SOP for a pair of sequences
def calc_sop(seq1, seq2, pair_scores):
    sop = 0
    for i in range(len(seq1)):
        #if not a gap, get the score from the dictionary
        if seq1[i] != '-' and seq2[i] != '-':
            sop += pair_scores[(seq1[i]+seq2[i])]
        else:
            #sdet gap penalty with -2
            sop -=2
    return sop

    # Calculate the SOP for all pairs of sequences 