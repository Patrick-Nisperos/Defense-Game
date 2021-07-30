
from pygame.constants import FINGERDOWN
from character import Character
from projectile import Projectile
import pygame
import pygame.image
import os



class Player(Character):
    def __init__(self, Image, xCoord, yCoord, xCoordChange, health, fired):
        super().__init__(Image, xCoord, yCoord, xCoordChange, health)
        self._fired = fired
        self._fireballList = []
        

    def launchFireball(self, screen):
        self._fireballList.append(Projectile(pygame.image.load(os.path.join("Images", "Fireball1.png")), 0, 580, 0.5, 1))
        fireball = self.fireballList[0]
        fireball.xCoord = self.xCoord + 16
        fireball.yCoord = self.yCoord - 40
        pygame.Surface.blit(screen, fireball.image, (fireball.xCoord, fireball.yCoord))
        print("launched")
        
    def moveFireball(self, screen, fireball):
        fireball.yCoord -= fireball.yChange
        pygame.Surface.blit(screen, fireball.image, (fireball.xCoord, fireball.yCoord))
        # if (fireball.yCoord > 0):
        #     return "Move"
        # else:
        #     return "Delete"


    @property
    def fired(self):
        return self._fired
    @fired.setter
    def fired(self, x):
        self._fired = x

    @property
    def fireballList(self):
        return self._fireballList




    

