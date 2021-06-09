#rock paper scissors game
import random

cdick = ["paper", "scissors", "rock"]

computer = random.choice(cdick)

valid = False

while not valid:
  try:
    player = input('''

*****************************************************************
                WELCOME TO PAPER SCISSORS ROCK
*****************************************************************

              Plese input paper, scissors or rock 
''')
    if player in cdick:
      valid = True
    else:
      print ("please enter rock, paper or scissors")
  except ValueError:
    print ("please enter rock, paper or scissors")

if player == 'paper':
  if computer == 'paper':
    print ("Computer used paper\nIts a draw")
  elif computer == "scissors":
    print ("Computer used scissors\nYou lose")
  elif computer == "rock":
    print ("Computer used rock\nYou Win")
elif player == 'scissors':
  if computer == 'paper':
    print ("Computer used paper\nYou win")
  elif computer == "scissors":
    print ("Computer used scissors\nIts a draw")
  elif computer == "rock":
    print ("Computer used rock\nYou Lose")
elif player == 'rock':
  if computer == 'paper':
    print ("Computer used paper\nYou lose")
  elif computer == "scissors":
    print ("Computer used scissors\nYou Win")
  elif computer == "rock":
    print ("Computer used rock\nIts a draw")



