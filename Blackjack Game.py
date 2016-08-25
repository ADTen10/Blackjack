import new_deck
import deal_hands
import time
print("            ∩︵∩                         ωєℓ¢σмє тσ αℓуиα'ѕ                        ∩︵∩ ")
print("           ( ╹◡╹ )凸     0 • º ° ´¨`-:¦:- B L A C K J A C K -:¦:- ´¨` ° º • 0    凸( ╹◡╹ )   \n")

#(◡‿◡✿)
#(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧

time.sleep(2.5)
p1 = input("ρℓą¥€я 1, ώhąţ ɨ$ ¥๏µя ɲąʍ€?")
print("Good luck",p1,"here we go...\n")
time.sleep(1.0)
d_start_hand=deal_hands.deal_dhand()
print ("Dealer's starting hand:", d_start_hand)
print (p1,"'s hand:",deal_hands.deal_phand())
hit = input("Do you want another card? y/n")
print ("Dealer's hand:", dhand)

dhand = (deal_hands.addcard_dhand(d_start_hand))

def score(hand):
    pass
