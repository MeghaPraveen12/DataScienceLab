print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")
def sum_of_digits(number):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum

try:
    number = int(input("Enter a positive number: "))
    if number <= 0:
        print("Please enter a positive number.")
    else:
        while number > 0:
            digit_sum = sum_of_digits(number)
            print(f"{number} - {digit_sum} = {number - digit_sum}")
            number = number - digit_sum
except ValueError:
    print("Invalid input. Please enter a positive number.")
