#!/usr/bin/env python3.8
import random
import time

start = input("Welcome to the game of Blackjack! \n\nPress Enter to start playing.\n")

while True:
  playerHand = []
  for i in range(2):
    playerHand.append(random.randint(2,11))
  print("Here is your hand: ")
  print(playerHand)

  continueGame = True

  if sum(playerHand) == 21:
    print("BlackJack! You Win!")
    continueGame = False

  if continueGame:
    hitOrStay = "H" 
    continueGame = True
    while hitOrStay == "H":
      while True:
        hitOrStay = input("Type Hit (H) or Stay (S): ")

        if hitOrStay == "H" or hitOrStay == "S":
          break
        else:
          print("Invalid Input /n")

      if hitOrStay == "H":
        playerHand.append(random.randint(2,11))
        print("Here is your hand: ")
        print(playerHand)
  
        if sum(playerHand) == 21:
          print("BlackJack! You Win!")
          continueGame = False
          break

        if sum(playerHand) > 21:
          print("You Busted!")
          continueGame = False
          break

    if continueGame:
      print("Dealer's Turn! \n")
      dealerHand = []
      for i in range(2):
        dealerHand.append(random.randint(2,11))
      print("This is the dealer's hand: ")
      print(dealerHand)

      while True:
        time.sleep(1)
        if sum(dealerHand) < 17:
          dealerHand.append(random.randint(2,11))
          print("The dealer hit. Here is the dealer's new hand: ")
          print(dealerHand)
        elif sum(dealerHand) > 21:
          print("Dealer Busted! You Win!")
          break
        elif sum(dealerHand) == 21:
          print("BlackJack! Dealer Wins!")
          break 
        else:
          print("The dealer has finalized his hand.")
          time.sleep(1)

          if sum(playerHand) > sum(dealerHand):
            print("You Win! \n")
          elif sum(dealerHand) > sum(playerHand):
            print("Dealer Wins! \n")
          else:
            print("Tie! \n")

          break
  input("Press enter to play again: ")