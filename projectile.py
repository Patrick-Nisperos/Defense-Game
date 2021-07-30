
class Projectile():
    def __init__(self, img, x, y, yChange, damage):
        self._image = img
        self._xCoord = x
        self._yCoord = y
        self._yChange = yChange
        self._damage = damage

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, img):
        self._image = img

    @property
    def xCoord(self):
        return self._xCoord
    
    @xCoord.setter
    def xCoord(self,x):
        self._xCoord = x

    @property
    def yCoord(self):
        return self._yCoord
    
    @yCoord.setter
    def yCoord(self,y):
        self._yCoord = y     

    @property
    def yChange(self):
        return self._yChange
    
    @yChange.setter
    def yChange(self,y):
        self._yChange = y     



