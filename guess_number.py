# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:04:42 2024

@author: chien
"""
from datetime import date
import sys
import random
from turtle import title


def guess_number(name='Player', test=False):
    game_count = 0
    player_wins = 0
    
    def decide_winner(player, computer):
      nonlocal name
      nonlocal player_wins
      
      if player == computer:
          player_wins += 1
          return f"🎉 {name}, You won!"
      
      else:
          return f"Sorry, {name}, You lost! 😢. Better luck next time."
    
    if test:
        return decide_winner
    
    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        
        # Set the title of the game
        title = " Guess the number game - 2024 ".upper()
        print(f" {title} ".center(50, "="))
        print("")
        # Player's input's name
        print("Welcome to the game!")
        print(f"Hello, {name}! Let's play a game!")
        
        playerchoice = input(
          f"\n{name}, guess which number I'm thinking of ... 1, 2, or 3:\n\n"
        )
        
        if playerchoice not in ['1', '2', '3']:
            print(f"{name}, You select the Invalid input. Please enter 1, 2 or 3.")
            return play_guess_number()
          
        
        computerchoice = random.choice("123")
        
        print(f"\n{name}, You choose {playerchoice}.")
        
        print(
          f"I was thinking about the number {computerchoice}.\n"        
        )
        
        player = int(playerchoice)
        
        computer = int(computerchoice)
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            
            if player == computer:
                player_wins += 1
                return f"🎉 {name}, You won!"
            else:
                return f"Sorry, {name}, You lost! 😢. Better luck next time."
              
        game_result = decide_winner(player, computer)
        
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins / game_count:.2%}")
        
        print(f"\n{name}, Do you want to play again?")
        
        while True:
            playagain = input("\nPlease enter Y for Yes or Q to Quit: \n")
            if playagain.lower() not in ["y", "q"]:
                print(f"{name}, You must enter Y or Q.")
                continue
            else:
                break
        
        if playagain.lower() == 'y':
            return play_guess_number()
        else:
            print("\n🎉🎉🎉🎉")
            print(f"Thank you for playing, {name}! Goodbye!\n")            
            title = " End of Guess the number game "
            print(f" {title} ".center(50, "="))
            # comment: print the current year: 2024 and exit the game
            year = date.today().year
            print(f"@ Copyright {year}, All rights reserved.")
            print("")        
            sys.exit(f"Bye! Bye! Bye! {name}! 👋👋👋 \n\n")
      
    return play_guess_number()
  
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
      description="Provides a personalized game experience."
    )
    
    parser.add_argument(
      "-n",
      "--name",
      metavar="name",
      required=True,
      help="The name of the person playing the game."
    )
    
    args = parser.parse_args()
    
    guess_my_number = guess_number(args.name)
    guess_my_number()
        
                