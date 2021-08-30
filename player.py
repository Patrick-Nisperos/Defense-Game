
from pygame.constants import FINGERDOWN
from character import Character
from projectile import Projectile
import pygame
import os
from pygame import image




class Player(Character):
    WizardImgDown = pygame.image.load(os.path.join("Images", "WizardFaceDown.png"))
    WizardImgUp = pygame.image.load(os.path.join("Images", "WizardFaceUp.png"))
    WizardImgLeft = pygame.image.load(os.path.join("Images", "WizardFaceLeft.png"))
    WizardImgRight = pygame.image.load(os.path.join("Images", "WizardFaceRight.png"))
    def __init__(self, Image, xCoord, yCoord, xCoordChange, health):
        super().__init__(Image, xCoord, yCoord, xCoordChange, health)
        self._yCoordChange = 0
        self._fireballList = []
        self._mana = 10
        self._coinAmount = 0
        

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

    def animate(self, direction):
        if direction == "up":
            self._Image = Player.WizardImgUp
        elif direction == "down":
            self._Image = Player.WizardImgDown
        elif direction == "right":
            self._Image = Player.WizardImgRight
        elif direction == "left":
            self._Image = Player.WizardImgLeft


    @property
    def fired(self):
        return self._fired
    @fired.setter
    def fired(self, x):
        self._fired = x

    @property
    def fireballList(self):
        return self._fireballList

    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self, x):
        self._mana = x

    @property
    def yCoordChange(self):
        return self._yCoordChange
    @yCoordChange.setter
    def yCoordChange(self, x):
        self._yCoordChange = x

    @property
    def coinAmount(self):
        return self._coinAmount
    @coinAmount.setter
    def coinAmount(self, x):
        self._coinAmount = x




    

