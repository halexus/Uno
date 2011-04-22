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
import color
import colorama
from card import Card

class Discardpile:
    def __init__(self):
        self.pile = []
    
    def putCard(self, card, player):
        self.pile.append(card)
        """If a black card was put on discard pile ask for new color
        and add a card with that color and respective value on pile"""
        if card.getColor() == color.BLACK:
            if not player.isKi(): #ki == False
                for i in range(4):
                    print('%d: %s%s%s' % (i + 1, color.toString(i), colorama.Fore.BLACK, colorama.Style.DIM))
                newColor = None
                while newColor == None:
                    try:
                        newColor = int(input('Choose Color: ')) - 1
                        if newColor not in range(4):
                            print('Number must be in range 1-4')
                            newColor = None 
                    except ValueError:
                        print('Number must be in range 1-4')
            else: #ki == True
                #newColor = randint(0,3)
                newColor = player.getHand().mostFrequentColor()
            card = Card(newColor, card.getValue())
            self.pile.append(card)
                
        
    def getWholePile(self):
        return self.pile
    
    def getCardOnTop(self):
        return self.pile[-1]
    
    def resetPile(self):
        oldTopCard = self.pile[-1]
        self.pile = [oldTopCard]
    
    def __str__(self):
        pileStr = [str(card) for card in self.pile]
        return ', '.join(pileStr)
    
if __name__ == '__main__': #Test
    from player import Player
    from deck import Deck
    pile = Discardpile()
    deck = Deck(pile)
    p = Player(0,deck,"TEST")
    pile.putCard(Card(color.RED, 4), p)
    print(pile)
    pile.putCard(Card(color.GREEN, 9), p)
    print(pile)
    pile.putCard(Card(color.RED, Card.REVERSE), p)
    print(pile)
    pile.putCard(Card(color.BLACK, Card.WILDDRAW4), p)
    print(pile)
    pile.resetPile()
    print(pile)