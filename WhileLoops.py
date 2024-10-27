import random
correct_number = random.randint(1, 100)
guess = int(input("Guess the secret number between 1-100: "))

while guess != correct_number:
    if guess < correct_number:
        print("TOO LOW, Try Again.")
    else:
        print("TOO HIGH, Try Again.")

    guess = int(input("Guess the secret number between 1-100: "))
print("YOU GUESSED THE CORRECT NUMBER!")
        