# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:46:06 2024

@author: jjuma
"""

import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    # Define the character sets to include based on user choice
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Length should be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Prompt the user for complexity options
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_special)
    
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
