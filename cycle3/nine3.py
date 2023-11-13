import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
iris_df = pd.read_csv('iris.csv')

# Create a relational plot for Sepal Length and Sepal Width
sns.relplot(x='sepal.length', y='sepal.width', hue='variety', data=iris_df, kind='scatter')
plt.title('Relational Plot between Sepal Length and Sepal Width')
plt.show()