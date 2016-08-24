import  random
def get_deck():
    deck = [value + suit for value in "23456789TJQKA" for suit in "♠♥♦♣"]
    random.shuffle(deck)
    return deck

def hit ():
    card = iter(get_deck())
    #(print(next(card)))
    return next(card)

"""This is the dictionary that contains the values for all cards with a value of 10"""
ten_points=({T,10}, {J,10}, {Q,10}, {K,10}, {A,11})



