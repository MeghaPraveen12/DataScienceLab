import numpy as np

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

size = int(input("Enter the size of the square matrix: "))

print(f"Enter {size}x{size} matrix:")
user_matrix = np.array([list(map(int, input().split())) for _ in range(size)])

print("\nUser Input Matrix:")
print(user_matrix)

try:
    inverse_matrix = np.linalg.inv(user_matrix)
    print("\nInverse of the Matrix:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("\nMatrix is singular, and its inverse does not exist.")

rank_matrix = np.linalg.matrix_rank(user_matrix)
print("\nRank of the Matrix:", rank_matrix)

determinant_matrix = np.linalg.det(user_matrix)
print("\nDeterminant of the Matrix:", determinant_matrix)

flattened_matrix = user_matrix.flatten()
print("\nMatrix as 1D Array:")
print(flattened_matrix)

eigenvalues, eigenvectors = np.linalg.eig(user_matrix)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)