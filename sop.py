import Bio.SubsMat.MatrixInfo as matrices

# Read the multiple sequence alignment in FASTA format
alignment = '''
>seq1
GATCTG
>seq2
GAAGAG
'''

# Parse the alignment to create a list of lists
sequences = []
for line in alignment.split('\n'):
  if line.startswith('>'):
    sequences.append('')
  else:
    sequences[-1] += line
sequences = [list(seq) for seq in sequences]

# Define a function to calculate the SOP for a pair of sequences
def calc_sop(seq1, seq2, matrix):
  sop = 0
  for i in range(len(seq1)):
    sop += matrix[(seq1[i], seq2[i])]
  return sop

# Calculate the SOP for all pairs of sequences
sop_total = 0
blosum62 = matrices.blosum62
for i in range(len(sequences)):
  for j in range(i+1, len(sequences)):
    sop = calc_sop(sequences[i], sequences[j], blosum62)
    sop_total += sop

print(f'Total SOP: {sop_total}')




