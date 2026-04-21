import pandas as pd
import numpy as np

# Creating DataFrame with missing values
data = {
    'Name':   ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Math':   [85, np.nan, 90, np.nan, 78],
    'Science':[92, 88, np.nan, 76, np.nan],
    'English':[np.nan, 75, 82, np.nan, 95]
}

df = pd.DataFrame(data)
print('--- DataFrame with Missing Values ---')
print(df)

print('\n--- Missing value count per column ---')
print(df.isnull().sum())

# Fill missing values with 0
df_filled = df.fillna(0)
print('\n--- DataFrame after filling NaN with 0 ---')
print(df_filled)
