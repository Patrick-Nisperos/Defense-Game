import pygame
from pygame.constants import USEREVENT
import pygame.display
import pygame.image
import pygame.event
import pygame.time
import pygame.mouse
import random
import os
import math

from player import Player
from enemy import Enemy
from projectile import Projectile
from level import Level

# Images
level1backgroundImg = pygame.image.load(os.path.join("Images", "background.png"))
playerImg = pygame.image.load(os.path.join("Images", "Wizard.png"))
knightImg = pygame.image.load(os.path.join("Images", 'knight.png'))
fireballImg1 = pygame.image.load(os.path.join("Images", "Fireball1.png"))

# Future Game Plan Features: 
    # - ADD Menu Inteface
    # - ADD Health and Damage to enemies/player/base
    # - ADD castle at bottom that you protect from enemies
    # - ADD treasure walking cross the screen that gives bonus money if shot
    # - ADD shop (After Wave) containing more firepower, faster fire, or additional teammates, or traps
    # - ADD UPgrade Shop
    # - ADD beach at top of screen with ships dropping off enemies
    # - ADD waves of enemies
    # - ADD enemy Archer
    # - ADD Golem enemies throwing big rocks
    # - ADD Enemy Wizard Boss
    # - ADD in shop a user farm that genereates coins
    # - ADD bonus round purchase that gives a powerup of some sort when succesfully completed
    # - ADD sound
    # - ADD different maps
    # - ADD random quotes each time start screen is opened


# Initialize the pygame
pygame.init()
clock = pygame.time.Clock()

#Create the screen
screen = pygame.display.set_mode((832, 800))

# Title and Icon
pygame.display.set_caption("Patrick's Medieval Defense")
icon = pygame.image.load(os.path.join("Images", "Game Icon.png"))
pygame.display.set_icon(icon)
    
# Timers & events
MANA = pygame.USEREVENT + 1
MoveGoblin = pygame.USEREVENT + 2

pygame.time.set_timer(MANA, 1000) #1000 ms = 1 s, each time the event goes off
pygame.time.set_timer(MoveGoblin, 25)

def isCollision(x, projectile):
    distance = math.sqrt((math.pow(x.xCoord - projectile.xCoord,2)) + (math.pow(x.yCoord - projectile.yCoord, 2)))
    if distance < 27: #27 pixels
        return True
    else:
        return False



def enemyHit(enemyList, projectile):
    for x in enemyList:
        collision = isCollision(x, projectile)
        if collision:
            enemyList.remove(x)
            return True

def gameLoop():
    firstPlayer = Player(playerImg, 370, 580, 0, 10)
    #testEnemy = Enemy(enemyImg, random.randint(0,700), 100, 0, 1)
    firstPlayerFireballList = []
    level1 = Level(level1backgroundImg, 20, "goblin")
    level1.initilizeEnemyList()

   

    # Game window running (Everything in game must be implemented in the while running loop)
    running = True
    while running:
        screen.fill((0,0,0))  
        level1.drawBackground(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if event.type == MANA:
            #     print("Mana Event")

            if event.type == MoveGoblin:
                print("Move goblin event")
                level1.moveGoblin(screen)
                # call moveleft() moverigt() in goblin instances
                #   Default moveDown()
                #   for each enemy in level1.enemyList:
                #   move goblin()


        # Keystroke Event for player movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    firstPlayer.xCoordChange = -1
                if event.key == pygame.K_SPACE: #For fire delay, make it need mana that is slowly regenerated
                    firstPlayer.launchFireball(screen)
                    firstPlayerFireballList.append(firstPlayer.fireballList.pop())
                if event.key == pygame.K_RIGHT:
                    firstPlayer.xCoordChange = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    firstPlayer.xCoordChange = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos()[0])
                print(pygame.mouse.get_pos()[1])


        if firstPlayer.xCoord > 750: firstPlayer.xCoord = 750
        if firstPlayer.xCoord < 0 : firstPlayer.xCoord = 0
        
        for x in firstPlayerFireballList:
            firstPlayer.moveFireball(screen, x)
            if x.yCoord < 0:
                firstPlayerFireballList.remove(x)
            if enemyHit(level1.enemyList, x):
                firstPlayerFireballList.remove(x)


        firstPlayer.xCoord += firstPlayer.xCoordChange

        pygame.Surface.blit(screen, firstPlayer.Image, (firstPlayer.xCoord, firstPlayer.yCoord))
        level1.drawEnemies(screen)



        pygame.display.update()
        clock.tick(60) # 60 means run at 60 fps max

#Testing again one more time
gameLoop()
