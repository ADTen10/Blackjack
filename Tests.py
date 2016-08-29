from deal_hands import score
from nose.tools import assert_equal

"""testing the scoring function"""

def test_score_2_Aces():
    hand=['A♠','A♠']
    result=score(hand)
    assert_equal(result,12)

def test_score_3_Aces():
    hand=['A♠','A♠','A♠']
    result = score(hand)
    assert_equal (result,13)

def test_score_ace_and_kings():
    hand=['A♠','K♠', 'K♠']
    result=score(hand)
    assert_equal(result,21)


""" Testing whether player can accept a new card to their hand"""


def test_ask_player_for_move():
    phand = ['3♦','7♦']
    hit = 'y'
    phand_with_new_card = ['3♦', '7♦', '3♦']
    assert_equal(hit,phand_with_new_card)