import numpy as np
import pandas as pd

np.random.seed(10)
data = {
    'Math':    [85, 90, 78, 92, 88, 76, 95, 60, 72, 83],
    'Science': [80, 88, 75, 90, 85, 70, 92, 58, 68, 80],
    'English': [70, 65, 80, 60, 75, 85, 55, 90, 78, 72]
}

df = pd.DataFrame(data)
print('--- Student Marks DataFrame ---')
print(df)

# Covariance matrix
cov_matrix = df.cov()
print('\n--- Covariance Matrix ---')
print(cov_matrix)

# Manual covariance between Math and Science
cov_manual = np.cov(df['Math'], df['Science'])[0][1]
print(f'\nCovariance between Math and Science: {cov_manual:.4f}')

if cov_manual > 0:
    print('Positive Covariance: both subjects increase together.')
elif cov_manual < 0:
    print('Negative Covariance: one increases as other decreases.')
else:
    print('Zero Covariance: no linear relationship.')
