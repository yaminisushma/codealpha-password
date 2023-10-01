import random
import string

def generate_pass(length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    return pwd


length = int(input("Enter the length of the password you need: "))
has_number = input("Do you want to have numbers (y/n)? ".lower()) == "y"
has_special = input("Do you want to have special characters (y/n)? ".lower()) == "y"
pwd = generate_pass(length, has_number, has_special)
print("The generated password is:", pwd)