import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
iris_df = pd.read_csv('iris.csv')

# Different kinds of plots: 'scatter', 'kde', 'hist', 'reg'
# Different kinds of markers: 'o', 's', '^', 'D'

# Scatter plot with different markers
sns.pairplot(iris_df, hue='variety', markers=['o', 's', '^'], kind='scatter')
plt.suptitle('Pairwise Relationships with Scatter Plot', y=1.02)
plt.show()

# KDE plot
sns.pairplot(iris_df, hue='variety', kind='kde')
plt.suptitle('Pairwise Relationships with KDE Plot', y=1.02)
plt.show()

# Histogram
sns.pairplot(iris_df, hue='variety', kind='hist')
plt.suptitle('Pairwise Relationships with Histogram', y=1.02)
plt.show()

# Regression plot
sns.pairplot(iris_df, hue='variety', markers=['o', 's', 'D'], kind='reg')
plt.suptitle('Pairwise Relationships with Regression Plot', y=1.02)
plt.show()
