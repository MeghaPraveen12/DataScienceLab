import matplotlib.pyplot as plt

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
affordable_segment = [173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131]
luxury_segment = [189, 189, 105, 112, 173, 109, 151, 197, 174, 145, 177, 161]
super_luxury_segment = [185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110]

fig, ax = plt.subplots(figsize=(8, 6))

plt.plot(months, affordable_segment, label='Affordable', color='blue', linestyle='-', marker='o')
plt.plot(months, luxury_segment, label='Luxury', color='green', linestyle='--', marker='s')
plt.plot(months, super_luxury_segment, label='Super Luxury', color='red', linestyle='-.', marker='^')

ax.set_xlabel('Months of Year')
ax.set_ylabel('Sales of Segments')
ax.set_title('Sales Data')

ax.legend(loc='upper right')

plt.show()
