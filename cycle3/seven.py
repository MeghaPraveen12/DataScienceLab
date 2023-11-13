import pandas as pd

iris_df = pd.read_csv('iris.csv')
print("i) Shape of the data set:")
print(iris_df.shape)

print("\nii) First 5 rows of the data set:")
print(iris_df.head())

print("\nLast 5 rows of the data set:")
print(iris_df.tail())

print("\niii) Size of the data set:")
print(iris_df.size)

print("\niv) Number of samples available for each variety:")
print(iris_df['variety'].value_counts())

print("\nv) Description of the data set:")
print(iris_df.describe())
