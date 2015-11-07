# Deck of Cards

The data structure I picked to represent the deck was a python list because it has easy access of like an array, and it also works like a queue because you can pop off the first element. The individual cards were represented as tuples in the form of ('A', 'spade') so the rank and suit were clearly separated. A simple list comprehension gave me all 52 possible cards.

To shuffle the cards I iterated through the cards and swapped each card with another random card in the deck. This will ensure that the deck is random because each index has an equal likelihood of being any particular rank and suit. To get the next card, I popped off the first element in the deck and returned it. The instructions did not specify exactly how to signal an error, but I figured that physically raising an error instead of just printing an error message would be better. Programs that are prone to doing something wrong should always be enclosed in try / catch statements, and thus it would be more helpful to raise an error to stop the program (thereby alerting it of a problem) and let the program handle the error than allow the program to continually do something wrong while only warning it with a print statement.

I originally had self.cards = [(rank, suit) for suit in self.SUITS for rank in self.RANKS] within both __init__ and shuffle(), but I realized that having it in shuffle() and then calling shuffle() from within __init__ would be a cleaner solution.

For testing my framework, I would initialize a Deck and check if the cards are random, call getNextCard() and check if the first card is actually being return and removed from the deck, call shuffle() to see if all the cards are put back into the deck and randomly shuffled, and also check if getNextCard() signals an error when there are no more cards left.


# Vacation

To run this program you can either type 'python vacation.py', 'python vacation.py km txtfile', or 'python vacation.py txtfile'. txtfile should be the relative path to a .txt file that has one City, Country per line. Including the argument km will change the output units into kilometers.

I used the python package geopy to handle the things related to geolocation and coordinates. I chose Python because it has strong scripting capabilities, but is not as limited programming-wise as bash is. It also has many powerful libraries written by other contributors, and is widely supported.

When I extracted the Vincenty distance and I had to choose between km and miles, I put the if / else statement inside the while loop. If I put the for loop inside the if / else statement then the performance when scaled up would increase because I wouldn't have to check the if / else statement at every iteration of the loop. However, this requires writing two nearly identical for loops. I opted for the if / else statement inside the while loop because that would make maintainability easier in the future. Throughout the script I also tried to make it as modular as possible for dealing with kilometers.
