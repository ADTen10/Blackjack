import new_deck

"""This function deals the player's first hand"""
def deal_phand():

    card1 = new_deck.hit()
    card2 = new_deck.hit()
    phand = [card1,card2]
    return phand

print ("Player's hand:",deal_phand())

"""This function deals 2 cards to the dealer, with only one shown"""
def deal_dhand():

    card = new_deck.hit()
    dhand = [card,'☺']
    return dhand

d_start_hand=deal_dhand()
print ("Dealers starting hand", d_start_hand)

"""This function reveals the delear's second card"""

def addcard_dhand(d_start_hand):
    #dhand = deal_dhand()
    d_start_hand.__delitem__(1)
    #print(d_start_hand)
    d_start_hand.append(new_deck.hit())
    return d_start_hand

dhand = (addcard_dhand(d_start_hand))
print("Dealers full hand",dhand)

"""This function reveals the score of the dealer's hand"""


#write a test for this
def score(dhand):
    total0=0
    for card in dhand:
        if card == int(card[0]):
            total0 += int(card[0])
        elif card == str(card[0]):

    return total0


print ("Dealer's score is",(score(dhand)))

