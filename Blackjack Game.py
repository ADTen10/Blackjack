import new_deck
import deal_hands
import time
print("Welcome to Alyna's Blackjack!¯\_(ツ)_/¯")
time.sleep(2.5)
p1 = input("Player 1, what is your name?")
print("Good luck", p1, ",here we go...")
time.sleep(1.0)
d_start_hand=deal_hands.deal_dhand()
print ("Dealer's starting hand:", d_start_hand)
print ("Player 1's hand:",deal_hands.deal_phand())

def score(hand):
    pass
