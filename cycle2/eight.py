import numpy as np

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

arr1d = np.array([int(x) for x in input("Enter elements of the 1D array separated by spaces: ").split()])
element = int(input("Enter the element to insert: "))
position = int(input("Enter the position to insert (0-based index): "))
arr1d_inserted = np.insert(arr1d, position, element)
print("Original 1D array:")
print(arr1d)
print("\n1D array after inserting the element:")
print(arr1d_inserted)
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter elements of the 2D array row by row:")
arr2d = np.array([[int(x) for x in input().split()] for _ in range(rows)])
row_index = int(input("Enter the row index to insert: "))
col_index = int(input("Enter the column index to insert: "))
element = int(input("Enter the element to insert: "))

arr2d_inserted = np.insert(arr2d, row_index, element, axis=0)
arr2d_inserted = np.insert(arr2d_inserted, col_index, element, axis=1)
print("Original 2D array:")
print(arr2d)
print("\n2D array after inserting the element:")
print(arr2d_inserted)