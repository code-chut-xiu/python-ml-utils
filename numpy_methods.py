import numpy as np
from scipy import sparse

# Create a vector as a row
vector_row = np.array([1, 2, 3])
print("Below is a row vector")
print(vector_row)

# Create a vector as a column
vector_col = np.array([
    [1],
    [2],
    [3]
])
print("Below is a column vector")
print(vector_col)

# A matrix is a multi-dimension array
# Create a matrix as a two-dimension (3 rows and 2 columns) array
matrix = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print("Below is a 3-row-2-column array")
print(matrix)

# The above matrix can also be created by an NumPy dedicated menthod 'mat'
matrix_object = np.mat([
    [1, 2],
    [3, 4],
    [5, 6]
])
print("Below is also a 3-row-2-column array")
print(matrix_object)

# A sparse matrix efficiently represents an array that has few nonzero values.
matrix = np.array([
    [0, 0],
    [0, 1],
    [3, 0]
])
# Create a compressed sparse row (CSR) matrix
matrix_sparse = sparse.csr_matrix(matrix)

print("Below is a sparsed matrix")
print(matrix_sparse)