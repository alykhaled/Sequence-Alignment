
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import AlignIO
from Bio.SeqRecord import SeqRecord
from math import log


from Bio.Align import MultipleSeqAlignment
import time
# def perc_identity(align):

#     # a = SeqRecord(Seq("CCAAGCTGAATCAGCTGGCGGAGTCACTGAAACTGGAGCACCAGTTCCTAAGAGTTCCTTTCGAGCACTACAAGAAGACGATTCGCGCGAACCACCGCAT"), id="Alpha")
#     # b = SeqRecord(Seq("CGAAGCTGACTCAGTGGGCGGAGTCACTGAAACTGGAGCACCAGTTCCTCAGAGTCCCCTTCGAGCACTACAAGAAGACAATTCGTGCGAACCACCGCAT"), id="Beta")
#     # c = SeqRecord(Seq("CGAAGCTGACTCAGTTGGCAGAATCACTGAAACTGGAGCACCAGTTCCTCAGAGTCCCCTTCGAGCACTACAAGAAGACGATTCGTGCGAACCACCGCAT"), id="Gamma")
#     # d = SeqRecord(Seq("CGAAGCTGACTCAGTTGGCAGAGTCACTGAAACTGGAGCACCAGTTCCTCAGAGTCCCCTTCGAGCACTACAAGAAGACGATTCGTGCGAACCACCGCAT"), id="Delta")
#     # e = SeqRecord(Seq("CGAAGCTGACTCAGTTGGCGGAGTCACTGAAACTGGAGCACCAGTTCCTCAGAGTCCCCTTCGAGCACTACAAGAAGACGATTCGTGCGAACCACCGCAT"), id="Epsilon")

#     # align = MultipleSeqAlignment([a, b, c], annotations={"tool": "demo"})

#     start_time = time.time()
#     if len(align) != 1:
#         for n in range(0,len(align[0])):
#             n=0
#             i=0
#             while n<len(align[0]):    
#                 column = align[:,n]
#                 if (column == len(column) * column[0]) == True:
#                     i=i+1
#                 n=n+1

#         match = float(i)
#         length = float(n)
#         global_identity = 100*(float(match/length))
#         print(global_identity)

#     print("--- %s seconds ---" % (time.time() - start_time))



# def MI(sequences,i,j):
#     Pi = Counter(sequence[i] for sequence in sequences)
#     Pj = Counter(sequence[j] for sequence in sequences)
#     Pij = Counter((sequence[i],sequence[j]) for sequence in sequences)   

#     print(sum(Pij[(x,y)]*log(Pij[(x,y)]/(Pi[x]*Pj[y])) for x,y in Pij))

def percent_identity_two():
    records = list(SeqIO.parse("./aligned.fasta"))
    
    total_pairs=0
    sop=0
    count=0
    countall=0 
    for i in range(len(records)): #bamsek 1 sequence
        for j in range(i+1,len(records)): #bamsek el ta7to
            seq1=records[i].seq #records le awl sequence
            seq2=records[j].seq #records for other sequences
                    #For percent identity analysis
            count,countall=sum_of_pairs(seq1,seq2)
            total_pairs+=countall
            sop=sop+count
    percent_Identity=sop/total_pairs*100 
    print(percent_Identity)

def sum_of_pairs(a,b):
        count = 0
        all_pairs_count=0
        for x, y in zip(a, b):
            all_pairs_count+=1
            if x == y:
                count += 1
        print(all_pairs_count)   
        return count,all_pairs_count


    