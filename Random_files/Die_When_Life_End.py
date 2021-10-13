import math
import random
import pygame
pygame.init()
# window_width/height = 500/500
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Die when life end')         # Caption

bullet_x = 0            # X-Location of Bullet
dabba_x = 420           # X-Location of Box (Enemy)
dabba_y = 200           # Y-Location of Box (Enemy)
bullet_y = 220          # Y-Location of Bullet
bullet_vel = 0          # Velocity of bullet
life = 50               # Life of Box (Enemy)


def collision():        # Function for collision occurs
    global bullet_x, life, bullet_vel, dabba_x, running, dabba_y
    global dabba    # Box (Enemy)
    global dabba_life_box   # Enemy's Life above its head
    dabba = pygame.draw.rect(window, (255, 255, 255), [
                             dabba_x, dabba_y, 50, 50])
    dabba_life_box = pygame.draw.rect(
        window, (0, 255, 0), [dabba_x, dabba_y-20, life, 10])

    distance = math.sqrt(
        ((math.pow(dabba_y-bullet_y, 2))+(math.pow(dabba_x-bullet_x, 2))))

    # distance formula: sqrt((x2-x1)^2+(y2-y1)^2)
    # this is for collision when the distance between bullet and box is less than or equals to 40.

    if distance <= 40:
        bullet_x = 0        # when collide, bullet's change its location to initial location
        bullet_vel = 0      # velocity of bullet becomes zero.
        # Life decreases randomly after hitting of bullet to box.
        life -= random.randint(1, 10)
        # Print Life in decreasing order (inside console)
        print(f"Life : {life}%")
        return True                     # True means collide
    else:
        return False                    # False means no collision


print(f"Life : {life}%")            # Print initial(full) life

# Game loop starts from here
running = True
while running:
    if life < 1:                # if life is less than one, means 0, then game over.
        print("Game Over !")
        running = False
    # if X-location of bullet is hit the boundary, then it change its location to intial.
    if bullet_x >= 480:
        bullet_x = 0
        bullet_vel = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           # if quit function calls then game exit.
            running = False
        # if keyboard button is in pressing stage.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                bullet_vel = 0.25
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                dabba_x -= 10
            if event.key == pygame.K_RIGHT:
                dabba_x += 10
            if event.key == pygame.K_UP:
                dabba_y -= 10
            if event.key == pygame.K_DOWN:
                dabba_y += 10
    
    if dabba_x == 100:      # Box never touch or cross the bullet's initial X-location the bullet
        dabba_x = 110       # whenever X-location of Box hits 100 on x-coordinate, then it hold their position on that coordinate

    # X-location of bullet increases with increase in its velocity
    bullet_x += bullet_vel
    # window color is fill with black.
    window.fill((0, 0, 0))
    # draw bullet on window
    bullet = pygame.draw.rect(window, (255, 0, 0), [
                              bullet_x, bullet_y, 25, 10])
    collision()         # function for collision
    pygame.display.update()     # update the window, time to time
pygame.quit()       # whenever quit function call, then quit.
