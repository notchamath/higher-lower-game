import random
from os import system
from art import logo, vs
from game_data import data

def print_logo(score): 
    system("clear")
    print(logo)
    if score > 0:
        print(f"You are right! Current score: {score}.")

def shuffle_data():
    random.shuffle(data)

def print_comparison(obj1, obj2):
    print(f"Compare A: {obj1['name']}, a {obj1['description']} from {obj1['country']}.")
    print(vs + "\n")
    print(f"Compare B: {obj2['name']}, a {obj2['description']} from {obj2['country']}.")

def get_guess():
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == 'a' or guess == 'b':
            break

    return guess

def get_answer(obj1, obj2):
    if obj1['follower_count'] >= obj2['follower_count']:
        return obj1
    else:
        return obj2
    
def check_answer(guess, obj1, obj2):
    if guess == 'a' and obj1 == get_answer(obj1, obj2):
        return obj1
    elif guess == 'b' and obj2 == get_answer(obj1, obj2):
        return obj2
    else:
        return None
    
def end_game(score):
    print_logo(0)
    print(f"Sorry, that was wrong. Final score: {score}")

def start():
    shuffle_data()
    obj1 = data[0]
    obj2 = data[1]
    score = 0

    while True:
        print_logo(score)
        print_comparison(obj1, obj2)
        guess = get_guess()
        answer = check_answer(guess, obj1, obj2)

        if answer == None:
            end_game(score)
            break
        else:
            score += 1

            if score >= (len(data) - 1):
                print_logo(0)
                print(f"You beat the game! Final score: {score}")
                break
            else:
                obj1 = answer
                obj2 = data[score + 1]

    
start()