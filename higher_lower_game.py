import random
from os import system
from art import logo, vs
from game_data import data

# Print logo and score
def print_logo(score):
    """
        Clears the screen and then prints the logo. Accepts argument 'score' that is the current score of the user. Then prints the user's score if score > 0. Pass in '0' as the argument to just print the logo and omit the score.
    """

    system("clear")
    print(logo)
    if score > 0:
        print(f"You are right! Current score: {score}.")

# Shuffle the list
def shuffle_data():
    """
        Shuffles the list 'data'.
    """

    random.shuffle(data)

# Print the two comparisons
def print_comparison(obj1, obj2):
    """
        Takes in 2 arguments: the two dictionaries to compare, named 'obj1' and 'obj2', then prints the 2 comparisons. 
    """

    print(f"Compare A: {obj1['name']}, a {obj1['description']} from {obj1['country']}.")
    print(vs + "\n")
    print(f"Compare B: {obj2['name']}, a {obj2['description']} from {obj2['country']}.")

# Get user's guess
def get_guess():
    """
        Asks for user's guess and returns it as an all-lowercase string.
    """

    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == 'a' or guess == 'b':
            break

    return guess

# Get the correct answer
def get_answer(obj1, obj2):
    """
        Takes in 2 arguments: two dictionaries as 'obj1' and 'obj2' then returns the one with higher follower_count value
    """

    if obj1['follower_count'] >= obj2['follower_count']:
        return obj1
    else:
        return obj2

# Check if user's guess is correct
def check_answer(guess, obj1, obj2):
    """
        Takes in 3 arguments: The user's guess as a string named 'guess' and the two comparison dictionaries as 'obj1' and 'obj2', then returns the dictionary with the higher follower_count value if the user got the guess right. Returns None if the user got it wrong.
    """
    if guess == 'a' and obj1 == get_answer(obj1, obj2):
        return obj1
    elif guess == 'b' and obj2 == get_answer(obj1, obj2):
        return obj2
    else:
        return None
    
# End the game if the user gets an answer wrong
def end_game(is_win, score):
    """
        Takes in 2 aruguments: First is a boolean value: True if user won the game, False if user lost the game. Second argument is the user's score as a Number. Then prints user's results.
    """

    print_logo(0)
    if not is_win:
        print(f"Sorry, that was wrong. Final score: {score}")
    else:
        print(f"You beat the game! Final score: {score}")

# Start game
def start():
    score = 0
    shuffle_data()

    # Since the list is shuffled, 0 and 1 indexes will hold new items everytime and iterating through the loop will avoid giving same comparison twice and comparisons to self
    obj1 = data[0]
    obj2 = data[1]

    while True:
        print_logo(score)
        print_comparison(obj1, obj2)
        guess = get_guess()
        answer = check_answer(guess, obj1, obj2)

        # If answer is incorrect, end game. Else keep going
        if answer == None:
            end_game(False, score)
            break
        else:
            score += 1

            # If user gets all comparisons right, finish game. Else move to next comparison
            if score >= (len(data) - 1):
                end_game(True, score)
                break
            else:
                obj1 = answer
                obj2 = data[score + 1]

start()