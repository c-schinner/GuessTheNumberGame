from random import randint

attempts = 0
user_guess = 0
CompNum = randint(0, 101)
name = input("Please tell me your name: ")
print(f"Hello {name}\nYou have 8 attempts to guess the correct number from 1 - 100.\nGood Luck...")

while attempts < 8:
    user_guess = int(input("What number will you guess?: "))
    attempts += 1

    if user_guess > CompNum:
        print("Try a lower number.")
    elif user_guess < CompNum:
        print("Try a higher number.")
    else:
        print(f"Congratulations {name}! You have figured out my number in {attempts} guesses!")
        break

if attempts == 8:
    print(f"Sorry, you have run out of guesses.\nThe secret number was {CompNum}.")
