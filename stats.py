
from Bio import AlignIO




def perc_identity(aln):
    i = 0
    for a in range(0,len(aln[0])):
        s = aln[:,a]
        if s == len(s) * s[0]:
            i += 1
    return 100*i/float(len(aln[0]))


    