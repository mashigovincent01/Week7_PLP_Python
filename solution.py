# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset (using the Iris dataset as an example)
    df = pd.read_csv("iris.csv")  # Replace with your dataset path
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path and try again.")
    exit()

# Display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nDataset info:")
print(df.info())

# Check for missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Clean the dataset (if any missing values are found)
if df.isnull().sum().sum() > 0:
    df = df.fillna(method='ffill')
    print("\nMissing values filled using forward fill method.")

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic statistics of the numerical columns:")
print(df.describe())


grouped_data = df.groupby('species').mean()
print("\nMean values grouped by species:")
print(grouped_data)


print("\nFindings:")
print("1. The average petal length differs significantly across species.")
print("2. Sepal width seems relatively consistent among species.")

# Task 3: Data Visualization
# Line Chart: Trends over time (dummy time series added for demonstration)
df['dummy_time'] = range(len(df))  
plt.figure(figsize=(10, 6))
plt.plot(df['dummy_time'], df['sepal_length'], label='Sepal Length')
plt.plot(df['dummy_time'], df['petal_length'], label='Petal Length')
plt.title('Trends of Sepal and Petal Length Over Time')
plt.xlabel('Time')
plt.ylabel('Length')
plt.legend()
plt.show()

# Bar Chart: Average petal length per species
plt.figure(figsize=(8, 6))
sns.barplot(x=grouped_data.index, y='petal_length', data=grouped_data)
plt.title('Average Petal Length Per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
plt.show()

# Histogram: Distribution of sepal length
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal_length'], kde=True, bins=15)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot: Sepal length vs. Petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend()
plt.show()

# Task Completion
print("\nAll tasks completed successfully. Visualizations generated.")
