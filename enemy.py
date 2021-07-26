
from player import Player

class Enemy(Player):
    def __init__(self, Image, xCoord, yCoord, xChange):
        super().__init__(Image, xCoord, yCoord, xChange) #Super always calls the parent class
