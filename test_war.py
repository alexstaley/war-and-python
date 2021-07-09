import unittest
import collections as co
from War import deal, show, takeATurn, makeWar


class TestDeal(unittest.TestCase):
    def test_even_deal(self):
        # Tests that an equal number of cards have been dealt to each player
        deck1, deck2 = deal()
        self.assertEqual(len(deck1), len(deck2))

    def test_complete_deal(self):
        # Tests that all four cards of each rank have been dealt
        deck1, deck2 = deal()
        for val in range(12):
            self.assertEqual(deck1.count(val) + deck2.count(val), 4)


class TestShowCard(unittest.TestCase):
    def test_card_creation_bounds(self):
        # Tests that showing a nonexistent card raises a ValueError
        with self.assertRaises(ValueError):
            show(-1)
        with self.assertRaises(ValueError):
            show(13)

    def test_number_cards(self):
        # Tests that number-valued cards are shown as expected
        for value in range(9):
            self.assertEqual(show(value), str(value + 2))

    # Tests that face cards and aces are shown as expected
    def test_show_jack(self):
        self.assertEqual(show(9), "Jack")

    def test_show_queen(self):
        self.assertEqual(show(10), "Queen")

    def test_show_king(self):
        self.assertEqual(show(11), "King")

    def test_show_ace(self):
        self.assertEqual(show(12), "Ace")


class TestTakeATurn(unittest.TestCase):
    def test_drawing_from_empty_hand(self):
        # Tests that attempting to draw from an empty hand exits the function as expected
        hand1 = co.deque()
        hand2 = co.deque()
        hand1.append(1)
        hand1.append(2)

        hand1, hand2 = takeATurn(hand1, hand2)

        self.assertIn(2, hand1)
        self.assertFalse(hand2)

    def test_winner_gets_cards(self):
        # Tests that the cards in a regular hand go to the winner
        hand1 = co.deque()
        hand2 = co.deque()
        hand1.append(1)
        hand2.append(2)

        hand1, hand2 = takeATurn(hand1, hand2)

        self.assertFalse(hand1)
        self.assertIn(1, hand2)
        self.assertIn(2, hand2)


class TestMakeWar(unittest.TestCase):
    def test_table_empty_after_war(self):
        # Tests that all cards are picked up after a war
        hand1 = co.deque()
        hand2 = co.deque()
        for _ in range(3):
            hand1.append(0)
            hand2.append(0)
        hand1.append(1)
        hand2.append(2)
        table = [5, 5]

        hand1, hand2, table = makeWar(hand1, hand2, table)

        self.assertIsNone(table)

    def test_multiple_wars_take_table(self):
        # Tests that serial wars leave the table empty
        hand1 = co.deque()
        hand2 = co.deque()
        for _ in range(7):
            hand1.append(0)
            hand2.append(0)
        hand1.append(1)
        hand2.append(2)
        table = [5, 5]

        hand1, hand2, table = makeWar(hand1, hand2, table)

        self.assertIsNone(table)

    def test_multiple_wars_empty_losing_hand(self):
        # Tests that serial wars leave the losing player with no unexpected cards
        hand1 = co.deque()
        hand2 = co.deque()
        for _ in range(7):
            hand1.append(0)
            hand2.append(0)
        hand1.append(1)
        hand2.append(2)
        table = [5, 5]

        hand1, hand2, table = makeWar(hand1, hand2, table)

        self.assertFalse(hand1)

    def test_multiple_wars_cards_go_to_winner(self):
        # Tests that serial wars leave the winner with the expected number of cards
        hand1 = co.deque()
        hand2 = co.deque()
        for _ in range(7):
            hand1.append(0)
            hand2.append(0)
        hand1.append(1)
        hand2.append(2)
        table = [5, 5]

        hand1, hand2, table = makeWar(hand1, hand2, table)

        self.assertEqual(len(hand2), 18)


if __name__ == '__main__':
    unittest.main()
