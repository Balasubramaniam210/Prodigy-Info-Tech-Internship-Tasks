import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guessed = False

    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    # Loop until the user guesses correctly
    while not guessed:
        # Prompt the user to input their guess
        user_guess = int(input("Enter your guess: "))

        # Compare the guess to the generated number
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
            guessed = True

# Run the game
guess_the_number()
