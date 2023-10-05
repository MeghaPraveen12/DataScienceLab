print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")

n = int(input("Enter the value of n: "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
    print(sum, end = " ")
    count += 1
    a = b
    b = sum
    sum = a + b