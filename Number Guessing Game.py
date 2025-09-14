# I am making a Number Guessing Game
# First I import random for it to generate a random number between 0 and 10.
from random import randint
# Then I created the variable number that I assigned to generate a random number everytime the user runs this program for them to guess
number = randint(0, 10)
# I will tell the user to guess the right number and that they have 9 tries, they have to input there guesses and it will be assigned to the variable I created "guess".
print("Try to guess the number? (Range: 0 to 10)")
print("you have 9 tries")
guess = int(input("Enter your guess (Range: 0 to 10):"))
# If the user inputs a guess above 10 or less than 0, then the program will print out "Invalid! guess can't be more/less than 10/0!" and ask them to guess again, and if the user still inputed above 10 then this will repeat
while guess > 10:
    print("Invalid! guess can't be more than 10!")
    guess = int(input("Enter your guess (Range: 0 to 10): "))
while guess < 0:
    print("Invalid! guess can't be less than 0!")
    guess = int(input("Enter your guess (Range: 0 to 10): "))
# If the user inputs the right number then the program will print "Congratulation! You won the game!", else if they input a wrong number then It will print "Incorrect! You have (tries minus the number of wrong answer) more tries." and ask them again, but if they ran out of trie then the user looses and the program will print out "Incorrect! you loose" and end the game, and if the user also inputs a number grater then 10 or less than 0, then it will do the samething as the last one will did.
if guess == number:
    print("Congratulation! You won the game!")
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
# if the user manages to put something else than a number or put more than 10 or less than 0 than the program will print out "Error!".
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