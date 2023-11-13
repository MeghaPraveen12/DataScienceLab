import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
iris_df = pd.read_csv('iris.csv')

# Create a histogram for a specific column (e.g., Sepal Width)
sns.histplot(iris_df['sepal.width'], bins=20, kde=True)
plt.title('Histogram of Sepal Width')
plt.show()
