import random
from os.path import dirname
DIR = dirname(__file__)

class Deck:
    winds       = list(range(0,4))
    dragons     = list(range(4,7))
    characters  = list(range(7,16))
    bamboos     = list(range(16,25))
    circles     = list(range(25,34))
    flowers     = list(range(34,38))
    seasons     = list(range(38,43))

    suited  = characters + bamboos + circles
    honors  = winds      + dragons
    bonus   = flowers    + seasons

    def __init__(self) -> None:
        
        self.remainingtiles = 3*self.suited + 4*self.honors + 1*self.bonus
        self.shuffle()
        pass

    def shuffle(self): random.shuffle(self.remainingtiles)
    def pulltile(self) -> int: return Tile(self.remainingtiles.pop(0))

class Hand:
    def __init__(self, deck:Deck) -> None:
        self.deck = deck
        self.tiles = []
        self.replenish()
        pass

    def replenish(self):
        while len(self.tiles) < 13:
            self.tiles.append(self.deck.pulltile())
    
    def __str__(self) -> str:
        return " ".join([str(tile) for tile in self.tiles])

    def name(self) -> str:
        return ", ".join([tile.name() for tile in self.tiles])

class Tile:
    with open(f"{DIR}/tilenames.txt", "r") as file:
        tilenames = file.read().split("\n")

    def __init__(self, type_int:int) -> None:
        self.id = type_int
        pass

    def name(self) -> str:
        return self.tilenames[self.id]
    
    def __str__(self) -> str:
        return chr(0x1F000 + self.id)



if __name__ == "__main__":
    deck = Deck()
    player1hand = Hand(deck)
    print(player1hand)
    print(player1hand.name())
