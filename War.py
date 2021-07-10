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
    Generates a list (deck) of 52 integers (cards), 4 each of the values [0-12].
    Deals half the cards, chosen at random, to each of two hands, returning both hands.
    :return: a tuple of two double-ended queue (deque) objects
    """
    # Initialize queues and generate a deck of card values:
    # [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, ..., 11, 11, 12, 12, 12, 12]
    playerHand = co.deque()
    opponentHand = co.deque()
    deck = [c % 13 for c in range(52)]

    # Deal the entire deck in random order, alternating between players
    while deck:
        u = rd.randint(0, len(deck) - 1)
        opponentHand.append(deck.pop(u))
        i = rd.randint(0, len(deck) - 1)
        playerHand.append(deck.pop(i))

    return playerHand, opponentHand


def takeATurn(playerHand, opponentHand, control):
    """
    Resolves a turn of war given each player's hand. Wraps the recursive 'makeWar' function.
    :param playerHand: collections.deque object representing the user's hand
    :param opponentHand: collections.deque object representing the opponent's hand
    :param control: controls if play should continue automatically or manually
    :return: tuple containing the players' hands after a turn (including all necessary wars) has resolved
    """
    # Draw cards; guard against empty hands
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
    print(f'\tYOUR CARD:\t\t\t{show(playerCard)}\n\tOPPONENT\'S CARD:\t{show(opponentCard)}')

    # Distribute cards to the winner; make war if necessary
    if playerCard == opponentCard:
        # War
        playerHand, opponentHand, table = makeWar(playerHand, opponentHand, table, control)
    else:
        # No war; winner collects cards on the table
        if playerCard < opponentCard:
            # Hand lost
            for card in table:
                opponentHand.append(card)
        else:
            # Hand won
            for card in table:
                playerHand.append(card)
        # Report status
        print(f'You {"won" if playerCard > opponentCard else "lost"} this hand...'
              f'{len(playerHand)} cards in your hand, {len(opponentHand)} in your opponent\'s.')

    return playerHand, opponentHand


def makeWar(playerHand, opponentHand, table, control):
    """
    Handles cards in the players' hands and on the table in the event of a war,
    handling the case of serial wars recursively.
    Returns with one hand empty if the game ends; with the table empty if/when the war ends.
    :param playerHand: collections.deque object representing the user's hand
    :param opponentHand: collections.deque object representing the opponent's hand
    :param table: list of integers representing the cards currently on the table
    :param control: controls if play should continue automatically or manually
    :return: tuple containing both players' hands, plus the list of cards on the table
    """
    # Put war cards face down on the table; guard against the game ending during/after this process
    print("This means WAR!")
    try:
        print("Laying three cards each face down on the table...")
        for _ in range(3):
            table.append(playerHand.popleft())
            table.append(opponentHand.popleft())
    except IndexError:
        # Someone ran out of cards mid-war; report status and return with losing hand == None
        print(f'{"Your opponent" if not opponentHand else "You"} just ran out of cards mid-war!')
        if not opponentHand:
            return playerHand, None, table
        else:
            return None, opponentHand, table

    # Someone just put their last three cards face down; report status and return with losing hand == None
    if not opponentHand:
        print("Your opponent is out of cards!")
        return playerHand, None, table
    if not playerHand:
        print("Uh oh... you're out of cards!")
        return None, opponentHand, table

    # If playing manually, trigger next draw
    if control == 'M':
        input("Hit any key to continue.")

    # Draw next cards to settle war
    playerCard = playerHand.popleft()
    opponentCard = opponentHand.popleft()
    print(f'\tYOUR NEW CARD:\t\t\t{show(playerCard)}\n\tOPPONENT\'S NEW CARD:\t{show(opponentCard)}')
    table.append(playerCard)
    table.append(opponentCard)

    # If war ends, show all cards on the table and distribute them to the winner; return both hands
    if playerCard != opponentCard:
        print(f'You {"lost" if playerCard < opponentCard else "won"} the war! Cards collected:', end=' ')
        if playerCard < opponentCard:
            # Hand lost
            for card in table:
                print(show(card), end=' ')
                opponentHand.append(card)
        else:
            # Hand won
            for card in table:
                print(show(card), end=' ')
                playerHand.append(card)
        # Report status and return
        print(f'\nYou {"won" if playerCard > opponentCard else "lost"} this hand...'
              f'{len(playerHand)} cards in your hand, {len(opponentHand)} in your opponent\'s.')
        return playerHand, opponentHand, None

    # If war must go on, recurse
    return makeWar(playerHand, opponentHand, table, control)


if __name__ == '__main__':
    # Allow user to select manual or automatic control
    controlOption = '_'
    while controlOption not in ['M', 'A']:
        controlOption = input("""
        Welcome to WAR!
        If you want to play the game manually, enter 'M'.
        For automatic play, enter 'A'."
        """)
        controlOption = controlOption.upper()

    # Begin the game
    print("Here we go!")
    myCards, yourCards = deal()
    myCards, yourCards = takeATurn(myCards, yourCards, controlOption)

    # Continue the game
    while myCards and yourCards:
        if controlOption == 'M':
            input("Hit any key to continue.")
        myCards, yourCards = takeATurn(myCards, yourCards, controlOption)

    # End the game
    if myCards:
        print("You win!")
    else:
        print("You lose :(")

