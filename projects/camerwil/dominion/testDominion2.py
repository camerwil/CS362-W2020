# -*- coding: utf-8 -*-
"""
Date: 1/19/2020
@author: William Cameron (camerwil)
Adapted from code provided in CS362
Assignment 2
"""

import Dominion
import random
from collections import defaultdict
import testUtility

# Get player names  (refactored)
player_names = testUtility.getPlayerNames()

# number of curses and victory cards (not refactoring in case I want to make changes here in the future)
if len(player_names) > 2:
    nV = 12
else:
    nV = 8
nC = -10 + 10 * len(player_names)

# Define box (refactored)

box = testUtility.CreateBoxes(nV)

# Supply order  (refactored)
supply_order = testUtility.setSupplyOrder()

# Pick 10 cards from box to be in the supply. (refactored)
supply = testUtility.pickCards(box)

# The supply always has these cards (refactored)
supply = testUtility.setSupply(supply, player_names, nC, nV)

# initialize the trash
trash = []

# Costruct the Player objects (refactored)
players = testUtility.players(player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)