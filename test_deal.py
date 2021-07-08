import unittest
from War import deal


class TestDeal(unittest.TestCase):
    def test_even_deal(self):
        deck1, deck2 = deal()
        self.assertEqual(len(deck1), len(deck2))

    def test_complete_deal(self):
        deck1, deck2 = deal()
        for val in range(12):
            self.assertEqual(deck1.count(val) + deck2.count(val), 4)


if __name__ == '__main__':
    unittest.main()
