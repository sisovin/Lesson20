# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import random
from enum import Enum
from turtle import title

print("")
def rps(name='PlayerOne', test=False):
  game_count = 0
  player_wins = 0
  computer_wins = 0
  def decide_winner(player, computer):
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins
        if player == 1 and computer == 3:
            player_wins += 1
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            player_wins += 1
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            player_wins += 1
            return "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            computer_wins += 1
            return f"🐍 Computer wins!\nSorry, {name}..😢"

  if test:
    return decide_winner
      
  def play_rps():
      nonlocal name
      nonlocal player_wins
      nonlocal computer_wins

      class RPS(Enum):
          ROCK = 1
          PAPER = 2
          SCISSORS = 3
        
      title = " Game: Rock, Paper, Scissors (RPS) - 2024 ".upper()
      print(title.center(50, "" + ("=") + ""))
      print ('')
      print("Welcome to the game of Rock, Paper, Scissors (RPS)!")
      
          
      print("")
      # Top Section of the Menu      
      line01 = "*************************************************************"
      line02 = "*                                                           *"
      line03 = "* Enter...                                                  *"
      line04 = "* 1 for Rock,                                               *"
      line05 = "* 2 for Paper, or                                           *"
      line06 = "* 3 for scissors                                            *"
      line07 = "*                                                           *"
      # Bottom Section of the Menu
      line08 = "* Would you like to play again?                             *"
      line09 = "* Y for Yes, if you want to stop, type: Q                   *"
      line10 = "* Q to Quit                                                 *"
      print("")
      
      print(f"Hello, {name}! Let's play Rock, Paper, Scissors (RPS)!")
      print("")

      playerchoice = input(f" " + line01 + "\n " + line02 + "\n " + line03 + "\n " + line04 + "\n " + line05 + "\n " + line06 + "\n " + line07 + "\n " + line01 + "\n\n Enter your choice: ")

      if playerchoice not in ["1", "2", "3"]:
          print(f"{name}, You must enter 1, 2, or 3.")
          return play_rps()
      print("")
      
      player = int(playerchoice)
      if player < 1 or player > 3:
          print("Invalid input. Please try again.")
          sys.exit("You must enter a number:\n\n 1, 2, or 3.")

      computerchoice = random.choice("123")

      computer = int(computerchoice)

      print("")
      print(f"\n{name}, You chose {str(RPS(player)).replace('RPS.', '').title()}.")
      print(
          f"Computer chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
      )
      print("")

      def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                computer_wins += 1
                return f"🐍 Computer wins!\nSorry, {name}..😢"

      game_result = decide_winner(player, computer)
      
      print("")
      print(game_result)
      print("")
      
      nonlocal game_count
      game_count += 1
      
      print(f"\nGame count: {str(game_count)}")
      print(f"\nPlayer Wins: {str(player_wins)}")
      print(f"\nComputer Wins: {str(computer_wins)}")
      print(f"\nPlayer and Computer Tie: {str(game_count - player_wins - computer_wins)}")
          
      print(f"\nPlay again, {name}?")
      
      while True:

        playagain = input(" " + line01 + "\n " + line08 + "\n " + line09 + "\n " + line10 + "\n " + line01 + "\n\n Enter your choice: ")
        if playagain.lower() not in ["y", "q"]:
            print("Invalid input. Please try again.")
            continue
        else:
          break

      if playagain.lower() == "y":
          return play_rps()
      else:
          print("\n 🎉🎉🎉🎉 \n")  
            
          title = " End Game: Rock, Paper, Scissors (RPS) ".upper()
          print(title.center(50, "" + ("=") + ""))
          print ("Thank you for playing the game of Rock, Paper, Scissors (RPS)!")
          print ("")
          if __name__ == "__main__":          
            sys.exit(f"Bye! Bye! Bye! {name}! 👋👋👋 \n\n")
          else:
            return
          
  return play_rps    

if __name__ == "__main__":
    import argparse
    
    # Create the parser
    parser = argparse.ArgumentParser(
      description="Provides a personalized game experience."
    )
    
    # Add arguments
    parser.add_argument(
      "-n", "--name", metavar="name", 
      required=True, help="The name of the person is playing the game."
    )
    
    args = parser.parse_args()
    
    # Use the arguments
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()