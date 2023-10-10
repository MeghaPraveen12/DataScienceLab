import numpy as np

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

arr_1d = np.array(list(map(int, input("Enter elements for 1D array separated by spaces: ").split())))

diag_1d = np.diag(arr_1d)

print("\nOriginal 1D Array:")
print(arr_1d)

print("\nDiagonal Elements (empty for 1D array):")
print(diag_1d)

n = int(input("Enter the size of the square matrix: "))
square_matrix = np.array([list(map(int, input().split())) for _ in range(n)])

diag_square_matrix = np.diag(square_matrix)

print("\nOriginal Square Matrix:")
print(square_matrix)

print("\nDiagonal Elements of Square Matrix:")
print(diag_square_matrix)