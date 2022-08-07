import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):


    def setUp(self):
        self.card1 = Card('spade', 6)
        self.card2 = Card('heart', 2)
        self.card3 = Card('diamond', 8)
        self.card4 = Card('club', 1)
        self.card_game = CardGame()

        self.allcards = [self.card1, self.card2, self.card3, self.card4]

    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card42))


    def test_highest_card(self):
        self.assertEqual(self.card3, self.card_game.highest_card(self.card4, self.card3))

    def test_cards_total(self):
        self.assertEqual(17, self.card_game.cards_total(self.allcards))


