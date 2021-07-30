# This class is used as a base class for inheritance for enemies, friendlies, and player.
# Has many comments for the purpose of learning

class Character:
    x = [1,2,3] # Elements outside the __init__ method are static elements; they belong to the class.
    def __init__(self, Image, xCoord, yCoord, xCoordChange, health): # Elements inside the __init__ method are elements of the 
                                                                    # object (self); they don't belong to the class.
        self._Image = Image # _ indicates convention: (private) object variable
        self._xCoord = xCoord
        self._yCoord = yCoord
        self._xCoordChange = xCoordChange
        self._health = health

#Getters and Setters or python(Decorators)
    @property
    def Image(self):
        return self._Image
    
    @Image.setter
    def Image(self, img):
        self._Img = img

    @property       #use @property keyword for a getter
    def xCoord(self):  
        return self._xCoord
        # Ex: print(firstPlayer.playerX)

    @xCoord.setter #use @variable.setter for a setter
    def xCoord(self, x):
        self._xCoord = x
        # Ex: firstPlayer.playerX = 300
    
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
    def health(self):
        return self._health

    @health.setter
    def health(self, x):
        self._health = x


