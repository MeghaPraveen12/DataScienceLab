import math

print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

def gcd_fun(a, b):
   gcd = math.gcd(a, b)
   return gcd == 1

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if gcd_fun(a, b):
    print(f"{a} and {b} are coprime")
else:
    print(f"{a} and {b} are not coprime")
