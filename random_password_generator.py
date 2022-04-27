import random
import string

print('''
            ####################################
                  RANDOM PASSWORD GENERATOR
            ####################################
''')

length = int(input("Enter the length of the password: "))

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
numbers = string.digits
special_char = string.punctuation

print("\nIf you need the following for the password, Enter (yes/no) : ")
need_lower = input("Lower Case: ")
need_Upper = input("Upper Case: ")
need_Numbers = input("Numbers: ")
need_special_char = input("Special characters: ")

all_char = ""

if need_lower.lower() == "yes":
    all_char += lower_case

if need_Upper.lower() == "yes":
    all_char += upper_case

if need_Numbers.lower() == "yes":
    all_char += numbers

if need_special_char.lower() == "yes":
    all_char += special_char


temp = random.sample(all_char, length)

password = "".join(temp)

print("\n\n")
print(password)


print("\n\nThank You for Using RPG !!!\n")