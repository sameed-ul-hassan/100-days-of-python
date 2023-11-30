import random

print("Welcome to PyPassword Generator!")
letters = int(input("How many alphabets you like to add?\n"))
symbols = int(input("How many symbols you like to add\n"))
numbers = int(input("How many numbers you like to add?\n"))

password = ''

num_list = '0123456789'
symbols_list = '!@#$%^&*{)(};"\'[<:>].,?/+-_-='
alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
final_pass = []


def generate_password(length, character_type=0):
    selected_list = num_list
    if character_type == 1:
        selected_list = symbols_list
    elif character_type == 2:
        selected_list = alphabets

    for ch in range(1, length + 1):
        # final_pass.extend(selected_list[random.randint(0, len(selected_list) - 1)])
        final_pass.extend(random.choice(selected_list))



if numbers > 0 or symbols > 0 or letters > 0:
    if numbers > 0:
        generate_password(numbers)
    if symbols > 0:
        generate_password(symbols, 1)
    if letters > 0:
        generate_password(letters, 2)

    random.shuffle(final_pass)
    shuffled_pass = ''.join(final_pass)

    print(f"Here is your password: {shuffled_pass}")
else:
    print("Please select a valid input to generate password.")