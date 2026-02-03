import random
import string

print("----- RANDOM PASSWORD GENERATOR -----")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        print("\nChoose character types to include:")
        include_letters = input("Include letters? (yes/no): ").lower()
        include_numbers = input("Include numbers? (yes/no): ").lower()
        include_symbols = input("Include symbols? (yes/no): ").lower()

        characters = ""

        if include_letters == "yes":
            characters += string.ascii_letters
        if include_numbers == "yes":
            characters += string.digits
        if include_symbols == "yes":
            characters += string.punctuation

        if characters == "":
            print("\nYou must select at least one character type!")
        else:
            password = ""

            for _ in range(length):
                password += random.choice(characters)

            print("\nGenerated Password:", password)

except ValueError:
    print("Invalid input! Please enter numbers only for length.")
