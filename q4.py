import pandas as pd
# Create first DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Amit', 'Neha', 'Raj']
})
# Create second DataFrame
df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Age': [25, 30, 22]
})
# Create third DataFrame (for join example)
df3 = pd.DataFrame({
    'Salary': [50000, 60000, 70000]
}, index=[1, 2, 3])
print("DataFrame df1:\n", df1)
print("\nDataFrame df2:\n", df2)
print("\nDataFrame df3:\n", df3)
# -----------------------------
# 1. Using concat()
# -----------------------------
print("\n--- Using concat() ---")
# Concatenate row-wise
concat_rows = pd.concat([df1, df2])
print("\nRow-wise concatenation:")
print(concat_rows)
# Concatenate column-wise
concat_cols = pd.concat([df1, df2], axis=1)
print("\nColumn-wise concatenation:")
print(concat_cols)
# -----------------------------
# 2. Using join()
# -----------------------------
print("\n--- Using join() ---")
# Set ID as index for join
df1_index = df1.set_index('ID')
joined_df = df1_index.join(df3)
print("\nJoin result:")
print(joined_df)
# -----------------------------
# 3. Using merge()
# -----------------------------
print("\n--- Using merge() ---")
# Merge based on common column 'ID'
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print("\nInner Merge:")
print(merged_df)
# Left merge
left_merge = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Merge:")
print(left_merge)
# Outer merge
outer_merge = pd.merge(df1, df2, on='ID', how='outer')
print("\nOuter Merge:")
print(outer_merge)

