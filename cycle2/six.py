import numpy as np

array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]])

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

print("Elements excluding the first row:")
print(array_2d[1:, :])

print("\nElements excluding the last column:")
print(array_2d[:, :-1])

print("\nElements of 1st and 2nd column in 2nd and 3rd row:")
print(array_2d[1:3, 0:2])

print("\nElements of the 2nd and 3rd column:")
print(array_2d[:, 1:3])

print("\n2nd and 3rd element of the 1st row:")
print(array_2d[0, 1:3])

print("\nElements from indices 4 to 10 in descending order:")
print(array_2d[1:].flatten()[::-1])