import matplotlib.pyplot as plt
import numpy as np

seq1 = "CTATTGACGTA"
seq2 = "CTATGAAA"

n = len(seq1)
m = len(seq2)

matrix = np.zeros((n, m))

for i in range(n):
    for j in range(m):
        if seq1[i] == seq2[j]:
            matrix[i, j] = 1

# plt.imshow(np.ones((len(seq1), len(seq2))), cmap='Reds', interpolation='none')
x, y = np.where(matrix == 1)
plt.scatter(x, y, s=5, c='black')
plt.xticks(range(len(seq1)), seq1)
plt.yticks(range(len(seq2)), seq2)

plt.show()