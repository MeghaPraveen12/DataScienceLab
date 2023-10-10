import numpy as np

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

A = np.array([[2, 1, -2],
              [3, 0, 1],
              [1, 1, -1]])

b = np.array([-3, 5, -2])

X = np.linalg.solve(A, b)

print("The solution for X is:")
print(X)
