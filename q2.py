import pandas as pd

# Create Series S5
S5 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Series S5:')
print(S5)

# Store square values in S6
S6 = S5 ** 2
print('\nSeries S6 (squares of S5):')
print(S6)

# Display S6 values > 15
print('\nValues in S6 that are greater than 15:')
print(S6[S6 > 15])
