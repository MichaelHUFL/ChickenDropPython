# Name: Michael Parks
# Date: 11/06/2025

# | ----- Libraries ----- |
import pygame
import random
import sys

# | ----- Initialize Game ----- |
pygame.init()

# | ----- Set Variables ----- |
black = (0, 0, 0)
red = (255, 0, 0)
width = 800
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zombie Clicker")

# | ----- Create Enemies ----- |
enemy = pygame.image.load("Zombie_TXT.png")
powerUp = pygame.image.load("Ice_TXT.png")

iterator = 0
numOfEnemies = 5
startX = []
startY = []
speed = []

while iterator < numOfEnemies:
    startX.append(random.randint(0, width - enemy.get_width() + 1))
    startY.append(0 - random.randint(enemy.get_height(), enemy.get_height() * 2))
    speed.append(0.5) # <- SPEED
    iterator += 1

# | ----- Replay Screen ----- |
replayScreen = False

bigFont = pygame.font.SysFont("Comic Sans", 200)
smallFont = pygame.font.SysFont("Comic Sans", 100)

playAgainText = bigFont.render("Play Again?", True, (0, 200, 0))
pax = width / 2 - playAgainText.get_rect().width / 2

yesText = smallFont.render("Yes", True, (0, 200, 0))
yesX = width / 4 - yesText.get_rect().width / 2

noText = smallFont.render("No", True, (0, 200, 0))
noX = width / 4 - yesText.get_rect().width / 2


# | ----- Game Loop ----- |
gameOver = False

while gameOver == False:
    # | - Quit - |
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
               gameOver = True
              
    # | - OnClick Manager - |
    if pygame.mouse.get_pressed()[0]:
        coords = pygame.mouse.get_pos()
        if replayScreen == False:
            iterator = 0
            while iterator < numOfEnemies:
                
                if coords[0] >= startX[iterator] and coords[0] <= startX[iterator] + enemy.get_width() and coords[1] >= startY[iterator] and coords[1] <= startY[iterator] + enemy.get_height():
                    startX[iterator] = random.randint(0, width - enemy.get_width() + 1)
                    startY[iterator] = 0 - random.randint(enemy.get_height(), enemy.get_height() * 2)
                    speed[iterator] = 0.5 # <- SPEED
                break
            iterator += 1
        else:
            
            if coords[0] >= yesX and coords[0] <= yesX + yesText.get_rect().width and coords[1] >= 450 and coords[1] <= 450 + yesText.get_rect().height:
                while iterator < numOfEnemies:
                    startX[iterator] = random.randint(0, width - enemy.get_width() + 1)
                    startY[iterator] = 0 - random.randint(enemy.get_height(), enemy.get_height() * 2)
                    speed[iterator] = 0.5 # <- SPEED
                replayScreen = False

            if coords[0] >= noX and coords[0] <= noX + noText.get_rect().width and coords[1] >= 450 and coords[1] <= 450 + noText.get_rect().height:
                gameOver = True
                
    # | - Update - |
    if replayScreen == False:
        iterator = 0
        while iterator < numOfEnemies:
            if startY[iterator] + enemy.get_height() > height:
             replayScreen = True
             break             
            startY[iterator] += speed[iterator]
            iterator += 1
            
    # | - Draw - |
    if replayScreen == False:
        screen.fill(black)
        iterator = 0
        while iterator < numOfEnemies:
            screen.blit(enemy, (startX[iterator], startY[iterator]))
            iterator += 1
        iterator = 0
    else:
        screen.fill(red)

        screen.blit(playAgainText, (pax, 150))
        screen.blit(yesText, (yesX, 450))
        screen.blit(noText, (noX, 450))
    
    pygame.display.flip()
pygame.display.quit()
