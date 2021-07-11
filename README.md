# War #
#### Written by Alex Staley, July 2021 ####

This program implements the card game "war".
Source code is written in Python 3.8 and is contained entirely in the file `War.py`.
Several unit tests exist for each function; these can be found in `test_war.py`.

Upon starting the program, the user will be prompted to select "manual" or "automatic" play style.
Select "manual" if you want to press the enter key to draw each card; in "automatic" mode the game
will simply play itself out until one hand is empty. All I/O takes place in the terminal window.

### Assumptions: ###
* We are using a standard, 52-card deck of playing cards,
with (increasing) values of 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen King, Ace.
* The game is single-player: the user may only compete against the program itself.
* When one player runs out of cards, the game ends immediately --
even if they have a stake in the cards currently on the table.

### Corner cases: ###
* If a player's hand is found to be empty, they immediately lose the game. This can occur:
    * At the end of a turn, before the next turn begins
    * After laying down a card that incurs a war
    * During the phase of war in which each player lays three cards face down on the table
    * After the "face down" phase of the war, before the players draw the final war card
* The case of serial wars is handled recursively by the `makeWar()` function.
* There is an extremely rare case in which players can run out of cards simultaneously.
Since the players' hands necessarily total to 52 cards, seven back-to-back wars
would need to take place, with equal initial hand sizes, for this to occur.
In this case, the win simply goes to the human (which honestly feels like a cop-out solution,
but I'd rather cop out than bloat the code to dress up such a rare case. And anyway,
we humans need SOME kind of edge).

### Future development: ###
* As it exists, there is some redundant code between the `takeATurn()` and `makeWar()` functions.
With more development time, I would like to refactor the common code to smaller, modular functions
that are called by both of these.
* I implemented crude user-control, with "manual" and "automatic" options, that let the user
either press the `enter` key to draw their face-up cards, or just let the game play itself out.
A hybrid, "manual war only" option is an idea I played with, but the sacrifice of readability
was too much for the trivial functionality gained. It may work better after the above described refactor.
* I would have liked to handle the edge cases with a bit more nuance -- implementing some
secondary tie-breaking functionality in the event a player doesn't have enough cards to settle a war
would make things more interesting.
* I would have liked to explore different techniques for dealing the cards; the one I used works fine
but sometimes leads to games that seem to not only go on forever, but go on forever without ever
even incurring a war. Some research into possible stable game states, to see if these have
characteristics that can be checked for, would be interesting.
* Test coverage can always be improved.
