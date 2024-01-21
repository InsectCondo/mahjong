from deck import Deck
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