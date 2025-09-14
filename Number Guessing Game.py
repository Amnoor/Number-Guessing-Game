# Number Guessing Game
# The program randomly selects a number between 0 and 10. The player has 9 attempts to guess the number.
# After each incorrect guess, the program informs the player of the remaining attempts.
# If the player guesses correctly, they win; otherwise, they lose after 9 incorrect attempts.
# First I will import the randint function from the random module to generate a random number.
from random import randint
# Then I will generate a random number between 0 and 10.
number = randint(0, 10)
# Now I will start the game.
# I will print a welcome message.
print("Welcome to the Number Guessing Game!")
# I will ask the player to guess the number.
print("Try to guess the number? (Range: 0 to 10)")
print("you have 9 tries")
guess = int(input("Enter your guess (Range: 0 to 10):"))
# I will check if the guess is valid (between 0 and 10).
# if guess is above 10, I will ask the player to enter a valid guess.
while guess > 10:
    print("Invalid! guess can't be more than 10!")
    guess = int(input("Enter your guess (Range: 0 to 10): "))
# if guess is below 0, I will ask the player to enter a valid guess.
while guess < 0:
    print("Invalid! guess can't be less than 0!")
    guess = int(input("Enter your guess (Range: 0 to 10): "))
# Now I will check if the guess is correct.
if guess == number:
    print("Congratulation! You won the game!")
# If the guess is incorrect, I will inform the player of the remaining attempts, I will repeat this process until the player runs out of attempts or guesses correctly.
elif not guess == number:
    print("Incorrect! You have 8 more tries.")
    guess = int(input("Enter your guess (Range: 0 to 10): "))
    while guess > 10:
        print("Invalid! guess can't be more than 10!")
        guess = int(input("Enter your guess (Range: 0 to 10): "))
    while guess < 0:
        print("Invalid! guess can't be less than 0!")
        guess = int(input("Enter your guess (Range: 0 to 10): "))
    if guess == number:
        print("Congratulation! You won the game!")
    elif not guess == number:
        print("Incorrect! You have 7 more tries.")
        guess = int(input("Enter your guess (Range: 0 to 10): "))
        while guess > 10:
            print("Invalid! guess can't be more than 10!")
            guess = int(input("Enter your guess (Range: 0 to 10): "))
        while guess < 0:
            print("Invalid! guess can't be less than 0!")
            guess = int(input("Enter your guess (Range: 0 to 10): "))
        if guess == number:
            print("Congratulation! You won the game!")
        elif not guess == number:
            print("Incorrect! You have 6 more tries.")
            guess = int(input("Enter your guess (Range: 0 to 10): "))
            while guess > 10:
                print("Invalid! guess can't be more than 10!")
                guess = int(input("Enter your guess (Range: 0 to 10): "))
            while guess < 0:
                print("Invalid! guess can't be less than 0!")
                guess = int(input("Enter your guess (Range: 0 to 10): "))
            if guess == number:
                print("Congratulation! You won the game!")
            elif not guess == number:
                print("Incorrect! You have 5 more tries.")
                guess = int(input("Enter your guess (Range: 0 to 10): "))
                while guess > 10:
                    print("Invalid! guess can't be more than 10!")
                    guess = int(input("Enter your guess (Range: 0 to 10): "))
                while guess < 0:
                    print("Invalid! guess can't be less than 0!")
                    guess = int(input("Enter your guess (Range: 0 to 10): "))
                if guess == number:
                    print("Congratulation! You won the game!")
                elif not guess == number:
                    print("Incorrect! You have 4 more tries.")
                    guess = int(input("Enter your guess (Range: 0 to 10): "))
                    while guess > 10:
                        print("Invalid! guess can't be more than 10!")
                        guess = int(input("Enter your guess (Range: 0 to 10): "))
                    while guess < 0:
                        print("Invalid! guess can't be less than 0!")
                        guess = int(input("Enter your guess (Range: 0 to 10): "))
                    if guess == number:
                        print("Congratulation! You won the game!")
                    elif not guess == number:
                        print("Incorrect! You have 3 more tries.")
                        guess = int(input("Enter your guess (Range: 0 to 10): "))
                        while guess > 10:
                            print("Invalid! guess can't be more than 10!")
                            guess = int(input("Enter your guess (Range: 0 to 10): "))
                        while guess < 0:
                            print("Invalid! guess can't be less than 0!")
                            guess = int(input("Enter your guess (Range: 0 to 10): "))
                        if guess == number:
                            print("Congratulation! You won the game!")
                        elif not guess == number:
                            print("Incorrect! You have 2 more tries.")
                            guess = int(input("Enter your guess (Range: 0 to 10): "))
                            while guess > 10:
                                print("Invalid! guess can't be more than 10!")
                                guess = int(input("Enter your guess (Range: 0 to 10): "))
                            while guess < 0:
                                print("Invalid! guess can't be less than 0!")
                                guess = int(input("Enter your guess (Range: 0 to 10): "))
                            if guess == number:
                                print("Congratulation! You won the game!")
                            elif not guess == number:
                                print("Incorrect! You have 1 more try.")
                                guess = int(input("Enter your guess (Range: 0 to 10): "))
                                while guess > 10:
                                    print("Invalid! guess can't be more than 10!")
                                    guess = int(input("Enter your guess (Range: 0 to 10): "))
                                while guess < 0:
                                    print("Invalid! guess can't be less than 0!")
                                    guess = int(input("Enter your guess (Range: 0 to 10): "))
                                if not guess == number:
                                    print("Incorrect! you loose")
                                    print(f"The correct number was {number}.")
# Just in case the player inputs a valid number but it's still wrong, out of range or something else that I didn't account for, I will add an else statement to catch any unexpected input.
                                else:
                                    print("Error!")
                            else:
                                print("Error!")
                        else:
                            print("Error!")
                    else:
                        print("Error!")
                else:
                    print("Error!")
            else:
                print("Error!")
        else:
            print("Error!")
    else:
        print("Error!")
else:
    print("Error!")