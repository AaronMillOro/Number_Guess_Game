"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
# IMPORTANT !!! : Verify to run it on Python 3.x 

import random

def start_game():

    print("-" * 35 + "\nWelcome to the number guessing game!\n" + "-" * 35 + "\n") # Welcome message
    score = []        # list that will store the scores
    play_again = "y"  # loop control

    while play_again == "y":
        answer = random.randint(1,10)     # Store random integer number to guess between 1 and 10
        attemps_count = 0                 # Attemps counter
        guess_number = None               # Null variable of guessing number

        while guess_number != answer:
            try:
                guess_number = int(input("Select a number between 1 and 10: "))
                while (guess_number < 1) or (guess_number > 10): # Condition for correct range
                    guess_number = int(input("Invalid value ! Please add ONLY numbers between 1 and 10: "))

                attemps_count += 1
                if guess_number > answer:
                    print("=> It's lower")
                elif guess_number < answer:
                    print("=> It's higher")
                else:
                    print("\nGot it ! It took you {} valid try(ies)\nEnd of game".format(attemps_count))
                    score.append(attemps_count)
                    play_again = input("Want to try again? [y]es/[n]o :")
                    if play_again.lower() == "n":
                        print("Bye")
                    else:
                        print("\nThe BEST score is {}".format(min(score))) #get min value from the list
                        continue

            # Handling exceptions
            except NameError as err:
                print("Invalid value ! ({})\n Please try again".format(err))
            except SyntaxError as err:
                print("Invalid value ! ({})\n Please try again".format(err))
            except ValueError as err:
                print("Invalid value ! ({})\n Please try again".format(err))

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
