import scipy.stats as stats
import numpy as np

# Marks of students from three different teaching methods
group1 = [85, 90, 78, 88, 92]   # Method A
group2 = [70, 75, 68, 80, 72]   # Method B
group3 = [60, 65, 58, 70, 62]   # Method C

# Perform one-way ANOVA
f_stat, p_value = stats.f_oneway(group1, group2, group3)

print('--- One-Way ANOVA Test ---')
print(f'F-Statistic : {f_stat:.4f}')
print(f'P-Value     : {p_value:.4f}')

if p_value < 0.05:
    print('Result: Reject H0 - Significant difference exists between groups.')
else:
    print('Result: Accept H0 - No significant difference between groups.')
