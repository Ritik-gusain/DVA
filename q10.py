import matplotlib.pyplot as plt

# Student names
students = ['Amit', 'Neha', 'Raj', 'Simran', 'Karan']

# Heights in cm
heights = [169, 170, 177, 160, 168]

# Create horizontal bar chart
plt.barh(students, heights)

# Add title and labels
plt.title("Height of Students")
plt.xlabel("Height (cm)")
plt.ylabel("Students")

# Display values on bars
for i in range(len(heights)):
    plt.text(heights[i], i, str(heights[i]))

# Show plot
plt.show()
