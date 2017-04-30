import pygame

black   = [   0,   0,   0]
white   = [ 255, 255, 255]
red     = [ 255,   0,   0]
green   = [   0, 255,   0]
blue    = [   0,   0, 255]
yellow  = [ 245, 239,  59]

pygame.init()

size = [1000,700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Al Khor Community Gate')

done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(1)

font = pygame.font.Font(None, 40)
font1 = pygame.font.Font(None, 35)
font2 = pygame.font.Font(None, 30)

pic1 = pygame.image.load('grass.png')
pic2 = pygame.image.load('store.png')
pic3 = pygame.image.load('road.png')
pic4 = pygame.image.load('clinic.png')
pic5 = pygame.image.load('club.png')
pic6 = pygame.image.load('school.png')
pic7 = pygame.image.load('house.png')
pic8 = pygame.image.load('tree.png')
pic9 = pygame.image.load('kbc.png')

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(white)
    #screen.blit(pic1, [0, 0])
    screen.blit(pic9, [0, 0])

    '''SCHOOL'''
    
##    screen.blit(pic6, [550, 150])
##    
##    for i in range(13):
##        screen.blit(pic8, [930, i * 50])
##    for i in range(13):
##        screen.blit(pic8, [i * 70 + 10, 0])
##        
##    for i in range(9):
##        for j in range(2):
##            screen.blit(pic3, [j*35 + 422, i * 35 + 382])
##    for i in range(2):
##        for j in range(19):
##            screen.blit(pic3, [j*35, 325 + i * 35])
##    for i in range(3):
##        screen.blit(pic3, [650, i * 35 + 290])
    

    '''CLINIC and CLUB'''

##    screen.blit(pic4, [145, 100])
##    screen.blit(pic5, [615, 350])
##    
##    for i in range(13):
##        screen.blit(pic8, [920, i * 50])
##    for i in range(13):
##        screen.blit(pic8, [i*70, 600])
##        
##    for i in range(15):
##        for j in range(2):
##            screen.blit(pic3, [j*35 + 422, i * 35])
##    for i in range(2):
##        for j in range(12):
##            screen.blit(pic3, [j*35, 315 + i * 35])
##    for i in range(7):
##        screen.blit(pic3, [i * 35 + 495, 490 ])

    '''HOUSE'''
    
##    screen.blit(pic7, [325, 225])
##
##    for i in range(14):
##        screen.blit(pic8, [i*70, 0])
##    for i in range(13):
##        screen.blit(pic8, [0, i*50])
##    
##    for i in range(9):
##        for j in range(2):
##            screen.blit(pic3, [j*35+380, 390+i*35])

    '''STORE'''

##    screen.blit(pic2, [145, 100])
##    for i in range(13):
##        if i in range(5,7):
##            continue
##        else:
##            screen.blit(pic8, [i*70 + 70, 600])
##    for i in range(13):
##        screen.blit(pic8, [0, i*50])
##    for i in range(20):
##        for j in range(2):
##            screen.blit(pic3, [j*35 + 450, i * 35])
##    for i in range(2):
##        for j in range(8):
##            screen.blit(pic3, [j*35 + 168, 420 + i * 35])

    pygame.display.flip()
    
    clock.tick(100)
    
pygame.quit()
