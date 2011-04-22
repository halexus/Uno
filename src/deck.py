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

import random
import color
from card import Card

class Deck:
    """Deck of cards."""
    def __init__(self, discardPile, cards = []):
        """Build a deck with given cards or build the start
        deck of 108 cards when no cards argument is given"""
        self.discardPile = discardPile
        self.deck = cards[:]
        if self.deck == []: #No cards argument was given
            for col in range(4): #Blue, Green, Red, Yellow
                for val in range(Card.MAXVALUE+1):
                    if val == 0: #The zeros are only once in deck
                        self.addCard(col, val, 1)
                    else: #All other color cards are twice in the deck
                        self.addCard(col, val, 2)
            self.addSpecialCards() #Add black cards (color change and draw 4)
        self.removeWrongCards()
        self.shuffle()
        
    def addCard(self, col, val, amount = 1):
        """Add a card with color col and value val amount times into deck."""
        for i in range(amount):
            self.deck.append(Card(col, val))

    def addSpecialCards(self):
        """Add 8 black special cards (change color and draw 4) to deck."""
        self.addCard(color.BLACK, Card.WILD, 4)
        self.addCard(color.BLACK, Card.WILDDRAW4, 4)
        
    def removeWrongCards(self):
        """Remove the colored wild and wild draw 4 cards in deck"""
        toDelete = []
        deleted = 0
        for i,c in enumerate(self.deck):
            if c.getColor() != color.BLACK and c.getValue() >= Card.WILD:
                toDelete.append(i-deleted)
                deleted += 1
        for i in toDelete:
            del self.deck[i]
        
                

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.deck)
        
    def makeNewDeck(self):
        wholeDiscardPile = self.discardPile.getWholePile()
        cardsToMakeNewDeck = wholeDiscardPile[:-1] #The upper card stays at discard pile
        self.discardPile.resetPile()
        self.__init__(self.discardPile, cardsToMakeNewDeck)
        #newDeck = Deck(self.discardPile, cardsToMakeNewDeck)
        #self = newDeck

    def drawCard(self, amount = 1):
        #if amount == 1:
        #    return self.deck.pop()
        cards=[]
        for i in range(amount):
            if self.hasNoCards(): #If no cards to draw make deck from discard pile
                self.makeNewDeck()
            try:
                cards.append(self.deck.pop())
            except IndexError: #Should not happen
                print("Can't draw card from empty deck")              
        return cards

    def noOfCards(self):
        return len(self.deck)

    def hasNoCards(self):
        return self.noOfCards() == 0
    
    def __str__(self):
        strdeck=[str(card) for card in self.deck]
        return ','.join(strdeck)


if __name__ == '__main__': #Test
    deck = Deck([])
    assert deck.noOfCards() == 108
    print(deck)
    card = deck.drawCard()
    print(card[0])
    assert deck.noOfCards() == 107
    deck.drawCard(7)
    assert deck.noOfCards() == 100
    deck.drawCard(99)
    deck=Deck([], [Card(color.BLUE, 1), Card(color.RED, 2),
               Card(color.YELLOW, 7), Card(color.GREEN, 9)])
    print(deck)
    print(deck.noOfCards())
    
    deck=Deck([], [Card(color.BLUE, Card.WILD), Card(color.RED, Card.WILDDRAW4),
               Card(color.YELLOW, Card.WILDDRAW4), Card(color.GREEN, Card.WILD)])
    assert deck.noOfCards() == 0
    
    from discardpile import Discardpile
    from player import Player
    d=Discardpile()
    deck = Deck(d)
    p = Player(0,deck,"TEST")
    d.putCard(Card(color.RED,4), p)
    d.putCard(Card(color.BLUE,7), p)
    d.putCard(Card(color.BLACK, 14), p)
    d.putCard(Card(color.GREEN,0), p)
    print("pile",d)
    deck = Deck(d,[Card(color.BLUE, 1), Card(color.RED, 2),
               Card(color.YELLOW, 7)])
    print("new",deck)
    deck.drawCard()
    print(deck)
    deck.drawCard()
    print(deck)
    deck.drawCard()
    print(deck)
    deck.drawCard()
    print(deck)
    deck.drawCard()
