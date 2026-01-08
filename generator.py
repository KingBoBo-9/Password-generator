import random

LETTERS_LOWER = "abcdefghijklmnopqrstuvwxyz"
LETTERS_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPECIAL_CHARS = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
NUMBERS = "1234567890"
LIST_OF_ACTIONS = [LETTERS_LOWER, LETTERS_UPPER, NUMBERS, SPECIAL_CHARS]


def generate_password(length):
    while True:
        password = ""

        for i in range(length):
            list_choice = random.choice(LIST_OF_ACTIONS)
            list_choice_choice = random.choice(list_choice)
            password += list_choice_choice

        if check_password(password):
            return password


def check_password(password: str):
    has_lower = False
    has_upper = False
    has_special = False
    has_number = False

    for character in password:
        if character in LETTERS_LOWER:
            has_lower = True
        elif character in LETTERS_UPPER:
            has_upper = True
        elif character in SPECIAL_CHARS:
            has_special = True
        elif character in NUMBERS:
            has_number = True

    if has_lower and has_upper and has_special and has_number:
        return True
    else:
        return False


def main():
    password_length = int(input("Please specify length of password: "))
    if password_length < 4:
        print("Password must be at least 4 characters long.")
    else:
        generated_password = generate_password(password_length)
        print(f"The generated password was: {generated_password}")


if __name__ == "__main__":
    main()
