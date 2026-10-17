import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Welcome to the Number Guessing Game!")
    print("I chose a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        remaining = max_attempts - attempts
        print(f"Attempts left: {remaining}\n")

    else:
        print(f"\nSorry! You ran out of attempts. The number was {secret_number}.")

number_guessing_game()