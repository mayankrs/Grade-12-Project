import pygame
 
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red = ( 255,   0,   0)
 
pygame.init()
 
size = (255, 255)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Grids")
 
done = False
 
clock = pygame.time.Clock()

width = 20
height = 20
margin = 5

grid = [[0 for i in range(10)] for j in range(10)]

grid[1][5] = 1

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            j = pos[0] / (width + margin)
            i = pos[1] / (height + margin)
            grid[i][j] = 1
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
 
    screen.fill(black)
    
    for i in range(10):
        for j in range(10):
            color = white
            if grid[i][j] == 1:
                color = green
            pygame.draw.rect(screen, color, [(margin + width) * j + margin,
                                             (margin + height) * i + margin,
                                              width, height])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
