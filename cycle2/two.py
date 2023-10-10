import numpy as np

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

matrix = np.array([[2+1j,3+2j,4+4j], [2+6j,4+7j,6+3j]])
dimensions = np.shape(matrix)
rows, columns = dimensions
print("Matrix:\n",matrix)
print("Number of Rows:", rows)
print("NUmber of Columns:", columns)
print("Dimension:",matrix.ndim)
matrix1=matrix.reshape(3,2)
print("New Matrix:\n",matrix1)