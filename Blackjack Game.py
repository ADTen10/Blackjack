import new_deck
import deal_hands
import time
print("            ∩︵∩                         ωєℓ¢σмє тσ αℓуиα'ѕ                        ∩︵∩ ")
print("           ( ╹◡╹ )凸     0 • º ° ´¨`-:¦:- B L A C K J A C K -:¦:- ´¨` ° º • 0    凸( ╹◡╹ )   \n")

#(◡‿◡✿)


time.sleep(2.5)
p1 = input("Player 1, what is your name?")
print("Good luck",p1,"here we go...\n")
time.sleep(1.0)
d_start_hand=deal_hands.deal_dhand()
print ("Dealer's starting hand:", d_start_hand)
p_hand = deal_hands.p_start_hand
print (p1,"'s hand:",p_hand)
print ("Your score is",deal_hands.score(p_hand))

d_hand = deal_hands.addcard_dhand(d_start_hand)
print("\nDealers full hand is",d_hand)
print ("Dealer's score is:", deal_hands.score(d_hand))
compare_scores=deal_hands.compare_dealer_and_player_scores(p1, d_hand, p_hand)
print(compare_scores)
hit_or_stick = deal_hands.ask_player_for_hit(p1,p_hand)
print(hit_or_stick)

compare_scores=deal_hands.compare_dealer_and_player_scores(p1, d_hand, p_hand)

compare_scores()
hit_or_stick
