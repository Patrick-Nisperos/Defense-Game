
from character import Character

class Enemy(Character):
    def __init__(self, Image, xCoord, yCoord, xCoordChange):
        super().__init__(Image, xCoord, yCoord, xCoordChange) #Super always calls the parent class
