import numpy as np

matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

matrix_sum = matrix1 + matrix2
print("Matrix Sum:")
print(matrix_sum)

matrix_diff = matrix1 - matrix2
print("\nMatrix Difference:")
print(matrix_diff)

elementwise_product = matrix1 * matrix2
print("\nElementwise Product:")
print(elementwise_product)

elementwise_division = matrix1 / matrix2
print("\nElementwise Division:")
print(elementwise_division)

matrix_product = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(matrix_product)

matrix1_transpose = np.transpose(matrix1)
print("\nTranspose of Matrix1:")
print(matrix1_transpose)

diagonal_sum = np.trace(matrix1)
print("\nSum of Diagonal Elements of Matrix1:")
print(diagonal_sum)
