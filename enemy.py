
import pygame
import os

from pygame import image


class Enemy():
    goblinImg = pygame.image.load(os.path.join("Images", "GoblinFaceDownWalk0.png"))
    def __init__(self, xCoord, yCoord, xCoordChange, enemyType):
        self._xCoord = xCoord
        self._yCoord = yCoord
        self._xCoordChange = xCoordChange
        self._enemyType = enemyType
        if self._enemyType == "goblin": # Add additional enemy types here
            self._image = Enemy.goblinImg
            self._health = 1
            print("image was set")

    @property
    def enemyType(self):
        return self._enemyType
    

    @property       
    def xCoord(self):  
        return self._xCoord
    

    @xCoord.setter 
    def xCoord(self, x):
        self._xCoord = x
      
    
    @property
    def yCoord(self):
        return self._yCoord

    @yCoord.setter
    def yCoord(self, y):
        self._yCoord = y
    
    @property
    def xCoordChange(self):
        return self._xCoordChange

    @xCoordChange.setter
    def xCoordChange(self, x):
        self._xCoordChange = x

    @property
    def image(self):
        return self._image
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, x):
        self._health = x
