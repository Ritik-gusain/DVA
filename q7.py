import pandas as pd

# Create DataFrame
data = {
    'State': ['Delhi', 'Mumbai', 'Punjab', 'Haryana'],
    'Toys': [100, 150, 120, 130],
    'Books': [200, 250, 220, 210],
    'Uniform': [80, 90, 85, 95],
    'Shoes': [60, 70, 65, 75]
}

aid = pd.DataFrame(data)

# Set State as index
aid.set_index('State', inplace=True)

print("Original DataFrame:\n")
print(aid)

# -----------------------------
# (a) Books and Uniforms only
# -----------------------------
print("\n(a) Books and Uniforms only:\n")
print(aid[['Books', 'Uniform']])

# -----------------------------
# (b) Shoes only
# -----------------------------
print("\n(b) Shoes only:\n")
print(aid[['Shoes']])
