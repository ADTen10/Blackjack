import new_deck


"""This function reveals the score of the a hand"""

#write a test for this
def score(hand):
    total0=0
    for card in hand:

        if (card[0]) in ('T','J','Q','K'):
            total0 += 10

        elif (card[0]) == 'A':
            total0 += 11

        elif (card[0]) not in ('T','J','Q','K'):
                total0 += int(card[0])

    return total0

"""This function deals the player's first hand"""
def deal_phand():

    card1 = new_deck.hit()
    card2 = new_deck.hit()
    phand = [card1,card2]
    return phand


p_start_hand = deal_phand()
print ("Player's starting hand:",p_start_hand)


""" This will deal the player a new card for their hand"""

def add_card_phand():
   p_start_hand.append(new_deck.hit())
   return p_start_hand

p_hand_hit1 = add_card_phand()

print ("player's hand with 1 new card", p_hand_hit1)

"""this adds up the players hand"""
print("This is the player's score after a new card:", score(p_hand_hit1))


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





print ("Dealer's score is",(score(dhand)))



