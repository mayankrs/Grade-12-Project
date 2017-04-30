import pygame
import math

pi=math.pi

black   = [   0,   0,   0]
white   = [ 255, 255, 255]
red     = [ 255,   0,   0]
green   = [   0, 255,   0]
blue    = [   0,   0, 255]
yellow  = [ 245, 239,  59]

def objects():
    pygame.draw.rect(screen, black, [25, 25, 950, 650], 2)
    
    #EXIT
    pygame.draw.rect(screen, black, [25, 25, 100, 50], 2)

    #Buildings
    pygame.draw.rect(screen, black, [125, 250, 125, 125], 2)#1
    pygame.draw.rect(screen, black, [575, 250, 125, 125], 2)#2
    pygame.draw.rect(screen, black, [125, 500, 125, 125], 2)#Youth club
    pygame.draw.rect(screen, black, [675, 500, 125, 125], 2)#Grocery
    pygame.draw.rect(screen, black, [345, 50, 125, 125], 2)#house
 
    #Roads
    pygame.draw.line(screen, black, [375, 175], [375, 275], 2)    
    pygame.draw.line(screen, black, [375, 325], [375, 525], 2)
    pygame.draw.line(screen, black, [375, 575], [375, 675], 2)

    pygame.draw.line(screen, black, [450, 175], [450, 275], 2)
    pygame.draw.line(screen, black, [450, 325], [450, 525], 2)
    pygame.draw.line(screen, black, [450, 575], [450, 675], 2)

    pygame.draw.line(screen, black, [250, 275], [375, 275], 2)
    pygame.draw.line(screen, black, [250, 325], [375, 325], 2)

    pygame.draw.line(screen, black, [450, 275], [575, 275], 2)
    pygame.draw.line(screen, black, [450, 325], [575, 325], 2)
    
    pygame.draw.line(screen, black, [450, 575], [675, 575], 2)
    pygame.draw.line(screen, black, [450, 525], [675, 525], 2)
    
    pygame.draw.line(screen, black, [250, 525], [375, 525], 2)
    pygame.draw.line(screen, black, [250, 575], [375, 575], 2)

    #Learning shapes   
    '''pygame.draw.line(screen, black, [50, 550], [550, 550], 2)
    pygame.draw.line(screen, black, [950, 50], [950, 550], 2)
    pygame.draw.line(screen, black, [950, 550], [800, 550], 2)
    pygame.draw.rect(screen, black, [180, 250, 200, 200], 2)

    
    #pygame.draw.rect(screen, black, [550, 250, 250, 200], 2)
    pygame.draw.arc(screen, black, [550, 250, 250, 200], 0, pi, 2)
    pygame.draw.line(screen, black, [550, 340], [550, 550], 2)
    pygame.draw.line(screen, black, [800, 340], [800, 550], 2)'''

    
def texting():
    font = pygame.font.Font(None, 40)
    text = font.render('Exit', True, black)
    screen.blit(text, [42, 42])
    
    font1 = pygame.font.Font(None, 30)
    text1 = font1.render('Youth Club', True, black)
    screen.blit(text1, [130, 550])

    text2 = font1.render('Al Meera', True, black)
    screen.blit(text2, [680, 550])

    text3 = font1.render('Home', True, black)
    screen.blit(text3, [375, 100])

    text4 = font1.render('School', True, black)
    screen.blit(text4, [600, 300])
    
    text5 = font1.render('Clinic', True, black)
    screen.blit(text5, [150, 300])
    
pygame.init()

size = [1000,700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Community Map')

done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(1)

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if x<125 and x>25 and y>25 and y<125:
                import Community_gate
    
    #All event processing above this comment
            
    #All logic below
    
    
    
    #All logic above

    screen.fill(white)

    #All code to draw below this comment

    objects()
    texting()
    #All code to draw above this comment

    pygame.display.flip()
    
    clock.tick(50)
    
pygame.quit()
        
