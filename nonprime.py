print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")
def is_prime(n):
   if n <= 1:
       return False
   if n <= 3:
       return True
   if n % 2 == 0 or n % 3 == 0:
       return False
   i = 5
   while i * i <= n:
       if n % i == 0 or n % (i + 2) == 0:
           return False
       i += 6
   return True
def print_non_primes_in_interval(start, end):
   for num in range(start, end + 1):
       if not is_prime(num):
           print(num, end=" ")
if __name__ == "__main__":
   start = int(input("Enter the start of the interval: "))
   end = int(input("Enter the end of the interval: "))
   print("Non-prime numbers in the interval are:")
   print_non_primes_in_interval(start, end)