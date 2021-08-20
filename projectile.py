
import pygame.image
import os

class Projectile():
    fireballImg = pygame.image.load(os.path.join("Images", "Fireball1.png"))
    def __init__(self, projectileType):
        self._projectileType = projectileType
        self._xCoord = 0
        self._yCoord = 0
        if self._projectileType == "fireball": # Set other types of projectiles here
            self._image = Projectile.fireballImg
            self._yChange = 3
            self._damage = 1


    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, img):
        self._image = img

    @property
    def yChange(self):
        return self._yChange
    
    @yChange.setter
    def yChange(self,y):
        self._yChange = y     

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
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, x):
        self._damage = x
        
