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
import colorama

class Card:
    """Data structure for one card in the game."""
    MAXVALUE = 12 #10-12 are the actioncards with color
    DRAW2 = 10
    REVERSE = 11
    SKIP = 12
    """When a black action card is played the player must choose a color.
    On top of the black card the program puts a card with chosen color
    and the respective following value. When shuffling the discard pile
    into new deck we must pay attention to remove "fake" colored cards."""
    WILD = 13
    WILDDRAW4 = 14
    
    def __init__(self, col = None, val = None):
        self.col = col #Color of card
        self.val = val #Value of card (0-12). 10-12 are colored actioncards. 
                       #10->+2, 11->reverse, 12->skip
        self.actionHappened = False #A action card should act on ONLY one player
        #If card is black (special card) val=13 means change color, val=14 means +4
        
    def didActionHappen(self):
        return self.actionHappened
    
    def actionHappens(self):
        self.actionHappened = True
        
    def getColor(self):
        return self.col

    def getValue(self):
        return self.val

    def setColor(self, col):
        self.col = col

    def setValue(self, val):
        if val > Card.MAXVALUE+2:
            raise ValueError('Value must be in range 0-%d!' % Card.MAXVALUE+2)
        else:
            self.val = val
    
    def isSpecial(self):
        return self.val >= 10
    
    def isReverse(self):
        return self.val == Card.REVERSE
    
    def isSkip(self):
        return self.val == Card.SKIP
    
    def isDraw2(self):
        return self.val == Card.DRAW2
    
    def isDraw4(self):
        return self.val == Card.WILDDRAW4

    def __str__(self):
        colStr = color.toString(self.col)
        value = self.val
        if self.val == Card.WILD:
            value = '(Wild)'
        elif self.val == Card.WILDDRAW4:
            value = '(Wild draw 4)'
        elif self.val == Card.DRAW2:
            value = '+2'
        elif self.val == Card.REVERSE:
            value = 'reverse'
        elif self.val == Card.SKIP:
            value = "skip"
        return '%s %s%s%s' % (colStr, value, colorama.Style.DIM, colorama.Fore.BLACK)
    
    def allowedOn(self, other):
        """Is card self allowed to be put on card
        other in discard pile."""
        if self.col == color.BLACK: #Black card allowed on every other card
            return True
        elif self.col == other.getColor(): #Same color -> allowed
            return True
        elif self.val == other.getValue(): #Same value -> allowed
            return True
        else:
            return False
    
if __name__ == '__main__': #Test
    print(Card(color.GREEN, 9))
    print(Card(color.BLACK, 1))
    print(Card(color.RED, 0))
    print(Card(color.YELLOW, 6))
    assert str(Card(color.BLACK, Card.WILD)) == 'wild'
    assert str(Card(color.BLACK, Card.WILDDRAW4)) == 'wild draw 4'
    assert str(Card(color.BLUE, Card.DRAW2)) == 'Blue draw 2'