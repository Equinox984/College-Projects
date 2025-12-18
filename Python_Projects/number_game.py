"""Number Guessing Game"""

import random

secret_num = random.randint(1, 20)
previous_guesses = []
tokens = 5
separator = "=============================================================\n"

loser = True
# Welcome Message
print(separator)
print("Welcome to Equinox Number Game! Make sure you have a lot of fun!\n")
print(separator)


while tokens > 0:
    usr_input = int(input("Please enter a number: "))

    if usr_input in previous_guesses:
        print("Nope, you already typed that number!\n")
    else:
        previous_guesses.append(usr_input)
        tokens = tokens - 1

        if usr_input < secret_num:
            print("Too low my friend!\n")
        elif usr_input > secret_num:
            print("Too high dude!")
        else:
            loser = False
            print("CORRECT! YOU ARE AWESOME!\n")
            break

if loser:
    print(separator)
    print("HAHAHAHAH! YOU'RE DUMB!")
    print(f"The number was: {secret_num}\n")
    print(separator)
