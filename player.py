
from pygame.constants import FINGERDOWN
from character import Character
from projectile import Projectile
import pygame
import pygame.image
import os



class Player(Character):
    fireball1 = Projectile(pygame.image.load(os.path.join("Images", "Fireball1.png")), 0, 580, 0.5, 1)
    def __init__(self, Image, xCoord, yCoord, xCoordChange, health, fired):
        super().__init__(Image, xCoord, yCoord, xCoordChange, health)
        self._fired = fired
        

    def launchFireball(self, screen):
        Player.fireball1.xCoord = self.xCoord + 16
        Player.fireball1.yCoord = self.yCoord - 40
        pygame.Surface.blit(screen, Player.fireball1.image, (Player.fireball1.xCoord, Player.fireball1.yCoord))
        print("launched")
        
    def moveFireball(self, screen):
        Player.fireball1.yCoord -= Player.fireball1.yChange
        pygame.Surface.blit(screen, Player.fireball1.image, (Player.fireball1.xCoord, Player.fireball1.yCoord))


    @property
    def fired(self):
        return self._fired
    @fired.setter
    def fired(self, x):
        self._fired = x



    

