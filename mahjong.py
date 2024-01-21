
from deck import Deck
from hand import Hand

if __name__ == "__main__":
    deck = Deck()
    player1hand = Hand(deck)
    print(player1hand)
    print(player1hand.name())
