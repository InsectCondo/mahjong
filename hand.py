from deck import Deck

class Hand:
    def __init__(self, deck:Deck) -> None:
        self.deck       = deck
        self.tiles      = []
        self.handsize   = 13
        self.replenish()
        pass

    def replenish(self):
        """
        pulls tiles from top of linked deck until the hand has enough of them
        """
        while len(self.tiles) < self.handsize:
            self.tiles.append(self.deck.pulltile())
    
    def __str__(self) -> str:
        """
        writes the unicode characters for each tile
        
        example:
        `🀇 🀚 🀕 🀓 🀌 🀄 🀔 🀒 🀟 🀞 🀀 🀉 🀆
        `"""
        return " ".join([str(tile) for tile in self.tiles])

    def name(self) -> str:
        """
        writes the names of each tile in english
        
        example:
        `one of characters, two of circles, six of bamboo, four of bamboo, six of characters, red dragon, five of bamboo, three of bamboo, seven of circles, six of circles, east wind, three of characters, white dragon
        `"""
        return ", ".join([tile.name() for tile in self.tiles])