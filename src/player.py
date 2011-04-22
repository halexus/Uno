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

from hand import Hand

def getNoOfPlayers():
    noOfPlayers = 0
    while noOfPlayers == 0:
        try:
            noOfPlayers = int(input("How many human players? "))
            if noOfPlayers > 10 or noOfPlayers < 1:
                print("Number of players must be 1-10")
                noOfPlayers = 0 
        except ValueError:
            print('Number of players must be 1-10')
    return noOfPlayers

def askForName(no):
    name = ""
    while name == "":
        name = input("Name of Player %d: " % no).strip()
    return name

def makePlayers(noOfPlayers, deck):
    players=[]
    for i in range(noOfPlayers):
        players.append(Player(i, deck))
        players[i].setName(askForName(i + 1))
    return players
        

class Player:
    def __init__(self, id, deck, name = ""):
        self.name = name
        self.id = id
        self.hand = Hand(deck) #Every player has a hand of cards drawn from deck

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getHand(self):
        return self.hand
    
    def noOfCardsInHand(self):
        return self.hand.noOfCardsInHand()
    
    def askForCardToPlay(self):
        """Input 0 to draw a card."""
        playCardWithIndex = None
        while playCardWithIndex == None:           
            try:
                playCardWithIndex = int(input("Play Card: ")) - 1 #-1 because we want index starting with 0
                if playCardWithIndex >= self.noOfCardsInHand() or playCardWithIndex < -1:
                    print("Wrong number of card!")
                    playCardWithIndex = None 
            except ValueError:
                print('Wrong number of card!')
        return playCardWithIndex
    
    def playCard(self, onOtherCard, deck):
        index = self.askForCardToPlay()
        if index == -1:
            self.drawCards(deck, 1)
            return None
        else:
            cardToPlay = self.hand.playCard(index, keepInHand = True)
            while not cardToPlay.allowedOn(onOtherCard):
                print('Card not allowed')
                index = self.askForCardToPlay()
                if index == -1:
                    self.drawCards(deck, 1)
                    return None
                cardToPlay = self.hand.playCard(index, keepInHand = True)
            return self.hand.playCard(index)
    
    def drawCards(self, deck, amount):
        for card in deck.drawCard(amount):
                self.hand.addCard(card)
    
    def takeTurn(self, deck, topCard, noOfPlayers):
        if topCard.isSpecial():
            if not topCard.didActionHappen(): #Did action already act on a player
                topCard.actionHappens() #Let action happen
                if topCard.isSkip():
                    return 'skip'
                elif topCard.isDraw2():            
                    self.drawCards(deck, 2)
                elif topCard.isDraw4():
                    self.drawCards(deck, 4)
                    return 'skip'
                elif topCard.isReverse(): 
                    if noOfPlayers == 2: #Skip next player if 2 players and reverse card is played
                        return 'skip'
                
        print(self) #Show the current player's hand
        cardToPlay = self.playCard(topCard, deck) #Play a card that's allowed on
                                                  #discard pile or draw a card
        return cardToPlay #Play a card
    
    def isWinner(self):
        if self.hand.noOfCardsInHand() == 0:
            return True
        else:
            return False
        
    def isKi(self):
        return False

    def __str__(self):
        return '%s\n%s' % (self.getName(), self.getHand())

    
