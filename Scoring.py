import new_deck

def deal_phand():

    card1 = new_deck.hit()
    card2 = new_deck.hit()
    phand = [card1,card2]
    return phand

print ("Player's hand:",deal_phand())

def deal_dhand():

    card = new_deck.hit()
    dhand = [card,'☺']
    return dhand

print ("Dealer's hand",deal_dhand())

#def score_hand(cards)


#store hand in a list

#arrange
#hand = [card1, card2, card3]
#act

#assert
#score =