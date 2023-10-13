import matplotlib.pyplot as plt

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
car_values = [24000, 22500, 19700, 17500, 14500, 10000, 5800]

fig, ax = plt.subplots()

ax.plot(years, car_values, linestyle='-.', color='red', label='Car Value')
ax.scatter(years, car_values, marker='*', color='green', s=20)

ax.set_title('Value Depreciation', loc='left')
ax.set_xlabel('Year')
ax.set_ylabel('Car Value')

ax.legend()

plt.show()
