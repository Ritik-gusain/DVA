import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tips = sns.load_dataset('tips')

# 1. Line Plot
plt.figure(figsize=(7,4))
data = pd.DataFrame({'x': range(10), 'y': np.cumsum(np.random.randn(10))})
sns.lineplot(data=data, x='x', y='y', marker='o')
plt.title('Line Plot')
plt.tight_layout()
plt.show()

# 2. Dist Plot (histplot in newer seaborn)
plt.figure(figsize=(7,4))
sns.histplot(tips['total_bill'], kde=True, color='skyblue')
plt.title('Dist Plot - Total Bill')
plt.tight_layout()
plt.show()

# 3. Lmplot
sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex')
plt.title('Lmplot - Total Bill vs Tip')
plt.tight_layout()
plt.show()

# 4. Count Plot
plt.figure(figsize=(7,4))
sns.countplot(data=tips, x='day', palette='Set2')
plt.title('Count Plot - Orders per Day')
plt.tight_layout()
plt.show()
