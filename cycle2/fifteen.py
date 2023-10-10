import numpy as np

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

matrix = np.array([[1, 2, 3],
                   [2, 4, 5],
                   [3, 5, 6]])

def is_symmetric(matrix):

    return np.array_equal(matrix, matrix.T)

def is_skew_symmetric(matrix):
    return np.array_equal(matrix, -matrix.T)

print(matrix)
if is_symmetric(matrix):
    print("The matrix is symmetric.")
elif is_skew_symmetric(matrix):
    print("The matrix is skew-symmetric.")
else:
    print("The matrix is neither symmetric nor skew-symmetric.")
