import random as rd
import collections as co


# TODO: refactor Card class... YAGNI?
class Card:
    """
    The Card class represents a single card. It has a numeric value [0-12]
    for use in comparison and a "face" value for use in text output.
        value: int, 0-12 inclusive
        faceValue: string, '2' - 'Ace'
    """
    def __init__(self, value):
        """
        Determine the face value from the given integer value.
        0 -> '2', 1 -> '3', 2 -> '4', ... 9 -> "Jack", 10 -> "Queen", ...
        :param value: int [0-12]
        """
        if value < 0 or value > 12:
            raise ValueError(f"value {value} must be between [0-12]")

        self.value = value
        if value == 9:
            self.faceValue = "Jack"
        elif value == 10:
            self.faceValue = "Queen"
        elif value == 11:
            self.faceValue = "King"
        elif value == 12:
            self.faceValue = "Ace"
        else:
            self.faceValue = str(value + 2)


def deal():
    """
    Generates a list (deck) of 52 integers (card values), 4 each of the values [0-12].
    Ordered at random, deals associated Card objects (cards) of half the elements of
    this list, chosen at random, to each of two deque objects (hands), returning both hands.
    :return: a tuple of two double-ended queue (deque) objects
    """
    # Initialize queues and generate a deck of card values [0, 0, 0, 0, 1, 1, 1, 1, 2, ..., 12, 12, 12]
    myCards = co.deque()
    yourCards = co.deque()
    deck = [c % 13 for c in range(52)]

    # Deal the entire deck in random order, alternating between players
    while deck:
        u = rd.randint(0, len(deck) - 1)
        # TODO: Deal with Card objects. Where do I need this?
        # yourCards.append(Card(deck.pop(u)))
        yourCards.append(deck.pop(u))
        i = rd.randint(0, len(deck) - 1)
        # myCards.append(Card(deck.pop(i)))
        myCards.append(deck.pop(i))

    return myCards, yourCards


if __name__ == '__main__':
    myCards, yourCards = deal()
    while myCards or yourCards:
        # TODO:
        # myCards, yourCards = takeATurn(myCards, yourCards)
        break
    if myCards:
        print("You win!")
    else:
        print("You lose :(")

    # for card in myCards:
    #     print(card.value, '->', card.faceValue)
    # for card in yourCards:
    #     print(card.value, '->', card.faceValue)

