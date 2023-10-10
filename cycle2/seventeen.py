import numpy as np

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

U, S, VT = np.linalg.svd(A)

reconstructed_A = np.dot(U, np.dot(np.diag(S), VT))

print("Original Matrix A:")
print(A)

print("\nMatrix U:")
print(U)
print("\nMatrix S (Singular Values):")
print(S)
print("\nMatrix VT (Transpose of V):")
print(VT)

print("\nReconstructed Matrix from SVD:")
print(reconstructed_A)
