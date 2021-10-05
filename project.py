

import pygame
import math
import random
pygame.init()

# Main Screen with background image
screen = pygame.display.set_mode((1280, 720))
icon = pygame.image.load("icon_of_game.png")
pygame.display.set_caption("Game Trial")
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')

# Player specification
img = pygame.image.load("char01.png")
playerY = 280
playerX = 0
playerY_change = 0

# Enemy specification
img2 = pygame.image.load("enemy_pic.png")
EnemyX = 1150
EnemyY = random.randint(100, 580)
EnemyY_change = 2
EnemyX_change = -.5

# Bullet specification
img3 = pygame.image.load("bullet01.png")
bltX = 400
bltY = 0
bltX_change = -30
blt_state = "ready"


score = 0
# Player displayed on screen

def player(x, y):
    screen.blit(img, (x, y))

# Enemy displayed on screed


def enemy(x, y):
    screen.blit(img2, (x, y))

# Bullet displayed on screen (x-axis)
# Error while firing bullet (should be move to X-direction, but it moves on Y-direction)


def fire_blt(x, y):
    global blt_state
    blt_state = "fire"
    screen.blit(img3, (x-310, y-6))


def isCollision(EnemyY, EnemyX, bltY, bltX):
    distance = math.sqrt(((math.pow(EnemyY-bltY,2)) + (math.pow(EnemyX-bltX,2))))
    
    if distance <= 27:
        print(f'{distance}')
        return True
    else:
        return False


# Loop for all
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                playerY_change = 5
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_LCTRL:
                if blt_state is "ready":
                    bltY = playerY
                    fire_blt(bltX, bltY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerY_change = 0

#   Boundary for player
    playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    elif playerY >= 1216:
        playerY = 1216
    elif playerY >= 590:
        playerY = 590

#   Boundary for enemy
    EnemyY += EnemyY_change
    EnemyX += EnemyX_change

    if EnemyY <= 0:
        EnemyY_change = 3
        EnemyX += EnemyX_change
    elif EnemyY >= 590:
        EnemyY_change = -2
        EnemyX += EnemyX_change

#   Bullet firing location
    if bltX >= 1600:
        bltX = 400
        blt_state = "ready"

    if blt_state is "fire":
        fire_blt(bltX, bltY)
        bltX -= bltX_change

    # Collision
    collision = isCollision(EnemyY, EnemyX, bltY, bltX)
    if collision:
        bltX = 400
        blt_state = "ready"
        score += 1
        print(score)
        EnemyX = 1150
        EnemyY = EnemyY = random.randint(100, 580)



    player(playerX, playerY)
    enemy(EnemyX, EnemyY)
    pygame.display.update()
