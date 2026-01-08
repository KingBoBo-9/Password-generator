import random

letters_lower = "abcdefghijklmnopqrstuvwxyz"
letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_chars = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
numbers = "1234567890"
list_of_actions = [letters_lower, letters_upper, numbers, special_chars]

def generate_password(length):
    password = ""

    i = 0
    while i < length:
        list_choice = random.choice(list_of_actions)
        list_choice_choice = random.choice(list_choice)
        password += list_choice_choice
        i += 1
    
    if check_password(password):
        return password
    

    

def check_password(password: str):
    has_lower = False
    has_upper = False
    has_special = False
    has_number = False

    for character in password:
        if character in letters_lower:
            has_lower = True
        elif character in letters_upper:
            has_upper = True
        elif character in special_chars:
            has_special = True
        elif character in numbers:
            has_number = True

    if (
        has_lower == True
        and has_upper == True
        and has_special == True
        and has_number == True
    ):
        return True
    else:
        print("Password does not meet requirements!")
        return False


x = generate_password(3)
y = generate_password(9)
z = generate_password(27)

print(f"password x = {x}")
print("")
print(f"Password y = {y}")
print("")
print(f"password z = {z}")
