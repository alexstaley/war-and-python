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
        hand1.append(2)  # hand2 stays empty

        hand1, hand2 = takeATurn(hand1, hand2, 'A')

        self.assertIn(2, hand1)
        self.assertIsNone(hand2)

    def test_winner_gets_cards(self):
        # Tests that the cards in a regular hand go to the winner
        hand1 = co.deque()
        hand2 = co.deque()
        hand1.append(1)
        hand2.append(2)

        hand1, hand2 = takeATurn(hand1, hand2, 'A')

        self.assertIn(1, hand2)
        self.assertIn(2, hand2)
        self.assertNotIn(1, hand1)

    def test_expected_hand_lengths(self):
        # Tests that a regular hand leaves both players with the expected number of cards
        hand1 = co.deque()
        hand2 = co.deque()
        hand1.append(1)
        hand2.append(2)
        for _ in range(25):
            hand1.append(0)
            hand2.append(0)

        hand1, hand2 = takeATurn(hand1, hand2, 'A')

        self.assertEqual(len(hand1), 25)
        self.assertEqual(len(hand2), 27)


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
        table = [5, 5]  # Matching 5s ('7's) start a war

        hand1, hand2, table = makeWar(hand1, hand2, table, 'A')

        self.assertIsNone(table)

    def test_not_enough_cards_for_war(self):
        # Tests that a player running out of cards at all mid-war points ends the game gracefully
        for cards in range(4):
            hand1 = co.deque()
            hand2 = co.deque()
            for _ in range(cards):
                hand1.append(0)
                hand2.append(0)
            hand1.append(1)
            hand1.append(2)
            hand1.append(3)
            hand1.append(4)
            table = [5, 5]

            hand1, hand2, table = makeWar(hand1, hand2, table, 'A')

            self.assertIsNone(hand2)  # hand2 == None -> hand1 wins the game
            self.assertIsNotNone(hand1)

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

        hand1, hand2, table = makeWar(hand1, hand2, table, 'A')

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

        hand1, hand2, table = makeWar(hand1, hand2, table, 'A')

        self.assertEqual(len(hand1), 0)

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

        hand1, hand2, table = makeWar(hand1, hand2, table, 'A')

        self.assertEqual(len(hand2), 18)

    def test_human_wins_seven_war_marathon(self):
        # Tests that rare seven-war case that puts all cards on the table leads to a human win
        handHuman = co.deque()
        hand2 = co.deque()
        for _ in range(25):
            handHuman.append(0)
            hand2.append(0)
        table = [5, 5]

        handHuman, hand2, table = makeWar(handHuman, hand2, table, 'A')  # First argument == user's hand

        self.assertIsNotNone(handHuman)
        self.assertIsNone(hand2)


if __name__ == '__main__':
    unittest.main()
