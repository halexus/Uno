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

class Hand:
    def __init__(self, deck):
        self.cards = deck.drawCard(7) #Hand starts with 7 cards
        
    def noOfCardsInHand(self):
        return len(self.cards)
    
    def playCard(self, i, keepInHand = False):
        if not keepInHand:
            return self.cards.pop(i)
        else:
            return self.cards[i]
        
    def addCard(self, card):
        self.cards.append(card)

    def __str__(self):
        #cardsStr = [str(card) for card in self.cards]
        cardsStr = ['%2d: %s' % ( index + 1, card) for index, card in enumerate(self.cards)]
        #return ', '.join(cardsStr) 
        return '\n'.join(cardsStr)
        
