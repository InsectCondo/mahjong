from tile import Tile
import random

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