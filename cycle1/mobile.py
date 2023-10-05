print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")
def find_absent_digits(mobile_number):
    all_digits = set("0123456789")
    mobile_digits = set(mobile_number)
    absent_digits = all_digits - mobile_digits
    return absent_digits

try:
    mobile_number = input("Enter a 10-digit mobile number: ")
    if len(mobile_number) == 10 and mobile_number.isdigit():
        absent_digits = find_absent_digits(mobile_number)
        if len(absent_digits) == 0:
            print("All digits are present in the mobile number.")
        else:
            print("Digits absent in the mobile number:", ', '.join(sorted(absent_digits)))
    else:
        print("Please enter a valid 10-digit mobile number.")
except ValueError:
    print("Invalid input. Please enter a valid 10-digit mobile number.")
