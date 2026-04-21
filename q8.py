import pandas as pd
# Create DataFrame
data = {
    'Name': ['Amit', 'Neha', 'Raj', 'Simran', 'Karan', 'Riya'],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F'],
    'Position': ['Manager', 'Developer', 'Manager', 'Developer', 'Tester', 'Tester'],
    'City': ['Delhi', 'Delhi', 'Mumbai', 'Mumbai', 'Delhi', 'Mumbai'],
    'Age': [30, 25, 35, 28, 27, 26],
    'Projects': [5, 3, 6, 4, 2, 3]
}
naf = pd.DataFrame(data)
print("Original DataFrame:\n")
print(naf)
# -----------------------------
# Pivot Table
# -----------------------------
pivot_table = naf.pivot_table(
    values='Projects',
    index='Position',
    columns='City',
    aggfunc='sum'
)
print("\nProjects handled by each Position for each City:\n")
print(pivot_table)
