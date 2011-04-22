from player import Player

def getNoOfPlayers():
    noOfPlayers = 0
    while noOfPlayers == 0:
        try:
            noOfPlayers = int(input("How many KI players? "))
            if noOfPlayers > 10 or noOfPlayers < 1:
                print("Number of players must be 1-10")
                noOfPlayers = 0 
        except ValueError:
            print('Number of players must be 1-10')
    return noOfPlayers

def makePlayers(noOfPlayers, startWithId, deck):
    players=[]
    for i in range(noOfPlayers):
        players.append(KiPlayer(startWithId + i, deck))
        players[i].setName('KI #%d' % (i + 1))
    return players

class KiPlayer(Player):
    
    
    def isKi(self):
        return True
    
    def playCard(self, onOtherCard, deck):
        """Begin with last card in hand."""
        for index in range(self.noOfCardsInHand()-1, -1, -1): #loop down to 0
            cardToPlay = self.hand.playCard(index, keepInHand = True)
            if cardToPlay.allowedOn(onOtherCard):
                return self.hand.playCard(index)
        self.drawCards(deck, 1)
        return None
    
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
                    
       #print(self) #Show the current player's hand #DEBUG

        cardToPlay = self.playCard(topCard, deck) #Play a card that's allowed on
                                                  #discard pile or draw a card
        return cardToPlay #Play a card
            