import unittest
from War import Card


class TestCard(unittest.TestCase):
    def test_number_faces(self):
        for value in range(9):
            card = Card(value)
            self.assertEqual(card.faceValue, str(value + 2))

    def test_jack_face(self):
        card = Card(9)
        self.assertEqual(card.faceValue, "Jack")

    def test_queen_face(self):
        card = Card(10)
        self.assertEqual(card.faceValue, "Queen")

    def test_king_face(self):
        card = Card(11)
        self.assertEqual(card.faceValue, "King")

    def test_ace_face(self):
        card = Card(12)
        self.assertEqual(card.faceValue, "Ace")

    def test_card_creation_bounds(self):
        with self.assertRaises(ValueError):
            Card(-1)
        with self.assertRaises(ValueError):
            Card(13)


if __name__ == '__main__':
    unittest.main()
