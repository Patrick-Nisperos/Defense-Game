# This class is used as a base class for inheritance for enemies, friendlies, and player.

class Character:
    x = [1,2,3] # Example to show that this is CLASS VARIABLE NOT OBJECT VARIABLES, DONT DO THIS TYPE OF Variables
    def __init__(self, Image, xCoord, yCoord, xCoordChange):  # initializer or constructor for OBJECT VARIABLES belonging 
                                                        # to object not the class (I.e. data encapsulation)
        self._Image = Image # _ indicates private object variable
        self._xCoord = xCoord
        self._yCoord = yCoord
        self._xCoordChange = xCoordChange

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