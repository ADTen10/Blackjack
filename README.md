# Blackjack
The code for this game can be found at: https://github.com/ADTen10/Blackjack

W**hat do the different files do?:**

Tests.py
Contains the nosetests used to check the games functionality 

deal_hands.py:
This file has all the separate functions of the game

BlackJack Game.py
The script for playing the game lives here. 

new_deck.py
Contains the deck function and function to 'hit' a new card.


**How to run the game:**
Right click the BlackJack.py file in PyCharm and click 'Run Blackjack Game'

**Have all the requirements been met?**
No!

Requirements:
The game should recognise an ace as high or low depending on what is 
best for the player; 
_As shown in the nosetests,the game is able to adjust scoring for an Ace
in a hand that scores over 21. This only works for the first ace, so if
there are more than two aces, only the first is treated as a 1._

The house should be an automated player but other players, up to 4, 
should be humans operating a command line interface;
_The house is an automated player however the game only accepts 1 player
at the moment. Additional players could perhaps be added by placing all 
the player functions in one for loop_

The house should win all ties;
_This doesn't work yet_

It is possible for more than one player to win a hand;
_This definitely doesn't exist_

Must be able to stick and twist
_This works!_

Must have an autonomous dealer
_This also works!!_

Dealer starts by showing only a single card
_Yep!_

All Players are dealt two cards to start
_YES!!!_

Extra marks will be awarded for tests, good function/variable names, 
sensible comments/docstrings, clean Pythonic code
_My naming is a little bit confusing, sorry. Not sure how clean the code
 is either._
 
 **Known Bugs**
    - Play script is incomplete (Blackjack Game.py)
    - Score comparison is incomplete (def compare_dealer_and_player_scores)
    - Scoring for a hand with more than one ace does not work as it should
    