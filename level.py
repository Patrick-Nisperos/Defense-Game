
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
            

    @property
    def enemyList(self):
        return self._enemyList

        

    