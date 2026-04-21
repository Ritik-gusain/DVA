import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.random.rand(50)   # 50 random numbers
y = np.random.rand(50)

# Calculate correlation
correlation = np.corrcoef(x, y)[0, 1]

print("Correlation between x and y:", correlation)

# Plot scatter graph
plt.scatter(x, y)
plt.title("Correlation between Two Random Variables")
plt.xlabel("X values")
plt.ylabel("Y values")

# Show plot
plt.show()
