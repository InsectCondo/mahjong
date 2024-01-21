from os.path import dirname
DIR = dirname(__file__)
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