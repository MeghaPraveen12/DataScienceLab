print("Megha Praveen")
print("SJC22MCA-2039")
print("MCA 2022-2024")
def count_vowels(input_string):
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    input_string = input_string.lower()
    for char in input_string:
        if char in vowel_count:
            vowel_count[char] += 1
    return vowel_count

input_string = input("Enter a string: ")
vowel_counts = count_vowels(input_string)
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")
