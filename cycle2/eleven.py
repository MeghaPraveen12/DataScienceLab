import numpy as np

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

cubed_matrix_multiply = np.multiply(X, np.multiply(X, X))

cubed_matrix_star = X * X * X

cubed_matrix_power = np.power(X, 3)

cubed_matrix_double_star = X ** 3

identity_matrix = np.identity(X.shape[0])

power_2_matrix = np.power(X, 2)
power_3_matrix = np.power(X, 3)
power_4_matrix = np.power(X, 4)

print("Original Matrix X:")
print(X)

print("\ni) Cubed Matrix (Using multiply()):")
print(cubed_matrix_multiply)

print("\ni) Cubed Matrix (Using * operator):")
print(cubed_matrix_star)

print("\ni) Cubed Matrix (Using power()):")
print(cubed_matrix_power)

print("\ni) Cubed Matrix (Using ** operator):")
print(cubed_matrix_double_star)

print("\nii) Identity Matrix:")
print(identity_matrix)

print("\niii) Matrix to the Power of 2:")
print(power_2_matrix)

print("\niii) Matrix to the Power of 3:")
print(power_3_matrix)

print("\niii) Matrix to the Power of 4:")
print(power_4_matrix)
