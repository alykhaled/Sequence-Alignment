from Bio import SeqIO
from math import log
from collections import Counter



def percent_identity():
    fasta_read = open("./data/aligned.fasta")
# sequences= [i for i in SeqIO.parse(fasta_read,'fasta')] # loop over the sequences and place each in a variable

    sequences = list(SeqIO.parse(fasta_read, "fasta"))
    # sequences = ['ABCD', 'ABCD', 'ABCD', 'ABCD']
    total_pairs=0
    sop=0
    count=0
    countall=0 

    class my_dictionary(dict): 
        # __init__ function 
        def __init__(self): 
            self = dict()   
        # Function to add key:value 
        def add(self, key, value): 
            self[key] = value 
    residue_frequency = my_dictionary() 

    def compare(a,b):
            identical_pairs_count = 0
            all_pairs_count= 0
            mismatch_pairs_count = 0
            gaps_count = 0
            for x, y in zip(a, b):
                if x!='-' and y!='-':
                    all_pairs_count+=1
                    if x == y:
                        identical_pairs_count += 1
                    else:
                        mismatch_pairs_count +=1
                else:
                    gaps_count +=1
            
            return identical_pairs_count,all_pairs_count
            


    for i in range(len(sequences)): 
     for j in range(i+1,len(sequences)): 
        seq1=sequences[i].seq 
        seq2=sequences[j].seq 

        identical_pairs_count,all_pairs_count=compare(seq1,seq2)
        
        total_pairs+=all_pairs_count

       
     return identical_pairs_count/total_pairs*100 


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