
from character import Character

class Enemy(Character):
    def __init__(self, Image, xCoord, yCoord, xCoordChange, health):
        super().__init__(Image, xCoord, yCoord, xCoordChange, health) #Super function calls the parent class
