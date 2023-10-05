print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

try:
    input_string = input("Enter elements separated by spaces: ")
    elements = [int(x) for x in input_string.split()]
    bubble_sort(elements)
    print("Sorted array:", elements)
except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
