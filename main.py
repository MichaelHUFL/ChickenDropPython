# Name: Michael Parks
# Date: 11/06/2025

# | ----- Libraries ----- |
import sys
import pygame
import random

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
time = pygame.time.Clock()

# | ----- Create Enemies ----- |
enemy = pygame.image.load("Zombie_TXT.png")
powerUp = pygame.image.load("Ice_TXT.png")

iterator = 0
numOfEnemies = 5
startX = []
startY = []
speed = []

normalSpeed = 0.5
slowSpeed = 0.25
gameModeSpeed = 0

while iterator < numOfEnemies:
      startX.append(random.randint(0, width - enemy.get_width() + 1))
      startY.append(0 - random.randint(enemy.get_height(), enemy.get_height() * 2))
      speed.append(normalSpeed)
      iterator += 1
replayscreen = False

# | ----- Power-Up ----- |
powerupX = random.randint(0, width - powerUp.get_width())
powerupY = -powerUp.get_height() - random.randint(20, 100)
powerupSpeed = 0.75

# | ----- Replay Screen ----- |
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
    time.tick(60)
      
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
                    if pygame.time.get_ticks() < gameModeSpeed:
                        speed[iterator] = slowSpeed # <- SPEED
                    else:
                        speed[iterator] = normalSpeed # <- SPEED
                break
                  
            if (powerupX <= coords[0] <= powerupX + powerUp.get_width() and powerupY <= coords[1] <= powerupY + powerUp.get_height()):
                gameModeSpeed = pygame.time.get_ticks() + 5000
                speed[iterator] = slowSpeed # <- SPEED
                powerupX = random.randint(0, width - powerUp.get_width())
                powerupY = -powerUp.get_height() - random.randint(20, 100)
                powerupSpeed = 0.75
                      
            iterator += 1
        else:
            
            if coords[0] >= yesX and coords[0] <= yesX + yesText.get_rect().width and coords[1] >= 450 and coords[1] <= 450 + yesText.get_rect().height:
                while iterator < numOfEnemies:
                    startX[iterator] = random.randint(0, width - enemy.get_width() + 1)
                    startY[iterator] = 0 - random.randint(enemy.get_height(), enemy.get_height() * 2)
                    speed[iterator] = normalSpeed # <- SPEED
                gameModeSpeed = 0
                powerupX = random.randint(0, width - powerUp.get_width())
                powerupY = -powerUp.get_height() - random.randint(20, 100)
                powerup_speed = 0.75
                replayScreen = False

            if coords[0] >= noX and coords[0] <= noX + noText.get_rect().width and coords[1] >= 450 and coords[1] <= 450 + noText.get_rect().height:
                gameOver = True
                
    # | - Update - |
    if replayScreen == False:
        if pygame.time.get_ticks() >= gameModeSpeed and gameModeSpeed != 0:
            speed[iterator] = normalSpeed
            gameModeSpeed = 0
          
        iterator = 0
        while iterator < numOfEnemies:
            if startY[iterator] + enemy.get_height() > height:
                replayScreen = True
                break             
            startY[iterator] += speed[iterator]
            iterator += 1

    powerupY += powerupSpeed
    if powerupY > height:
        powerupX = random.randint(0, width - powerUp.get_width())
        powerupY = -powerUp.get_height() - random.randint(20, 100)
        powerupSpeed = 0.75
            
    # | - Draw - |
    if replayScreen == False:
        screen.fill(black)
        iterator = 0
        while iterator < numOfEnemies:
            screen.blit(enemy, (startX[iterator], startY[iterator]))
            iterator += 1
        screen.blit(powerUp, (powerupX, powerupY))
        iterator = 0
    else:
        screen.fill(red)

        screen.blit(playAgainText, (pax, 150))
        screen.blit(yesText, (yesX, 450))
        screen.blit(noText, (noX, 450))
    
    pygame.display.flip()
pygame.display.quit()
