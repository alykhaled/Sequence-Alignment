import Bio
from localalign import localAllignment
from globalalign import globalAllignment
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import MultipleSeqAlignment
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from muscle import muscle
import matplotlib.pyplot as plt
from Bio import Phylo

# Read the multiple sequence alignment
alignment = AlignIO.read("./data/alig.fasta", "fasta")

# Create the MultipleSeqAlignment object
msa = MultipleSeqAlignment(alignment)

# Calculate the distance matrix
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(msa)

# Construct the phylogenetic tree using the neighbor-joining method
constructor = DistanceTreeConstructor(calculator, 'nj')
tree = constructor.build_tree(msa)

# Print the phylogenetic tree in Newick format
print(tree.format("newick"))
fig = plt.figure(figsize=(8, 8), dpi=80)
ax = fig.add_subplot(1, 1, 1)

# Draw the phylogenetic tree
Phylo.draw(tree, axes=ax)

# Show the plot
plt.show()