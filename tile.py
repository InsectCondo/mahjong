from os.path import dirname
DIR = dirname(__file__)

class Tile:
    with open(f"{DIR}/tilenames.txt", "r") as file:
        tilenames = file.read().split("\n")

    def __init__(self, type_int:int) -> None:
        self.id = type_int
        pass

    def name(self) -> str:
        """
        writes the english name of the tile
        
        example: `red dragon`
        """
        return self.tilenames[self.id]
    
    def __str__(self) -> str:
        """
        writes the unicode character of the tile
        
        example: `🀄`
        """
        return chr(0x1F000 + self.id)
    
    def __gt__(self, other:"Tile") -> bool: return self.id > other.id
    def __lt__(self, other:"Tile") -> bool: return self.id < other.id