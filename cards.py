from random import randint


class Deck:
    def __init__(self):
        '''A class that represents a deck of cards. Holds the individual cards
        as tuples in the form as ('A', 'spade').
        '''
        self.SUITS = ['club', 'diamond', 'heart', 'spade']
        self.RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.CARDS = []
        self.shuffle()

    def shuffle(self):
        '''Shuffles the deck randomly. Should cause all cards to be put
        back in the deck.
        '''
        self.CARDS = [(rank, suit) for suit in self.SUITS for rank in self.RANKS]
        size = len(self.CARDS)
        for i in range(size):
            randomIndex = randint(0, size-1)
            randomCard = self.CARDS[randomIndex]
            self.CARDS[randomIndex] = self.CARDS[i]
            self.CARDS[i] = randomCard

    def getNextCard(self):
        '''Returns the next card from the deck. Should signal an error
        when the entire deck has been dealt out.
        '''
        try:
            return self.CARDS.pop(0)
        except:
            raise AttributeError('The deck is empty!')
