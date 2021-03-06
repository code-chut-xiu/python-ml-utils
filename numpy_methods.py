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

# Create larger matrix
matrix_large = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Create compressed sparse row (CSR) matrix
matrix_large_sparse = sparse.csr_matrix(matrix_large)

print("Below is also a sparsed matrix")
print(matrix_large_sparse)

# Create a row vector
vector = np.array([1, 2, 3, 4, 5, 6])
# Create a matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# Select the 3rd element of the vector
print(vector[2])
# Select the 2nd row, 2nd column of the matrix
print(matrix[1, 1])
# Select all elements of the vector
print(vector[:])
# Select everything up to and including the 3rd element of the vector
print(vector[:3])
# Select everything after the 3rd element
print(vector[3:])
# Select the last element of the vector
print(vector[-1])
# Select the 1st 2 rows and all columns of the matrix
print(matrix[:2, :])
# Select all rows and second column of the matrix
print(matrix[:, 1:2])

# Checking sizes of matrix
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# View the number of rows and columns
print(matrix.shape)

# View the number of elements (rows * columns
print(matrix.size)

# View the number of dimensions
print(matrix.ndim)

# Vectorize function
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# Create a lambda function that adds 100 to something
add_100 = lambda i: i + 100

# Create a vectorized function
vectorized_add_100 = np.vectorize(add_100)

print(vectorized_add_100(matrix))

# Or broadcasting will do the same
print(matrix + 100)

# Returns the maximum element in the matrix
print(np.max(matrix))

# And the minimum
print(np.min(matrix))

# Returns the maximum element in each column
print(np.max(matrix, axis=0))

# and the maximum element for each row
print(np.max(matrix, axis=1))

# Calculate the mean value of a matrix
print(np.mean(matrix))

# Return the variance
print(np.var(matrix))

# Return the standard deviation
print(np.std(matrix))

# Find the mean value in each column
print(np.mean(matrix, axis=0))

# Reshaping Arrays
# Adding a row to the existing matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
print(matrix.reshape(2, 6))
# Reshape with 1 row, and "as many as needed" columns
print(matrix.reshape(1, -1))
# Reshape with 1 column, and "as many as needed" rows
print(matrix.reshape(-1, 1))

# Transposing a matrix
print(matrix.T)






