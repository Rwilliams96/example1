#!/usr/bin/env python3.8
import random

def rps_fnctn():
  print('Rock Paper Scissors (enter "history" at any time to check score)')
  rps = ['rock','paper','scissors']
  answer = input('rock, paper, scissors, Shoot!')
  computer = random.choice(rps)
  ###user's answer is rock
  if answer == 'rock':
    if computer == 'rock':
      results = print('%s vs. %s: tie' % (answer, computer))
    elif computer == 'paper':
      results = print('%s vs. %s: you win' % (answer, computer))
    elif computer == 'scissors':
      results = print('%s vs. %s: you lose' % (answer, computer))
  ###user's answer is paper
  elif answer == 'paper':
    if computer == 'rock':
      results = print('%s vs. %s: you win' % (answer, computer))
    elif computer == 'paper':
      results = print('%s vs. %s: tie' % (answer, computer))
    elif computer == 'scissors':
      results = print('%s vs. %s: you lose' % (answer, computer))
  ###user's answer is scissors
  elif answer == 'scissors':
    if computer == 'rock':
      results = print('%s vs. %s: you lose' % (answer, computer))
    elif computer == 'paper':
     results = print('%s vs. %s: you win' % (answer, computer))
    elif computer == 'scissors':
     results = print('%s vs. %s: tie' % (answer, computer))
  ###quits rps_fnctn
  if input('play again?') == "yes":
    rps_fnctn()
  else:
    print('game over')
  
rps_fnctn()