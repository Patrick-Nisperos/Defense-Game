import pygame
from pygame.constants import USEREVENT
# these other pygame imports aren't necessary for function, but allow for easier coding
import pygame.display
import pygame.image
import pygame.event
import pygame.time
import pygame.mouse
import pygame.draw
import pygame.font
import random
import os
import math

from player import Player
from enemy import Enemy
from projectile import Projectile
from level import Level

# Images
level1backgroundImg = pygame.image.load(os.path.join("Images", "background.png"))
playerImg = pygame.image.load(os.path.join("Images", "WizardFaceUp.png"))
knightImg = pygame.image.load(os.path.join("Images", 'knight.png'))
fireballImg1 = pygame.image.load(os.path.join("Images", "Fireball1.png"))
coinImg = pygame.image.load(os.path.join("Images", "Coin.png"))

# Future Game Plan Features: 
    # - ADD Menu Inteface
    # - ADD Guard Towers you can buy
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
screen = pygame.display.set_mode((832, 880))

# Coin and Wave Text
GAME_FONT = pygame.font.SysFont('Comic Sans MS', 30)


# Title and Icon
pygame.display.set_caption("Patrick's Medieval Defense")
icon = pygame.image.load(os.path.join("Images", "Game Icon.png"))
pygame.display.set_icon(icon)
    
# Timers & events
MANA = pygame.USEREVENT + 1
moveBoat = pygame.USEREVENT + 2
spawnBoat = pygame.USEREVENT + 3
moveGoblin = pygame.USEREVENT + 4
animateCoin = pygame.USEREVENT + 5
checkEndWave = pygame.USEREVENT + 6

pygame.time.set_timer(MANA, 2000) #1000 ms = 1 s, each time the event goes off
pygame.time.set_timer(moveBoat, 30)
pygame.time.set_timer(spawnBoat, 2000)
pygame.time.set_timer(moveGoblin, 30)
pygame.time.set_timer(animateCoin, 1000)

def isCollision(x, projectile):
    distance = math.sqrt((math.pow(x.xCoord - projectile.xCoord,2)) + (math.pow(x.yCoord - projectile.yCoord, 2)))
    if distance < 27: #27 pixels
        return True
    else:
        return False

def castleHit(enemyList):
    for x in enemyList:
        if x.xCoord == 327 and x.yCoord == 743:
            enemyList.remove(x)
            return True
        elif x.xCoord == 441 and x.yCoord == 743:
            enemyList.remove(x)
            return True
        else:
            return False


def enemyHit(enemyList, projectile, player, deadEnemyList):
    for enemy in enemyList:
        collision = isCollision(enemy, projectile)
        if collision:
            coinDrop(player, enemy)
            enemyList.remove(enemy)
            deadEnemyList.append(enemy)
            return True

def coinDrop(player, enemy):
    if enemy.EnemyType == "goblin":
        player.coinAmount += 1
        print("set")

def animateCoinDrop(enemy):
    pygame.Surface.blit(screen, coinImg, (enemy.xCoord + 15, enemy.yCoord))

def gameLoop():
    firstPlayer = Player(playerImg, 370, 580, 0, 10)
    firstPlayerFireballList = []
    level1 = Level(level1backgroundImg, 5, "goblinBoat")
    level1NumOfBoats = level1.numEnemies
    deadEnemyList = []
    boatNumber = 0
    castleHealth = 10
    firing = False


   

    # Game window running (Everything in game must be implemented in the while running loop)
    running = True
    while running:
        screen.fill((0,0,0))  
        level1.drawBackground(screen)
        coinText = GAME_FONT.render(str(firstPlayer.coinAmount), False, (255,255,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == spawnBoat:
                if boatNumber < level1NumOfBoats:
                    level1.spawnBoat()
                    boatNumber += 1

            if event.type == MANA:
                 if firstPlayer.mana < 10:
                     firstPlayer.mana += 1

            if event.type == moveBoat:
                level1.moveBoat()

            if event.type == moveGoblin:
                level1.moveGoblin()

            if event.type == animateCoin:
                deadEnemyList.clear()

 


        # Keystroke Event for player movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not firing:
                    firstPlayer.yCoordChange = -2
                    firstPlayer.animate("up")
                if event.key == pygame.K_DOWN and not firing:
                    firstPlayer.yCoordChange = 2
                    firstPlayer.animate("down")
                if event.key == pygame.K_LEFT and not firing:
                    firstPlayer.xCoordChange = -2
                    firstPlayer.animate("left")
                if event.key == pygame.K_RIGHT and not firing:
                    firstPlayer.xCoordChange = 2
                    firstPlayer.animate("right")
                if event.key == pygame.K_SPACE and firstPlayer.mana > 0: #For fire delay, make it need mana that is slowly regenerated
                    firstPlayer.launchFireball(screen)
                    firstPlayerFireballList.append(firstPlayer.fireballList.pop())
                    firstPlayer.mana -= 1
                    firstPlayer.animate("up")
                    firing = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    firing = False
                if event.key == pygame.K_UP:
                    firstPlayer.yCoordChange = 0
                if event.key == pygame.K_DOWN:
                    firstPlayer.yCoordChange = 0
                if event.key == pygame.K_LEFT:
                    firstPlayer.xCoordChange = 0
                if event.key == pygame.K_RIGHT:
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
            if enemyHit(level1.enemyList, x, firstPlayer, deadEnemyList):
                firstPlayerFireballList.remove(x)

        for enemy in deadEnemyList:
            animateCoinDrop(enemy)

                

        firstPlayer.xCoord += firstPlayer.xCoordChange
        firstPlayer.yCoord += firstPlayer.yCoordChange

        pygame.Surface.blit(screen, firstPlayer.Image, (firstPlayer.xCoord, firstPlayer.yCoord))
        level1.drawEnemies(screen)
        level1.drawBoats(screen)

        # Castle Health Bar
        if castleHit(level1.enemyList):
            castleHealth -= 1
            print("castle hit")
        pygame.draw.rect(screen, (120,128,120), (365, 835, 100, 10))
        pygame.draw.rect(screen, (0,255,0), (365, 835, castleHealth * 10, 10))

        # Player Mana Bar
        pygame.draw.rect(screen, (120,128,120), (715, 835, 100, 10))
        pygame.draw.rect(screen, (20,30,190), (715, 835, firstPlayer.mana * 10, 10))

        # Player Health Bar
        pygame.draw.rect(screen, (120,128,120), (15, 835, 100, 10))
        pygame.draw.rect(screen, (190,20,30), (15, 835, firstPlayer.health * 10, 10))
        pygame.Surface.blit(screen, coinText, (205,825))

        pygame.display.update()
        clock.tick(60) # 60 means run at 60 fps max

def main():
    gameLoop()

# Use special var __name__ for good practice, this is the first line of code to be executed
if __name__ == "__main__":
    main()
