from math import log
from collections import Counter
from Bio import SeqIO



fasta_read = open("temp.fasta") # read a fasta  file
sequences= [i for i in SeqIO.parse(fasta_read,'fasta')] # read multiple sequences from the file

# store each sequence in a variable
sequence_1= sequences[0].seq
sequence_2=sequences[1].seq
sequence_3=sequences[2].seq
sequence_4=sequences[3].seq

seq1_str = str(sequence_1)
seq2_str = str(sequence_2)
seq3_str = str(sequence_3)
seq4_str = str(sequence_4)

def stringToList(data):
   return list(data)

seq1 = stringToList(seq1_str)
seq2 = stringToList(seq2_str)
seq3 = stringToList(seq3_str)
seq4 = stringToList(seq4_str)
sequences_matrix = [seq1, seq2, seq3, seq4]
print(sequences_matrix)
length = len(sequences_matrix)


def MI(sequences,i,j):
    sequences = [s for s in sequences if not '-' in [s[i],s[j]]]
    Pi = Counter(s[i] for s in sequences)
    Pj = Counter(s[j] for s in sequences)
    Pij = Counter((s[i],s[j]) for s in sequences)

    return sum(Pij[(x,y)]*log(Pij[(x,y)]/(Pi[x]*Pj[y])) for x,y in Pij)

out = MI(sequences_matrix,4,4)
print(out)