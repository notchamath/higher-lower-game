import random
from os import system
from art import logo, vs
from game_data import data

def clear(): 
    system("clear")
    print(logo)

def shuffle_data():
    random.shuffle(data)

def start():
    clear()
    shuffle_data()
    print(f"Compare A: {data[0]}")
    print(f"Compare B: {data[1]}")

start()