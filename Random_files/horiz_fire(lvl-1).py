import pygame
pygame.init()

screen_width = 900
screen_height = 600
gameWin = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Horizontal Movement")
pygame.display.update()

clock = pygame.time.Clock()
x = 0
velocity = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                velocity = 10
    if x >= 900:
        x = 0
        velocity = 0

    x += velocity
    gameWin.fill((255,255,255))
    Rectangle = pygame.draw.rect(gameWin, (255,0,0), [x ,250, 20, 10])
    pygame.display.update()
    clock.tick(60)
pygame.quit()