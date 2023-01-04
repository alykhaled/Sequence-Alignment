from math import log
from collections import Counter
from Bio import SeqIO



fasta_read = open("temp.fasta") # read a fasta  file
sequences= [i for i in SeqIO.parse(fasta_read,'fasta')] # read multiple sequences from the file


def stringToList(data):
   return list(data)

sequences_matrix = [stringToList(str(record.seq)) for record in sequences] # convert the sequences to a matrix
def MI(sequences,i,j):
    fasta_read = open("./data/aligned.fasta")
    records= [i for i in SeqIO.parse(fasta_read,'fasta')] # loop over the sequences and place each in a variable
    sequences = [str(record.seq) for record in records]
    sequences = [s for s in sequences if not '-' in [s[i],s[j]]]
    Pi = Counter(s[i] for s in sequences)
    Pj = Counter(s[j] for s in sequences)
    Pij = Counter((s[i],s[j]) for s in sequences)

    return sum(Pij[(x,y)]*log(Pij[(x,y)]/(Pi[x]*Pj[y])) for x,y in Pij)