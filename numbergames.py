logo='''
 _______               ___.                    ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/     \/      \/     \/ 
'''
import os
import random
from random import randint
easy_level = 10
hard_level = 5

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == "easy":
        return easy_level
    else:
        return hard_level
def game():
    print(logo)
    print("Welcome to the Number Guessing Games!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1,100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns==0:
            print("You have run out of guesses, you loose.")
            return
        elif guess!= answer:
            print("Guess again.")
game()
while input("Do you want to play the number game once more? Type 'y' or 'n': ") =="y":
    screen_clear()
    game()