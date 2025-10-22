import random
import numpy as np

def rref(matrix):
    #Return the Reduced Row Echelon Form of a matrix.
    A = [row[:] for row in matrix]
    rows = len(A)
    cols = len(A[0])
    lead = 0

    for r in range(rows):
        if lead >= cols:
            return A
        i = r
        while A[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if cols == lead:
                    return A
        A[i], A[r] = A[r], A[i]
        lv = A[r][lead]
        A[r] = [m / lv for m in A[r]]
        for i in range(rows):
            if i != r:
                lv = A[i][lead]
                A[i] = [iv - lv * rv for rv, iv in zip(A[r], A[i])]
        lead += 1
    return A

def random_matrix():
    n = random.randint(2, 6)
    matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
    print(f"\nGenerated {n}x{n} matrix:")
    for row in matrix:
        print(row)
    return matrix

x = random_matrix()
print("\nRREF:")
r = rref(x)
for row in r:
    print([round(v, 3) for v in row])

print("\nDeterminant:", np.linalg.det(x))
