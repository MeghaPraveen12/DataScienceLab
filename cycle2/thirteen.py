import numpy as np

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

A = np.array([[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30]])

B = np.array([[2, 0, 1],
              [1, 2, 3],
              [0, 1, 2]])

sub_matrix = A[:3, :3]

result_matrix = np.dot(sub_matrix, B)

A[:3, :3] = result_matrix

print("Updated Matrix A:")
print(A)
