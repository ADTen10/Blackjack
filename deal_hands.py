import new_deck


"""This function reveals the score of a hand"""

#write a test for this
def score(hand):
    total_0=0

    for card in hand:

        if (card[0]) in ('T','J','Q','K'):
            total_0 += 10

        elif (card[0]) == 'A':
            total_0 += 11

        elif (card[0]) not in ('T','J','Q','K'):
                total_0 += int(card[0])
    return total_0


"""This function deals the player's starting hand"""
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

"""This decides whether the dealer wants a new hand, scores the new hand and decides if bust"""


def dhand_newcard (dhand):


    while (score(dhand)) <17:
                dhand.append(new_deck.hit())
                print ("Dealer's new hand is:", dhand,"\nDealer's new score is:", score(dhand))

    if (score(dhand)) > 21 == 'A' in dhand:
        (score(dhand)) - 10
        return dhand

    elif (score(dhand)) >21:
                print ("Dealer's score is:", score(dhand),"\nDealer is bust")
                return dhand

    elif (score(dhand)) == 17 or 18 or 19 or 20 or 21:
                print ("Dealer's final score is:", score(dhand), "\nDealer has stuck")
                return dhand








dhand2 = dhand_newcard(dhand)


#print ("Dealer's hand:",dhand2)
#print ("Dealer's new score is",(score(dhand2)))



