import random as rd
import collections as co


def show(value):
    """
    Returns as a string the face value of the card, given its integer value.
    i.e. 0 -> '2', 1 -> '3', 2 -> '4', ... 9 -> "Jack", 10 -> "Queen", ...
    :raise: ValueError if given integer value outside [0 - 12]
    :param value: int [0 - 12]
    :return: string ['2' - 'Ace']
    """
    if value < 0 or value > 12:
        raise ValueError(f"value {value} must be between [0-12]")

    if value == 9:
        return "Jack"
    if value == 10:
        return "Queen"
    if value == 11:
        return "King"
    if value == 12:
        return "Ace"

    return str(value + 2)


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
        yourCards.append(deck.pop(u))
        i = rd.randint(0, len(deck) - 1)
        myCards.append(deck.pop(i))

    return myCards, yourCards


def takeATurn(playerHand, opponentHand):
    """
    Resolves a turn of war given each player's hand. Wraps the recursive 'makeWar' function.
    :param playerHand: collections.deque object representing the user's hand
    :param opponentHand: collections.deque object representing the opponent's hand
    :return: tuple containing the players' hands after a turn (including all necessary wars) has resolved
    """
    try:
        playerCard = playerHand.popleft()
        opponentCard = opponentHand.popleft()
    except IndexError:
        # Someone is out of cards; the game is over
        print(f'{"You" if not playerHand else "Your opponent"} just ran out of cards!')
        if not playerHand:
            return None, opponentHand
        else:
            return playerHand, None

    # Show cards
    table = [playerCard, opponentCard]
    print(f'YOUR CARD:\t\t\t{show(playerCard)}\nOPPONENT\'S CARD:\t{show(opponentCard)}')

    # Distribute cards to the winner; make war if necessary
    if playerCard == opponentCard:
        # War
        playerHand, opponentHand, table = makeWar(playerHand, opponentHand, table)
    else:
        # Winner collects; ready for new hand
        if playerCard < opponentCard:
            for card in table:
                opponentHand.append(card)
        else:
            for card in table:
                playerHand.append(card)

    return playerHand, opponentHand


def makeWar(playerHand, opponentHand, table):
    """
    Handles cards in the players' hands and on the table in the event of a war,
    handling the case of serial wars recursively. Returns with one hand empty if the game ends.
    :param playerHand: collections.deque object representing the user's hand
    :param opponentHand: collections.deque object representing the opponent's hand
    :param table: list of integers representing the cards currently on the table
    :return: tuple containing both players' hands, plus the list of cards on the table
    """
    print("This means WAR!")
    try:
        print("\tLaying three cards each face down on the table...")
        for _ in range(3):
            table.append(playerHand.popleft())
            table.append(opponentHand.popleft())
    except IndexError:
        print(f'{"You" if not playerHand else "Your opponent"} just ran out of cards mid-war!')
        # Someone ran out of cards mid-war; the game is over
        if not playerHand:
            return None, opponentHand, table
        else:
            return playerHand, None, table

    # Someone just put their last three cards face down; the game is over
    if not playerHand:
        print("Uh oh... you're out of cards!")
        return None, opponentHand, table
    if not opponentHand:
        print("Your opponent is out of cards!")
        return playerHand, None, table

    # Show cards to settle war
    playerCard = playerHand.popleft()
    opponentCard = opponentHand.popleft()
    table.append(playerCard)
    table.append(opponentCard)
    print(f'\tYOUR NEW CARD:\t\t\t{show(playerCard)}\n\tOPPONENT\'S NEW CARD:\t{show(opponentCard)}')

    # If war ends, show all cards on the table and distribute them to the winner
    if playerCard != opponentCard:
        print(f'\tYou {"lost" if playerCard < opponentCard else "won"} the war! Cards collected:')
        # TODO: Clean up card display, remove last commas
        if playerCard < opponentCard:
            for card in table:
                print('\t', show(card), end=', ')
                opponentHand.append(card)
        else:
            for card in table:
                print('\t', show(card), end=', ')
                playerHand.append(card)
        print('\n')
        return playerHand, opponentHand, None

    # If war must go on, recurse
    return makeWar(playerHand, opponentHand, table)


if __name__ == '__main__':
    myCards, yourCards = deal()
    while myCards and yourCards:
        myCards, yourCards = takeATurn(myCards, yourCards)
    if myCards:
        print("You win!")
    else:
        print("You lose :(")

