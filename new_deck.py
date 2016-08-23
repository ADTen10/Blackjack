import  random
def get_deck():
    deck = [value + suit for value in "23456789TJQKA" for suit in "♠♥♦♣"]
    random.shuffle(deck)
    return deck

def hit ():
    card = iter(get_deck())
    (print(next(card)))
    return card
hit()

#set up a git repository
