import matplotlib.pyplot as plt

# Marks of a student in 10 unit tests
Marks = [72, 85, 60, 90, 78, 88, 55, 92, 76, 83]
tests  = [f'Test {i+1}' for i in range(10)]

plt.figure(figsize=(10, 5))
plt.plot(tests, Marks, marker='o', color='royalblue',
         linewidth=2, markersize=8, markerfacecolor='red')

# Annotate each point
for i, val in enumerate(Marks):
    plt.text(i, val + 1, str(val), ha='center', fontsize=9)

plt.title("Student's Performance in 10 Unit Tests", fontsize=14, fontweight='bold')
plt.xlabel('Unit Tests')
plt.ylabel('Marks (out of 100)')
plt.ylim(40, 105)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
