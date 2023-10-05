print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")
def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_digits == num
for number in range(1, 1001):
    if is_armstrong_number(number):
        print(number)
