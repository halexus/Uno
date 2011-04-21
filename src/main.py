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

def playARound(players, startWithId, deck, discardPile):
    """Deprecated!!!"""
    noOfPlayers = len(players)
    def currentPlayer(i):
        return players[(i+startWithId) % noOfPlayers]
    if startWithId > noOfPlayers -1:
        raise ValueError('No player with given ID')
    for i in range(noOfPlayers):
        if not deck.hasCards():
            deck = Deck(discardPile.getWholePile()) #If deck is empty shuffle discard pile into new deck
        print('Pile: %s' % discardPile.getCardOnTop()) #Print top card of discard pile
        currPlayer = currentPlayer(i)
        print(currPlayer) #Show the current player's hand
        cardToPlay = currPlayer.playCard(discardPile.getCardOnTop(), deck) #Play a card that's allowed on discard pile
        if cardToPlay != None: #It's None when a card was drawn
            discardPile.putCard(cardToPlay) #Play a card and put it on discard pile
        
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

if __name__ == '__main__':
    colorama.init() #Initialize color output
    print(colorama.Back.WHITE + colorama.Fore.BLACK) #Background white, textcolor black
    clear_screen() #To make background white
    printCopyright()
    discardPile = Discardpile() #Build the initial (empty) discard pile
    deck = Deck(discardPile) #Build a deck with 108 cards   
    noOfPlayers = player.getNoOfPlayers() #How many players?
    players = player.makePlayers(noOfPlayers, deck) #Initialize players with deck    
    discardPile.putCard(deck.drawCard()[0]) #Put first card at discard pile
    idCurrentPlayer = randint(0, noOfPlayers-1) #ID of first player in first round
    isClockwise = True #Direction of play. Can be changed by reverse card
    while True: #Game loop
        clear_screen()
        topCard = discardPile.getCardOnTop()
        currentPlayer = players[idCurrentPlayer]
        print('Pile: %s\n' % topCard) #Show top card on discard pile
        cardToPlay = currentPlayer.takeTurn(deck, topCard, noOfPlayers)          
        if cardToPlay == None: #It's None if a card was drawn
            print('%s draws a card.' % currentPlayer.getName())
        elif cardToPlay == 'skip': #It's 'skip' if player's turn is skipped
            print("%s's turn is skipped." % currentPlayer.getName())
        else: #A card was chosen to play
            discardPile.putCard(cardToPlay) #Put played card on pile
            if cardToPlay.isReverse(): #Did player play a reverse card?
                isClockwise = not isClockwise #Order of play reversed
        if currentPlayer.isWinner():
            print('%s wins the game!' % currentPlayer.getName())
            break
        idCurrentPlayer = nextId(currentPlayer.getId(), noOfPlayers, isClockwise) #Id of next player   
    
    