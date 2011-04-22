#TODO: KI
"""
Uno: A clone of the cardgame UNO (C)
Copyright (C) 2011  Alexander Thaller <alex.t@gmx.at>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from random import randint
import os
import colorama
from deck import Deck
from discardpile import Discardpile
import player
import kiplayer

def nextId(currentId, noOfPlayers, isClockwise = True):
    if isClockwise: #Direction of play can be changed by reverse card
        return (currentId + 1) % noOfPlayers
    else:
        return (currentId - 1) % noOfPlayers
    
def clear_screen():
    """OS independent version to clear the cmd or shell window"""
    if os.name == 'posix':
        os.system("clear")
    elif os.name == 'nt':
        os.system("cls")
        
def printCopyright():
    copy = """
    Uno  Copyright (C) 2011  Alexander Thaller
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions; See LICENSE.txt for details
    """
    print(copy)
    print()
    
def makePlayers(deck):
    noOfHumanPlayers = player.getNoOfPlayers() #How many human players?
    noOfKiPlayers = kiplayer.getNoOfPlayers() #How many KI players?
    players = player.makePlayers(noOfHumanPlayers, deck) #Initialize players with deck
    players = players + kiplayer.makePlayers(noOfKiPlayers, noOfHumanPlayers, deck)
    return players

def showNoOfCardsInHand(players, idCurrentPlayer):
    for player in players:
        if player.getId() == idCurrentPlayer:
            continue
        cardsInHand = player.getHand().noOfCardsInHand()
        print('%s has %d cards' % (player.getName(), cardsInHand), end='; ')
    print()

if __name__ == '__main__':
    colorama.init() #Initialize color output
    print(colorama.Back.WHITE + colorama.Fore.BLACK) #Background white, textcolor black
    clear_screen() #To make background white
    printCopyright()
    discardPile = Discardpile() #Build the initial (empty) discard pile
    deck = Deck(discardPile) #Build a deck with 108 cards   
    players = makePlayers(deck) #Initialize players with deck
    noOfPlayers = len(players)
    idCurrentPlayer = randint(0, noOfPlayers-1) #ID of first player in first round  
    discardPile.putCard(deck.drawCard()[0], players[idCurrentPlayer]) #Put first card at discard pile
    isClockwise = True #Direction of play. Can be changed by reverse card
    while True: #Game loop
        clear_screen()
        topCard = discardPile.getCardOnTop()
        currentPlayer = players[idCurrentPlayer]
        showNoOfCardsInHand(players, idCurrentPlayer) #Print how many cards the other players have
        print('Pile: %s\n' % topCard) #Show top card on discard pile
        cardToPlay = currentPlayer.takeTurn(deck, topCard, noOfPlayers)          
        if cardToPlay == None: #It's None if a card was drawn
            print('%s draws a card.' % currentPlayer.getName())
        elif cardToPlay == 'skip': #It's 'skip' if player's turn is skipped
            print("%s's turn is skipped." % currentPlayer.getName())
        else: #A card was chosen to play
            discardPile.putCard(cardToPlay, currentPlayer) #Put played card on pile
            if cardToPlay.isReverse(): #Did player play a reverse card?
                isClockwise = not isClockwise #Order of play reversed
        if currentPlayer.isWinner():
            print('%s wins the game!' % currentPlayer.getName())
            break
        idCurrentPlayer = nextId(currentPlayer.getId(), noOfPlayers, isClockwise) #Id of next player
    input()
    
    