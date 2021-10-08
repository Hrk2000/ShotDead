import math
import random
import pygame
pygame.init()

screen_width = 900
screen_height = 600
gameWin = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bullet vs Box")
pygame.display.update()

clock = pygame.time.Clock()
x = 0           # x-coordinate value of bullet
y = 250         # y-coordinate value of bullet
sq_x = 840      # x-coordinate value of square-box
sq_y = 230      # y-coordinate value of square-box
velocity = 0    # speed of bullet

def collision():
    global sq_x,sq_y,x, Square,velocity
    Square = pygame.draw.rect(gameWin, (0,0,255), [sq_x, sq_y, 50, 50])     # Square-box (defender)

    if abs(x - sq_x)<6:
        print("Collision")      # Show in terminal
        sq_x = random.randint(500, 850)     # after collision, Square-box randomly generate on x-coordinate only
        x,velocity = 0,0        # After collision, bullet move on its initial coordinate and velocity becomes 0

# Loop starts
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:    # when button pressed
            if event.key == pygame.K_LCTRL: # when left-contrl pressed.
                velocity = 10               # velocity increases after Left-control button pressed

    x += velocity   # bullet move with velocity
    gameWin.fill((255, 255, 255))
    Rectangle = pygame.draw.rect(gameWin, (255, 0, 0), [x, y, 20, 10])  # Bullet
    collision()
    pygame.display.update()
    clock.tick(60)
pygame.quit()       # Game Quit
