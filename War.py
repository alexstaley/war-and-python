import random as rd
import queue as qu


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


if __name__ == '__main__':
    print("Mic check 1 2")
