
from warnings import resetwarnings
from enemy import Enemy
import pygame
import random

class Level():
    def __init__(self, background, numEnemies, enemyType1):
        self._enemyList = []
        self._boatList = []
        self._backGround = background
        self._numEnemies = numEnemies
        self._enemyType1 = enemyType1
        self._enemyType2 = None

    def initilizeEnemyList(self):
        for x in range (self._numEnemies):
            if self._enemyType1 == "goblinBoat":
                self._boatList.append(Enemy(random.randint(0,750), -110, self._enemyType1))

    def spawnBoat(self):
        self._boatList.append(Enemy(random.randint(0,750), -110, self._enemyType1))
    
    def spawnFromGoblinBoat(self, x, y):
        self._enemyList.append(Enemy(random.randint(x - 90, x + 90), y + 80, "goblin"))
        self._enemyList.append(Enemy(random.randint(x - 90, x + 90), y + 80, "goblin"))


    def moveBoat(self):
        for boat in self._boatList:
            if boat.enemyType == "goblinBoat":
                if boat.yCoord < -30: # first part of movement irrespective of lane
                    boat.yCoord += 1              
                if boat.yCoord >= -30 and boat.spawned == False: # second part of movement respective of lane
                    if boat.xCoord < 140: #lane 1 part 1
                        boat.xCoord += 1      
                    if boat.xCoord > 140 and boat.xCoord < 288:
                        boat.xCoord -= 1
                    if boat.xCoord == 140: #lane 1 part 2
                        if boat.yCoord < 50:
                            boat.yCoord += 1                    
                        if boat.yCoord == 50:
                            Level.spawnFromGoblinBoat(self, boat.xCoord, boat.yCoord) 
                            boat.spawned = True
                    if boat.xCoord >= 288 and boat.xCoord < 396: #lane 2 part 1
                        boat.xCoord += 1
                    if boat.xCoord > 396 and boat.xCoord < 524:
                        boat.xCoord -= 1
                    if boat.xCoord == 396: #lane 2 part 2
                        if boat.yCoord < 105:
                            boat.yCoord += 1
                        if boat.yCoord == 105:
                            Level.spawnFromGoblinBoat(self, boat.xCoord, boat.yCoord) 
                            boat.spawned = True
                    if boat.xCoord >= 524 and boat.xCoord < 652: #lane 3 part 1
                        boat.xCoord += 1
                    if boat.xCoord > 652:
                        boat.xCoord -= 1
                    if boat.xCoord == 652: #lane 3 part 2
                        if boat.yCoord < 50:
                            boat.yCoord += 1             
                        if boat.yCoord == 50:
                            Level.spawnFromGoblinBoat(self, boat.xCoord, boat.yCoord) 
                            boat.spawned = True
                if boat.spawned and boat.yCoord > -110:
                    boat.yCoord -= 1

                        


    def drawBackground(self, screen):
        pygame.Surface.blit(screen, self._backGround, (0,-20))

    def drawEnemies(self, screen):
        for x in self._enemyList:
            pygame.Surface.blit(screen, x.image, (x.xCoord, x.yCoord))

    def drawBoats(self, screen):
        for boat in self._boatList:
            pygame.Surface.blit(screen, boat.image, (boat.xCoord, boat.yCoord))

    def moveGoblin(self):
        for goblin in self._enemyList:
            if goblin.enemyType == "goblin":
                if goblin.yCoord < 370: # first part of movement seperate goblins to their respective lanes
                    #lane 1
                    if goblin.xCoord < 96 and goblin.xCoord > 10:
                        goblin.xCoord -= 1
                        goblin.animate("left")
                    if goblin.xCoord <= 10:
                        goblin.yCoord += 1
                        goblin.animate("down")
                    #lane 2
                    if goblin.xCoord > 135 and goblin.xCoord < 224: #135 - 128 = 7 difference, 224 - 192 = 36 difference from xcoord in image
                        goblin.xCoord -= 1
                        goblin.animate("left")
                    if goblin.xCoord >= 96 and goblin.xCoord < 135:
                        goblin.xCoord += 1
                        goblin.animate("right")
                    if goblin.xCoord == 135:
                        goblin.yCoord += 1
                        goblin.animate("down")
                    #lane 3
                    if goblin.xCoord > 263 and goblin.xCoord < 388:
                        goblin.xCoord -= 1
                        goblin.animate("left")
                    if goblin.xCoord >= 224 and goblin.xCoord < 263:
                        goblin.xCoord += 1
                        goblin.animate("right")
                    if goblin.xCoord == 263:
                        goblin.yCoord += 1
                        goblin.animate("down")
                    #lane 4
                    if goblin.xCoord > 519 and goblin.xCoord < 612:
                        goblin.xCoord -= 1
                        goblin.animate("left")
                    if goblin.xCoord >= 388 and goblin.xCoord < 519:
                        goblin.xCoord += 1
                        goblin.animate("right")
                    if goblin.xCoord == 519:
                        goblin.yCoord += 1
                        goblin.animate("down")
                    #lane 5
                    if goblin.xCoord > 647 and goblin.xCoord < 740:
                        goblin.xCoord -= 1
                        goblin.animate("left")
                    if goblin.xCoord >= 612 and goblin.xCoord < 647:
                        goblin.xCoord += 1
                        goblin.animate("right")
                    if goblin.xCoord == 647:
                        goblin.yCoord += 1
                        goblin.animate("down")
                    #lane 6
                    if goblin.xCoord > 775 and goblin.xCoord < 800:
                        goblin.xCoord -= 1
                        goblin.animate("left")
                    if goblin.xCoord >= 740 and goblin.xCoord < 775:
                        goblin.xCoord += 1
                        goblin.animate("right")
                    if goblin.xCoord == 775:
                        goblin.yCoord += 1
                        goblin.animate("down")
                if goblin.yCoord >= 370 and goblin.yCoord < 498: # second part of movement
                    if goblin.xCoord < 263:
                        goblin.xCoord += 1
                        goblin.animate("right")
                    if goblin.xCoord == 263:
                        goblin.yCoord += 1
                        goblin.animate("down")
                    if goblin.xCoord > 519:
                        goblin.xCoord -= 1
                        goblin.animate("left")
                    if goblin.xCoord == 519:
                        goblin.yCoord += 1
                        goblin.animate("down")
                if goblin.yCoord >= 498 and goblin.yCoord < 743:   # third part of movement
                    if goblin.xCoord <= 263 and goblin.xCoord > 71:
                        goblin.xCoord -= 1
                        goblin.animate("left")
                    if goblin.xCoord == 71:
                        goblin.yCoord += 1
                        goblin.animate("down")
                    if goblin.xCoord >= 519 and goblin.xCoord < 711:
                        goblin.xCoord += 1
                        goblin.animate("right")
                    if goblin.xCoord == 711:
                        goblin.yCoord += 1
                        goblin.animate("down")
                if goblin.yCoord == 743: # fourth and final part of movement
                    if goblin.xCoord < 327:
                        goblin.xCoord += 1
                        goblin.animate("right")
                    if goblin.xCoord > 441:
                        goblin.xCoord -= 1
                        goblin.animate("left")

    @property
    def numEnemies(self):
        return self._numEnemies
            
    @property
    def enemyList(self):
        return self._enemyList

    @property
    def boatList(self):
        return self._boatList

        

    