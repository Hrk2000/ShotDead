import math
import random
import pygame
pygame.init()

screen_width = 900
screen_height = 600
gameWin = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bullet vs Box")

clock = pygame.time.Clock()
x = 0           # x-coordinate value of bullet
y = 250         # y-coordinate value of bullet
sq_x = 850      # x-coordinate value of square-box
sq_y = 230      # y-coordinate value of square-box
velocity_x = 0    # speed of bullet
rect_size_x = 20
square_vel_x = 0

end_line_x = 902

def collision():
    global sq_x,sq_y,x, Square,velocity_x, end_line_x, square_vel_x
    Square = pygame.draw.rect(gameWin, (0,0,255), [sq_x, sq_y, 50, 50])     # Square-box (defender)
 
    
    if abs(x - sq_x)<25:
        # print("Collision")      # Show in terminal
        sq_x = 850     # after collision, Square-box randomly generate on x-coordinate only
        x,velocity_x = 0,0        # After collision, bullet move on its initial coordinate and velocity becomes 0
        square_vel_x = -5
    # elif abs(x-sq_x)>6:
    #     velocity_x = 5
# Loop starts
running = True 
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:    # when button pressed
            if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL or event.key == pygame.K_KP0: # when left-contrl pressed.
                velocity_x = 10            # velocity increases after Left-control button pressed
            if event.key == pygame.K_ESCAPE or event.key == (pygame.K_LALT and pygame.K_F4):
                running = False
        
    x += velocity_x   # bullet move with velocity
    sq_x += square_vel_x      
    if sq_x == 300:
        square_vel_x = 5
    if sq_x == 850:
        square_vel_x = -5

   
    gameWin.fill((255, 255, 255))
    Rectangle = pygame.draw.rect(gameWin, (255, 0, 0), [x, y, rect_size_x, 10])  # Bullet
    Line = pygame.draw.rect(gameWin, (0,0,0), [end_line_x, 250, 5,20])    
    collision()
    pygame.display.update()
    clock.tick(60)
pygame.quit()       # Game Quit
