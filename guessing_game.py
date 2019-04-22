"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
import random

invalid_message = "Invalid value! Please add ONLY numbers between 1 and 10:"

def start_game():
    """Guess game logic"""
    print("-"*35 + "\nWelcome to the number guessing game!\n" + "-"*35 +"\n")
    score = []
    play_again = "y"

    while play_again == "y":
        answer = random.randint(1,10)
        attemps = 0
        guess_number = None

        while guess_number != answer:
            try:
                guess_number = int(input("Select a number between 1 and 10: "))
                while (guess_number < 1) or (guess_number > 10):
                # Condition to verify correct input range
                    guess_number = int(input(invalid_message))
                attemps += 1
                if guess_number > answer:
                    print("=> It's lower")
                elif guess_number < answer:
                    print("=> It's higher")
                else:
                    print("\nGot it! It took you {} try(ies)".format(attemps))
                    print("\nEnd of game")
                    score.append(attemps)
                    play_again = input("Want to try again? [y]es/[n]o :")
                    if play_again.lower() == "n":
                        print("Bye")
                    else:
                        print("\nThe BEST score is {}".format(min(score)))
                        continue
            # Handling exceptions
            except NameError as err:
                print("Invalid value ! ({})\n Please try again".format(err))
            except SyntaxError as err:
                print("Invalid value ! ({})\n Please try again".format(err))
            except ValueError as err:
                print("Invalid value ! ({})\n Please try again".format(err))


if __name__ == '__main__':
    start_game()
