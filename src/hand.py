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

import color

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
        
    def mostFrequentColor(self):
        freq={color.BLUE: 0, color.GREEN: 0, color.RED: 0, color.YELLOW: 0}
        for card in self.cards:
            if card.getColor() != color.BLACK:
                freq[card.getColor()] += 1
        freqView = freq.items()
        freqView = sorted(freqView, key = lambda x: x[1])
        return freqView[-1][0]

    def __str__(self):
        #cardsStr = [str(card) for card in self.cards]
        cardsStr = ['%2d: %s' % ( index + 1, card) for index, card in enumerate(self.cards)]
        #return ', '.join(cardsStr) 
        return '\n'.join(cardsStr)
    
if __name__ == '__main__': #TEST
    from discardpile import Discardpile
    from deck import Deck
    discardPile = Discardpile() #Build the initial (empty) discard pile
    deck = Deck(discardPile) #Build a deck with 108 cards
    h = Hand(deck)
    print(h)
    print(color.toString(h.mostFrequentColor()))
        
