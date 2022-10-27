# This program will prompt the user to select either rock, paper, or scissors and then prompt the computer to do the same. The program will then compare the two choices and determine who is the winner. 

from random import randint

options = [
  'ROCK',
  'PAPER',
  'SCISSORS'
]

message = {
  "Tie": "Yawn it's a tie!",
  "Win": "Yay you won!",
  "Lose": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  print("User choice: %s" % (user_choice))
  print("Computer choice: %s" % (computer_choice))
  if user_choice == computer_choice:
    print(message["Tie"])
  elif user_choice == 'ROCK' and computer_choice == 'SCISSORS':
    print(message["Win"])
  elif user_choice == 'SCISSORS' and computer_choice == 'PAPER':
    print(message["Win"])
  elif user_choice == 'PAPER' and computer_choice == 'ROCK':
    print(message["Win"])
  else:
    print(message["Lose"])

def play_RPS():
  user_choice = input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice, computer_choice)

play_RPS()
