""" Python script for
   - Representing sparse matrix
   - Sparse matrix addition
   - Sparse matrix transpose  """

# Write your code from here

# Took Help from internet (From GeeksForGeeks)
# Import numpy packages and csr_matrix() from scipy.sparse
import numpy as np
from scipy.sparse import csr_matrix

# Entering row positions for values
row_num_1 = np.array([0, 0, 1, 1, 2])
# Entering column positions for the values
co_num_1 = np.array([0, 1, 2, 0, 2])
# Entering values in sparse matrix 1 to print.
values_1 = np.array([1, 4, 5, 8, 9])
# The positions which are not specified above will remain Zero's
# Creating sparse matrix using csr_matrix() method
# The array will show the matrix form
matrix_01 = csr_matrix((values_1, (row_num_1, co_num_1)),shape = (3, 3)).toarray()
print("\nFirst Sparse Matrix : \n", matrix_01)

# Creating sceond matrix same as first 
row_num_2 = np.array([0, 0, 1, 1, 2])
co_num_2 = np.array([2, 1, 1, 0, 2])
values_2 = np.array([3, 4, 7, 8, 9])
matrix_02 = csr_matrix((values_2, (row_num_2, co_num_2)),shape = (3, 3)).toarray()
print("\nSecond Sparse Matrix : \n", matrix_02)

# Addition of matrices
add_matrix = matrix_01 + matrix_02
print("\nAddtion of the two matrices is : \n", add_matrix)

# Subtraction of matrices
subtract_matrix = matrix_01 - matrix_02
print("\nSubtraction of the two matrices is : \n", subtract_matrix)

# Multiplication of matrices
muilti_matrix = matrix_01 * matrix_02
print("\nMultiplication of the two matrices is : \n" ,muilti_matrix)

#For transpose using inbulit funtion
print("\nTranspose of the given matrix 1 is \n", matrix_01.transpose())

print("\nTranspose of the given matrix 2 is \n", matrix_02.transpose())
