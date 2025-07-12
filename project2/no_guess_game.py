import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
guess = None
number_of_guesses = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Loop until the user guesses the correct number
while guess != number_to_guess:
    try:
        guess = int(input("Enter your guess: "))
        number_of_guesses += 1

        if guess > number_to_guess:
            print("Lower number please.")
        elif guess < number_to_guess:
            print("Higher number please.")
        else:
            print(f"Congratulations! You guessed the number in {number_of_guesses} tries.")
    except ValueError:
        print("Please enter a valid number.")
