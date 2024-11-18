# Data Analysis Project

This project demonstrates data loading, exploration, basic analysis, and visualization using Python libraries like `pandas` and `matplotlib`. The analysis uses the popular **Iris dataset**, which contains information about three iris species based on petal and sepal measurements.

---

## Table of Contents
- [Objective](#objective)
- [Requirements](#requirements)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Features](#features)


---

## Objective
- Load and explore a dataset using the `pandas` library.
- Perform basic data analysis to identify trends, patterns, and statistics.
- Create visualizations with `matplotlib` and `seaborn` for data insights.

---

## Requirements
- Python 3.8+
- Libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn` (optional)

---

## Dataset
The dataset used in this project is the **Iris dataset**, which contains:
- **150 rows** of data.
- **4 numerical features**:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- **1 categorical feature**: Species (Setosa, Versicolor, Virginica).

---

## Project Workflow

### 1. Data Loading and Exploration
- Loaded the Iris dataset using `pandas`.
- Displayed the first five rows with `.head()`.
- Checked for missing values and confirmed all columns are complete.
- Explored data types and dataset structure.

### 2. Basic Data Analysis
- Used `.describe()` to compute summary statistics for numerical columns.
- Grouped data by `Species` and calculated the average of each numerical column.
- Identified interesting patterns:
  - Petal length varies significantly between species.

### 3. Data Visualization
Created visualizations to interpret the data:
- **Line Chart**: To display trends (if applicable).
- **Bar Chart**: Comparing mean petal length across species.
- **Histogram**: Visualizing the distribution of petal width.
- **Scatter Plot**: Showing relationships between sepal length and petal length.

---

## Features
1. **Data Exploration**: Quickly understand the dataset structure.
2. **Basic Statistics**: Compute mean, median, and standard deviation.
3. **Custom Visualizations**: Generate four types of charts with proper titles, labels, and legends.
4. **Clean Data Workflow**: Ensure the dataset is ready for analysis (e.g., handle missing values).

---
