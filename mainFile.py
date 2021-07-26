from enemy import Enemy
import pygame
import pygame.display
import pygame.image
import pygame.event
import random
import os

from player import Player
from enemy import Enemy

# Future Game Plan Features: 
    # - ADD Menu Inteface
    # - ADD castle at bottom that you protect from enemies
    # - ADD treasure walking cross the screen that gives bonus money if shot
    # - ADD shop containing more firepower, faster fire, or additional teammates, or traps
    # - ADD beach at top of screen with ships dropping off enemies
    # - ADD waves of enemies
    # - ADD enemy Archer
    # - ADD in shop a user farm that genereates coins
    # - ADD bonus round purchase that gives a powerup of some sort when succesfully completed
    # - ADD sound
    # - ADD different maps
    # - ADD random quotes each time start screen is opened


# Initialize the pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800, 700))

# Title and Icon
pygame.display.set_caption("Patrick's Medieval Defense")
icon = pygame.image.load(os.path.join("Images", "Game Icon.png"))
pygame.display.set_icon(icon)

# Enemy

enemyX = random.randint(0, 780)
enemyY = 100 
enemyX_change = 0

def drawImage(img, x, y):
    screen.blit(img, (x, y)) #Blit means draw
    
def gameLoop():
    playerImg = pygame.image.load(os.path.join("Images", "Wizard.png"))
    enemyImg = pygame.image.load(os.path.join("Images", "GoblinFaceDownWalk0.png"))
    knightImg = pygame.image.load(os.path.join("Images", 'knight.png'))
    firstPlayer = Player(playerImg, 370, 480, 0)
    

    testEnemy = Enemy(enemyImg, random.randint(0,700), 100, 0)

    # Game window running (Everything in game must be implemented in the while running loop)
    running = True
    while running:
        screen.fill((0,0,0))  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

       # Keystroke Event for player movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    firstPlayer.xCoordChange = -0.3

                if event.key == pygame.K_RIGHT:
                    firstPlayer.xCoordChange = 0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    firstPlayer.xCoordChange = 0

        if firstPlayer.xCoord > 750: firstPlayer.xCoord = 750
        if firstPlayer.xCoord < 0 : firstPlayer.xCoord = 0
        

        firstPlayer.xCoord += firstPlayer.xCoordChange
        drawImage(firstPlayer.Image, firstPlayer.xCoord, firstPlayer.yCoord)
        drawImage(knightImg, 200, 200)
        drawImage(enemyImg, testEnemy.xCoord, testEnemy.yCoord)
    
        pygame.display.update()

#Testing again one more time
gameLoop()
