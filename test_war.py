import unittest
from War import deal, show


class TestDeal(unittest.TestCase):
    def test_even_deal(self):
        deck1, deck2 = deal()
        self.assertEqual(len(deck1), len(deck2))

    def test_complete_deal(self):
        deck1, deck2 = deal()
        for val in range(12):
            self.assertEqual(deck1.count(val) + deck2.count(val), 4)


class TestShowCard(unittest.TestCase):
    def test_card_creation_bounds(self):
        with self.assertRaises(ValueError):
            show(-1)
        with self.assertRaises(ValueError):
            show(13)

    def test_number_cards(self):
        for value in range(9):
            self.assertEqual(show(value), str(value + 2))

    def test_show_jack(self):
        self.assertEqual(show(9), "Jack")

    def test_show_queen(self):
        self.assertEqual(show(10), "Queen")

    def test_show_king(self):
        self.assertEqual(show(11), "King")

    def test_show_ace(self):
        self.assertEqual(show(12), "Ace")


if __name__ == '__main__':
    unittest.main()
