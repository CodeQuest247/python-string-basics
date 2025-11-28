# PA5, CS7, Section D01, 10/6/2024, Aditi Menon
# ***section1***
input_string = input("Enter a string that ends with '$': ")
counter = 0
for letter in input_string:
    counter += 1
print("Character count: ", counter)
len_counter = len(input_string)
print("Character count: ", len_counter)
# ***section2***
print("This program will count both lowercase and uppercase vowels in your string")
user_input = input("Enter a string: ")
vowel_counter = 0
vowels = "aeiouAEIOU"
for letter in user_input:
    if letter in vowels:
        vowel_counter += 1
print("The number of vowels in the string is:", vowel_counter)
# ***section3***
name = input("Enter your first and last name: ")
first_name, last_name = name.split()
first_name_length = len(first_name)
last_name_length = len(last_name)
print("The number of characters in the first name is: ", first_name_length)
print("The number of characters in the last name is: ", last_name_length)