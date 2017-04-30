import pygame
import result
 
def f():
    black = (   0,   0,   0)
    white = ( 255, 255, 255)
    green = (   0, 255,   0)
    red = ( 255,   0,   0)

    pygame.init()

    width = 75
    height = 75
    margin = 10

    turn = 0
    grid = [[0 for i in range(3)] for j in range(3)]

    name1 = raw_input('Player 1:')
    name2 = raw_input('Player 2:')

    font = pygame.font.Font(None, 40)
    font1 = pygame.font.Font(None, 25)
    t1 = font.render('X', True, black)
    t2 = font.render('O', True, black)
    t3 = font1.render(name1, True, black)
    t4 = font1.render(name2, True, black)
    
    b, c = 0, 0
    p1r1, p1r2, p1r3, p1c1, p1c2, p1c3, p1d1, p1d2 = 0, 0, 0, 0, 0, 0, 0, 0
    p2r1, p2r2, p2r3, p2c1, p2c2, p2c3, p2d1, p2d2 = 0, 0, 0, 0, 0, 0, 0, 0
     
    size = (500, 500)
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Tic-Tac-Toe")
     
    done = False
     
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
                
            if event.type == pygame.MOUSEBUTTONDOWN :
                c += 1
                pos = pygame.mouse.get_pos()
                j = pos[0] / (width + margin)
                i = pos[1] / (height + margin)
                
                if turn:
                    
                    grid[i][j] = 2

                    turn = 0

                    if i == 0:
                        p2r1 += 1
                    if i == 1:
                        p2r2 += 1
                    if i == 2:
                        p2r3 += 1
                    if j == 0:
                        p2c1 += 1
                    if j == 1:
                        p2c2 += 1
                    if j == 2:
                        p2c3 += 1
                    if i == j:
                        p2d1 += 1
                    if i == (2 - j):
                        p2d2 += 1
                    
                else:
                    
                    grid[i][j] = 1

                    turn = 1
                    
                    if i == 0:
                        p1r1 += 1
                    if i == 1:
                        p1r2 += 1
                    if i == 2:
                        p1r3 += 1
                    if j == 0:
                        p1c1 += 1
                    if j == 1:
                        p1c2 += 1
                    if j == 2:
                        p1c3 += 1
                    if i == j:
                        p1d1 += 1
                    if i == (2 - j):
                        p1d2 += 1
                            
        # --- Drawing code should go here
     
        screen.fill(white)
        
        for i in range(3):
            for j in range(3):
                color = black
                if grid[i][j] == 1:
                    color = green
                    screen.blit(t1, [(margin + width) * (j + 0.45), (margin + height) * (i + 0.4)])
                if grid[i][j] == 2:
                    color = red
                    screen.blit(t2, [(margin + width) * (j + 0.45), (margin + height) * (i + 0.4)])
                pygame.draw.rect(screen, color, [(margin + width) * j + margin,
                                                 (margin + height) * i + margin,
                                                  width, height], 2)
      
        pygame.display.flip()

        for x in [p1r1, p1r2, p1r3, p1c1, p1c2, p1c3, p1d1, p1d2]:
            if x == 3:
                print name1, 'wins'
                b += 1
                break
        for y in [p2r1, p2r2, p2r3, p2c1, p2c2, p2c3, p2d1, p2d2]:
            if y == 3:
                print name2, 'wins'
                b += 1
                break
        if b != 0:
            break
        elif c == 9 and b == 0:
            print 'Draw'
            d += 1
            break
        
        clock.tick(10)
        
    pygame.quit()
f()
