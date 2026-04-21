import matplotlib.pyplot as plt
# Medal data
medals = ['Gold', 'Silver', 'Bronze', 'Total']
values = [26, 20, 20, 66]
# Create bar graph
plt.bar(medals, values)
# Add title and labels
plt.title("Medal Tally - CWG 2018")
plt.xlabel("Medal Type")
plt.ylabel("Number of Medals")
# Show values on top of bars
for i in range(len(values)):
    plt.text(i, values[i], str(values[i]), ha='center')
# Display graph
plt.show()
