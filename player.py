
from pygame.constants import FINGERDOWN
from character import Character
from projectile import Projectile
import pygame



class Player(Character):
    def __init__(self, Image, xCoord, yCoord, xCoordChange, health):
        super().__init__(Image, xCoord, yCoord, xCoordChange, health)
        self._fireballList = []
        self._mana = 5
        

    def launchFireball(self, screen):
        self._fireballList.append(Projectile("fireball"))
        fireball = self.fireballList[0]
        fireball.xCoord = self.xCoord + 16
        fireball.yCoord = self.yCoord - 20
        pygame.Surface.blit(screen, fireball.image, (fireball.xCoord, fireball.yCoord))
        print("launched")
        
    def moveFireball(self, screen, fireball):
        fireball.yCoord -= fireball.yChange
        pygame.Surface.blit(screen, fireball.image, (fireball.xCoord, fireball.yCoord))


    @property
    def fired(self):
        return self._fired
    @fired.setter
    def fired(self, x):
        self._fired = x

    @property
    def fireballList(self):
        return self._fireballList




    

