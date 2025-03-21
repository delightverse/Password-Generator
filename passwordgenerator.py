#!/usr/bin/env python
import string
import secrets
import time
import getpass
# import math

#Function that generates a random password
def generate_password():
    #Generates a password based on users preference
    pass_length=int_input("What is your desired password length(minimum:8): ", min_value=8)
   
    use_numbers=string_input("Would you want to include Numbers?")

    use_upper=string_input("Would you want to include Uppercase alphabets?")

    use_lower=string_input("Would you want to include Lowercase alphabets?")
    
    use_special=string_input("Would you want to include Special characters?")

    characters_pool =""
    if use_numbers:
        characters_pool+=string.digits

    if use_upper:
        characters_pool+=string.ascii_uppercase
    
    if use_lower:
        characters_pool+=string.ascii_lowercase

    if use_special:
        characters_pool+=string.punctuation

    if not (use_numbers or use_upper or use_lower or use_special):
        print("Error: No character set selected. Restarting selection...!")
        time.sleep(2)
        return generate_password() #Restart to function so that the user can make a valid selection

    password=''.join(secrets.choice(characters_pool) for _ in range(pass_length))
    print("\nCreating your password...")
    time.sleep(2)
    print(f"Your Password is: {password}")

#function to validate all string input
def string_input(prompt):
    #Get a valid string input from the user: Yes | No 
    while True:
        user_response=input(f"{prompt} (y/n): ").strip().lower()
        if user_response in ["y", "yes"]:
            return True
        elif user_response in ["n", "no"]:
            return False
        else:
            print("Error: Invalid input. Please enter 'y' for Yes or 'n' for No.")

#function to validate all integer input
def int_input(prompt, min_value=1):
    #Get a valid integer input from the user
    while True:
        try:
            value=int(input(prompt).strip())
            if value < min_value:
                print(f"Error: Please enter a number greater than or equal to {min_value}.")
            else:
                return value   
        except ValueError:
            print("Error: You have not made a valid response. Please input a valid number!")


#Function to check the strength of a password
def password_strength():
    """Gets a password from the user and checks the strength of the password by evaluating 
    the characters that makes up the password"""
    prev_password=getpass.getpass("Please enter the password you want to check: ")

    strength_score = 0
    if any(char.isdigit() for char in prev_password):
        strength_score += 1
    if any(char.isupper() for char in prev_password):
        strength_score += 1
    if any(char.islower() for char in prev_password):
        strength_score += 1
    if any(char in string.punctuation for char in prev_password):
        strength_score += 1
    if len(prev_password) >= 12:
        strength_score += 1

    print("\nPassword Strength Analysis:")
    if strength_score == 5:
        print("Strong password! (Very Secure)")
    elif strength_score == 4:
        print("Good password! (Secure)")
    elif strength_score == 3:
        print("Moderate password. (Consider adding more complexity)")
    elif strength_score == 2:
        print("Weak password! (Use a mix of uppercase, lowercase, numbers, and symbols)")
    else:
        print("Very weak password! (Highly insecure)")

    if strength_score <= 3:
        pass_response=string_input("Would you want to create a more secure password!")
        if pass_response:
            generate_password()
        else:
            print("Thanks for using our services. Feel free to try again later!")
    else:
        print("Keep protecting your information by using strong and secure passwords!")

#The first function that executes and leads to other functions being executed. The MAIN function
def main():
    print("Welcome to the automated password generator!")

 #Pause execution for 3seconds
    time.sleep(1.5)
    print("\nWhat would you want to do: ")
    print("[A]: Generate a password!")
    print("[B]: Check if your password is strong!")
    print() 

    task=input().strip().upper()

    if task == "A":
        generate_password()
    elif task == "B":
        password_strength()
    else:
        print("Invalid option selected. Try again next time.\nExiting...")    


if __name__ == "__main__":
    main()







