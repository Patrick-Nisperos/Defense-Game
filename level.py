
from enemy import Enemy
import pygame
import random

class Level():
    def __init__(self, background, numEnemies, enemyType1):
        self._enemyList = []
        self._backGround = background
        self._numEnemies = numEnemies
        self._enemyType1 = enemyType1
        self._enemyType2 = None

    def initilizeEnemyList(self):
        for x in range (self._numEnemies):
            if self._enemyType1 == "goblin":
                self._enemyList.append(Enemy(random.randint(0,750), 100, 0, self._enemyType1))

    def drawBackground(self, screen):
        pygame.Surface.blit(screen, self._backGround, (0,-20))

    def drawEnemies(self, screen):
        for x in self._enemyList:
            pygame.Surface.blit(screen, x.image, (x.xCoord, x.yCoord))

    def moveGoblin(self, screen):
        for goblin in self._enemyList:
            if goblin.enemyType == "goblin":
                if goblin.yCoord < 370: # first part of movement seperate goblins to their respective lanes
                    #lane 1
                    if goblin.xCoord < 96 and goblin.xCoord > 10:
                        goblin.xCoord -= 1
                    if goblin.xCoord <= 10:
                        goblin.yCoord += 1
                    #lane 2
                    if goblin.xCoord > 135 and goblin.xCoord < 224: #135 - 128 = 7 difference, 224 - 192 = 36 difference from xcoord in image
                        goblin.xCoord -= 1
                    if goblin.xCoord >= 96 and goblin.xCoord < 135:
                        goblin.xCoord += 1
                    if goblin.xCoord == 135:
                        goblin.yCoord += 1
                    #lane 3
                    if goblin.xCoord > 263 and goblin.xCoord < 388:
                        goblin.xCoord -= 1
                    if goblin.xCoord >= 224 and goblin.xCoord < 263:
                        goblin.xCoord += 1
                    if goblin.xCoord == 263:
                        goblin.yCoord += 1
                    #lane 4
                    if goblin.xCoord > 519 and goblin.xCoord < 612:
                        goblin.xCoord -= 1
                    if goblin.xCoord >= 388 and goblin.xCoord < 519:
                        goblin.xCoord += 1
                    if goblin.xCoord == 519:
                        goblin.yCoord += 1
                    #lane 5
                    if goblin.xCoord > 647 and goblin.xCoord < 740:
                        goblin.xCoord -= 1
                    if goblin.xCoord >= 612 and goblin.xCoord < 647:
                        goblin.xCoord += 1
                    if goblin.xCoord == 647:
                        goblin.yCoord += 1
                    #lane 6
                    if goblin.xCoord > 775 and goblin.xCoord < 800:
                        goblin.xCoord -= 1
                    if goblin.xCoord >= 740 and goblin.xCoord < 775:
                        goblin.xCoord += 1
                    if goblin.xCoord == 775:
                        goblin.yCoord += 1
                if goblin.yCoord >= 370 and goblin.yCoord < 498: # second part of movement
                    if goblin.xCoord < 263:
                        goblin.xCoord += 1
                    if goblin.xCoord == 263:
                        goblin.yCoord += 1
                    if goblin.xCoord > 519:
                        goblin.xCoord -= 1
                    if goblin.xCoord == 519:
                        goblin.yCoord += 1
                if goblin.yCoord >= 498 and goblin.yCoord < 743:   # third part of movement
                    if goblin.xCoord <= 263 and goblin.xCoord > 71:
                        goblin.xCoord -= 1
                    if goblin.xCoord == 71:
                        goblin.yCoord += 1
                    if goblin.xCoord >= 519 and goblin.xCoord < 711:
                        goblin.xCoord += 1
                    if goblin.xCoord == 711:
                        goblin.yCoord += 1
                if goblin.yCoord == 743: # fourth and final part of movement
                    if goblin.xCoord < 327:
                        goblin.xCoord += 1
                    if goblin.xCoord > 441:
                        goblin.xCoord -= 1


            

    @property
    def enemyList(self):
        return self._enemyList

        

    