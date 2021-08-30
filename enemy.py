
from projectile import Projectile
import pygame
import os

from pygame import image


class Enemy():
     #Images
    goblinImgDown1 = pygame.image.load(os.path.join("Images", "GoblinFaceDownWalk1.png"))
    goblinImgDown2 = pygame.image.load(os.path.join("Images", "GoblinFaceDownWalk2.png"))
    goblinImgDown3 = pygame.image.load(os.path.join("Images", "GoblinFaceDownWalk3.png"))
    goblinImgRight1 = pygame.image.load(os.path.join("Images", "GoblinFaceRightWalk1.png"))
    goblinImgRight2 = pygame.image.load(os.path.join("Images", "GoblinFaceRightWalk2.png"))
    goblinImgLeft1 = pygame.image.load(os.path.join("Images", "GoblinFaceLeftWalk1.png"))
    goblinImgLeft2 = pygame.image.load(os.path.join("Images", "GoblinFaceLeftWalk2.png"))
    goblinBoatImgDown = pygame.image.load(os.path.join("Images", "goblinBoatFaceDown.png"))

    def __init__(self, xCoord, yCoord, EnemyType):
        self._xCoord = xCoord
        self._yCoord = yCoord
        self._EnemyType = EnemyType
        self._coinDrop = False
        if self._EnemyType == "goblin": # Add additional enemy types here
            self._image = Enemy.goblinImgDown1
            self._moveNumber = 1 #used to track images for movement
            self._imageDelay = 0
            self._health = 1
        if self._EnemyType == "goblinBoat": # Each boat carries 2 goblins
            self._image = Enemy.goblinBoatImgDown
            self._health = 2
            self._spawned = False
    
    def animate(self, direction):
        if self._EnemyType == "goblin" and direction == "down" and self._imageDelay == 0:
            self._imageDelay = 6
            if self._moveNumber == 1:
                self._image = Enemy.goblinImgDown2
                self._moveNumber += 1
            elif self._moveNumber == 2:
                self._image = Enemy.goblinImgDown3
                self._moveNumber = 1
        if self._EnemyType == "goblin" and direction == "right" and self._imageDelay == 0:
            self._imageDelay = 6
            if self._moveNumber == 1:
                self._image = Enemy.goblinImgRight1
                self._moveNumber += 1
            elif self._moveNumber == 2:
                self._image = Enemy.goblinImgRight2
                self._moveNumber = 1
        if self._EnemyType == "goblin" and direction == "left" and self._imageDelay == 0:
            self._imageDelay = 6
            if self._moveNumber == 1:
                self._image = Enemy.goblinImgLeft1
                self._moveNumber += 1
            elif self._moveNumber == 2:
                self._image = Enemy.goblinImgLeft2
                self._moveNumber = 1
        if self._imageDelay > 0:
            self._imageDelay -= 1


    @property
    def coinDrop(self):
        return self._coinDrop

    @coinDrop.setter
    def coinDrop(self, x):
        self._coinDrop = x

    @property
    def EnemyType(self):
        return self._EnemyType

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
    def image(self):
        return self._image
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, x):
        self._health = x

    @property
    def spawned(self):
        return self._spawned
    
    @spawned.setter
    def spawned(self, x):
        self._spawned = x
