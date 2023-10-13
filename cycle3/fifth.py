import matplotlib.pyplot as plt

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

modes_of_transport = ["Walking", "Cycling", "Car", "Bus", "Train"]
frequency = [29, 15, 35, 18, 3]

fig, ax = plt.subplots()

ax.bar(modes_of_transport, frequency, width=0.1, color='green')

ax.set_xlabel('Mode of Transport')
ax.set_ylabel('Frequency')
ax.set_title('Primary Mode of Transport to School')

plt.show()
