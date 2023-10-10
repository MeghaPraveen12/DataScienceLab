import numpy as np

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

C = np.array([[13, 14],
              [15, 16]])

result_matrix = np.dot(np.dot(A, B), C)

print("Result Matrix:")
print(result_matrix)
