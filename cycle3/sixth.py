import matplotlib.pyplot as plt

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

heights = [61, 63, 64, 66, 68, 69, 71, 71.5, 72, 72.5, 73, 73.5, 74, 74.5, 76, 76.2, 76.5, 77, 77.5, 78, 78.5, 79, 79.2, 80, 81, 82, 83, 84, 85, 87]

fig, ax = plt.subplots()

bins = range(60, 90, 5)  # Bin edges from 60 to 85 with a bin size of 5
ax.hist(heights, bins=bins, edgecolor='black', color='blue')

ax.set_xlabel('Height (in inches)')
ax.set_ylabel('Frequency')
ax.set_title('Height Distribution of Cherry Trees')

plt.show()
