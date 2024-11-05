# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 21:15:18 2024

@author: chien
"""
from datetime import date
import sys
from game_rps import rps # Import the game_rps module
from guess_number import guess_number # Import the guess_number module

# Set the title of the game
title = " Group of the Arcade - 2024 ".upper()
print(f" {title} ".center(50, "="))
print("")

def play_game(name='PlayerOne'):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f"\n{name}, Welcome back to the Arcade menu.")
        
        playerchoice = input(
            f"\n{name}, select a game to play:\n\n"
            "1. Rock, Paper, Scissors (RPS)\n"
            "2. Guess the number\n Or"
            " press \"x\" to exit the Arcade\n\n"
        )
        
        if playerchoice not in ['1', '2', 'x']:
            print(f"{name}, You select the Invalid input. Please enter 1, 2 or x.")
            return play_game(name)
        
        welcome_back = True
        
        if playerchoice == '1':
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == '2':
            guess_the_number = guess_number(name)
            guess_the_number()
        else:
            print(f"\n{name}, Thank you for playing the Arcade. See you next time!\n")
            print ("")
            title = " End of the Arcade ".upper()
            print(f" {title} ".center(50, "="))
            # comment: print the current year: 2024 and exit the game
            year = date.today().year
            print(f"@ Copyright {year}, All rights reserved.")
            print("")            
            sys.exit(f"Bye! Bye! Bye! {name}! 👋👋👋 Enjoy Your life! \n\n")
                        
  
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
      description="Provides a personalized game experience with Arcade game"
    )
    
    parser.add_argument(
      "-n",
      "--name",
      metavar="name",
      required=True,
      help="The name of the person playing the game."
    )
    
    args = parser.parse_args()
    
    print(f"\n{args.name}, Welcome to the Arcade! 🤖")
    
    play_game(args.name)


