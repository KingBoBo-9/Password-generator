import random

# 8 characters
# 1 uppercase
# 1 lowercase
# 1 number
# 1 special character


letters_lower = "abcdefghijklmnopqrstuvwxyz"
letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
special_chars = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
list_of_actions = [letters_lower, letters_upper, numbers, special_chars]

# print(letters_lower[random.randint(0, len(letters_lower)-1)])


def generate(length):
    password = ""

    i = 0
    while i < length:
        list_choice = random.choice(list_of_actions)
        list_choice_choice = random.choice(list_choice)
        password += list_choice_choice
        i += 1
    return password


x = generate(3)
y = generate(9)
z = generate(27)

print(f"password x = {x}")
print(f"password y = {y}")
print(f"password z = {z}")
