import new_deck

def score(hand):
    """This function reveals the score of a hand"""
    total_0=0

    for card in hand:

        if (card[0]) in ('T','J','Q','K'):
            total_0 += 10

        elif (card[0]) == 'A':
            total_0 += 11

        elif (card[0]) not in ('T','J','Q','K'):
                total_0 += int(card[0])


    for card in hand:
        if total_0 > 21 and (card[0]) == 'A':
            total_0 -= 10

    return total_0


def deal_phand():
    """This function deals the player's starting hand"""
    card1 = new_deck.hit()
    card2 = new_deck.hit()
    phand = [card1,card2]
    return phand


p_start_hand = deal_phand()


def add_card_phand(p_start_hand):
    """ This will deal the player a new card for their hand"""
    p_start_hand.append(new_deck.hit())
    return p_start_hand

def ask_player_for_hit(p1,phand):
    """
    this adds a new card to the players hand
    """
    print(p1, "Your score is", (score(phand)))
    hit=input ("\nWould you like another card? y/n")
    if hit == 'y':
        phand.append(new_deck.hit())
        print (p1, "Your hand is now", phand,"\nyour cards add up to", score(phand))
        return phand
    elif hit == 'n':
        print(p1,"has stuck on", (score(phand)))

def compare_dealer_and_player_scores(p1,phand,dhand):
    """
    compares the score of the players hand and the dealers hand and decides who has won
    """

    if score(phand) == 21:
        print(p1, "you have scored 21, you win!!(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
    elif score(dhand) == 21:
        print ("Dealer has a score of 21 and wins. Sorry! ¯\_(ツ)_/¯")
    elif score(phand)>21 == score(dhand)<21:
        print ("Dealer wins this round. Better luck next time ¯\_(ツ)_/¯")
    elif score(dhand)>21 == score(phand)<21:
        print(p1, "you have scored 21, you win!!(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")



def deal_dhand():
    """This function deals 2 cards to the dealer, with only one shown"""
    card = new_deck.hit()
    dhand = [card,'☺']
    return dhand

d_start_hand=deal_dhand()
print ("Dealers starting hand", d_start_hand)


def addcard_dhand(d_start_hand):
    """This function reveals the delear's second card by deleting the smiley face (which represents a face down card)
    from the list and replaces it with a new card from the deck"""
    #dhand = deal_dhand()
    d_start_hand.__delitem__(1)
    #print(d_start_hand)
    d_start_hand.append(new_deck.hit())
    return d_start_hand

dhand = (addcard_dhand(d_start_hand))
print("Dealers full hand",dhand)
print ("Dealer's score is",(score(dhand)))


def dhand_newcard(dhand):
    """ This decides whether the dealer wants a new hand, scores the new hand and decides if bust. describe input and output"""


    while (score(dhand)) < 17:
        dhand.append(new_deck.hit())
        print("Dealer's new hand is:", dhand, "\nDealer's new score is:", score(dhand))

    if (score(dhand)) >= 17 and (score(dhand)) < 21:
        print("Dealer's final score is:", score(dhand), "\nDealer has stuck")
        return dhand

    elif (score(dhand)) > 21:
        print("Dealer's score is:", score(dhand), "\nDealer is bust")
        return dhand


dhand2 = dhand_newcard(dhand)


#print ("Dealer's hand:",dhand2)
#print ("Dealer's new score is",(score(dhand2)))



