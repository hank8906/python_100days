# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

################################################################

import art
import random

print(art.logo)

def guess_number():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    goal_number = random.randint(1, 100)
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        correctness = False
        num_guesses = 10
        print("You have " + str(num_guesses) + " attempts to guess the number.")
        while correctness == False and num_guesses > 0:
            num = int(input("Make a guess: "))
            if num < goal_number:
                print("Too low.")
            elif num > goal_number:
                print("Too high.")
            else:
                correctness = True
                print("You got it! The number was " + str(goal_number))
                continue_game = input("enter y to start a new game, or any other key to exit: ")
                if continue_game == "y":
                    guess_number()
                else:
                    exit()
            num_guesses -= 1
        if correctness == False:
            print("You ran out of guesses. The number was " + str(goal_number))
            continue_game = input("enter y to start a new game, or any other key to exit: ")
            if continue_game == "y":
                guess_number()
            else:
                exit()

    elif level == "hard":
        correctness = False
        num_guesses = 5
        print("You have " + str(num_guesses) + " attempts to guess the number.")
        while correctness == False and num_guesses > 0:
            num = int(input("Make a guess: "))
            if num < goal_number:
                print("Too low.")
            elif num > goal_number:
                print("Too high.")
            else:
                correctness = True
                print("You got it! The number was " + str(goal_number))
                continue_game = input("enter y to start a new game, or any other key to exit: ")
                if continue_game == "y":
                    guess_number()
                else:
                    exit()
            num_guesses -= 1
        if correctness == False:
            print("You ran out of guesses. The number was " + str(goal_number))
            continue_game = input("enter y to start a new game, or any other key to exit: ")
            if continue_game == "y":
                guess_number()
            else:
                exit()
    else:
        guess_number()

#start the game
guess_number()