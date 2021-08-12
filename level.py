
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
                self._enemyList.append(Enemy(random.randint(0,700), 100, 0, self._enemyType1))

    def drawBackground(self, screen):
        pygame.Surface.blit(screen, self._backGround, (0,-20))

    def drawEnemies(self, screen):
        for x in self._enemyList:
            pygame.Surface.blit(screen, x.image, (x.xCoord, x.yCoord))

    def moveGoblin(self, screen):
        for goblin in self._enemyList:
            if goblin.enemyType == "goblin":
                if goblin.yCoord < 370: # stop moving down cause wall
                    #lane 1
                    if goblin.xCoord < 96 and goblin.xCoord > 20:
                        goblin.xCoord -= 1
                    if goblin.xCoord <= 20:
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
                    if goblin.xCoord >= 612 and goblin.xCoord < 640:
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
            pygame.Surface.blit(screen, goblin.image, (goblin.xCoord, goblin.yCoord))
            

    @property
    def enemyList(self):
        return self._enemyList

        

    