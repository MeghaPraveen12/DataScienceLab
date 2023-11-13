import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
iris_df = pd.read_csv('iris.csv')

# Create a distribution plot for a specific column (e.g., Sepal Length)
sns.displot(iris_df['sepal.length'], kde=True)
plt.title('Distribution of Sepal Length')
plt.show()