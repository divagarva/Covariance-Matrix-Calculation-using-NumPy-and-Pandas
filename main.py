# Import required libraries
import numpy as np
import pandas as pd

# Step 1: Load or create the dataset (using NumPy)
# Example data: 2D NumPy array with two variables (features) and multiple observations
data = np.array([
    [65, 70, 75],
    [68, 73, 80],
    [70, 72, 78],
    [66, 71, 76],
    [68, 69, 74]
])

# Step 2: Calculate the covariance matrix using NumPy
cov_matrix_np = np.cov(data, bias=False)  # `bias=False` calculates the unbiased estimator

print("Covariance Matrix using NumPy:")
print(cov_matrix_np)

# Step 3 (Optional): Calculate the covariance matrix using Pandas
# Convert the data to a Pandas DataFrame for better labeling
df = pd.DataFrame(data, columns=["Feature1", "Feature2", "Feature3"])

# Calculate the covariance matrix using Pandas
cov_matrix_pd = df.cov()

print("\nCovariance Matrix using Pandas:")
print(cov_matrix_pd)
