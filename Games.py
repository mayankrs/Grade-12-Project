import random
import pygame

def Hangman():
    hangman = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    words = ['python','computer','dictionary','monitor','keyboard','television']
    z, co, e, y = 0, 0, 0, 0
    a, b, d, x, g = '', [], ' ', '_', ''

    print 'How to play?'
    print 'You have to guess the word in 7 tries'
    print
    while True:
        secret = random.choice(words)
        l = len(secret)
        w = ['Wrong letters:']
                    
        for i in range(l):
            if i == 2 or i == 5:
                a = a + secret[i] + d           
            else:
                a = a + '_ '
        print a
        print
                        
        while co < 7:
            let = raw_input('Enter a letter:')
            if let in secret:
                e += 1
                if e == 1:
                    for i in range(l):
                        if i == 2 or i == 5 or secret[i] == let:
                            b.append(secret[i])
                        else:
                            b.append(x)
                else:
                    for i in range(l):
                        if i == 2 or i == 5 or secret[i] == let:
                            b[i] = secret[i]
                        else:
                            continue        
                f = d.join(b)
                print 
                print f
                print
                f = g.join(b)

                if f == secret:
                    break
                else:
                    continue
                         
            else:
                if let in w:
                    print 'This letter is already discarded'
                    print
                else:
                    print hangman[co]
                    co += 1
                    w.append(let)
                    print d.join(w)
                    print

        if co != 7:
            print
            print 'You WIN!!!'       
        else:
            print
            print 'You LOSE'
            print 'The word was',secret
        break
def Bingo():
    a = [[random.random() for row in range(1000)]for col in range(1000)]
    b = [[random.random() for row in range(1000)]for col in range(1000)]

    c = [ok for ok in range(1, 76)]
    g = ['B', 'I', 'N', 'G', 'O']
    u = ['(0-15)', '(16-30)', '(31-45)', '(46-60)', '(61-75)']
    r, q, r1, q1 = 0, 0, 0, 0

    n1 = ''
    n2 = ''

    n, m = 0, 15
    for i in range(5):
        d = []
        for j in range(5):
            for k in range(n,m):
                d.append(c[k])
                
            z = random.choice(d)
            a[i][j] = z
                    
        n += 15
        m += 15

    n, m = 0, 15
    for i in range(5):
        d = []
        for j in range(5):
            for k in range(n,m):
                d.append(c[k])
                
            z = random.choice(d)
            b[i][j] = z
                    
        n += 15
        m += 15

    def bingo(a, b, n1, n2):    
        print
        print 'Board 1 :', n1
        for i in range(5):
            print u[i],
        print
        for i in range(5):
            print g[i], '\t',
        print
        print '-' * 35,
        print
            
        for i in range(5):
            for j in range(5):
                print a[j][i], '\t',
            print
            
        print
        print 'Board 2 :', n2
        for i in range(5):
            print u[i],
        print
        for i in range(5):
            print g[i], '\t',
        print
        print '-' * 35,
        print
            
        for i in range(5):
            for j in range(5):
                print b[j][i], '\t',
            print

    print 'How to play?(Instructions)'
    print '1) This is totally based on your luck and no skill is required to play this game'
    print '2) There will be 2 boards given and you have to choose if you want to play 2 player or 1 player(against computer)'
    print '3) The first one to complete 4 corners or quick 7 wins'
    print '4) The computer will generate random numbers between 1-75'
    print '5) If the number is there in any of the boards then only they will be shown'
    print '6) If the number is not present in any of the boards then the boards will not be shown'
    print '7) Hit enter to generate a number'
    print
    print 'Game mode:'
    print '1) 1 player'
    print '2) 2 player'
    ans = raw_input('>>>')
    print
    if ans == '1':
        n1 = raw_input('Player 1:')
        n2 = 'Computer'
    else:
        n1 = raw_input('Player 1:')
        n2 = raw_input('Player 2:')
        
    bingo(a, b, n1, n2)

    for h in range(25):
        print
        t = raw_input('Hit ENTER to generate a new number')
        s = random.choice(c)
        print
        print 'The number is',s
        y = 0
        for i in range(5):
            for j in range(5):
                #if a[j][i] == s or b[j][i] == s:
                if a[j][i] == s:
                    a[j][i] = 'X'
                    if j in [0, 4] and i in [0, 4]:
                        r += 1
                    y += 1
                    r1 += 1
                if b[j][i] == s:
                    b[j][i] = 'X'
                    if j in [0, 4] and i in [0, 4]:
                        q += 1
                    y += 1
                    q1 += 1               
                    
        if y in [1, 2, 3, 4]:
            bingo(a, b, n1, n2)
                  
        if r == 4:
            print n1, 'wins by completing corners'
            break
        elif r1 == 7:
            print n1, 'wins by quick seven'
            break
        elif q == 4:
            print n2, 'wins by completing corners'
            break
        elif q1 == 7:
            print n2, 'wins by quick seven'
            break
        
    print
    print 'Thank you for playing'

def Tic_tac_toe():
    black = (   0,   0,   0)
    white = ( 255, 255, 255)
    green = (   0, 255,   0)
    red = ( 255,   0,   0)

    pygame.init()

    width = 100
    height = 100
    margin = 10

    turn = 0
    grid = [[0 for i in range(3)] for j in range(3)]

    name1 = raw_input('Player 1:')
    name2 = raw_input('Player 2:')

    font = pygame.font.Font(None, 50)
    font1 = pygame.font.Font(None, 25)
    font2 = pygame.font.Font(None, 35)
    t1 = font.render('X', True, black)
    t2 = font.render('O', True, black)
    t3 = font1.render(name1, True, black)
    t4 = font1.render(name2, True, black)
    t5 = font1.render('Won', True, black)
    t6 = font1.render('Lost', True, black)
    t7 = font1.render('Draw', True, black)
    t13 = font2.render('Play Again', True, black)
    t14 = font1.render(name1 + ' wins', True, black)
    t15 = font1.render(name2 + ' wins', True, black)
    t16 = font1.render('It is a draw', True, black)
    t17 = font.render('X and O', True, black)
    t18 = font1.render('Return to main screen', True, black)
        
    b, c = 0, 0
    w1, w2, d = 0, 0, 0
    KKK = 17
    p1r1, p1r2, p1r3, p1c1, p1c2, p1c3, p1d1, p1d2 = 0, 0, 0, 0, 0, 0, 0, 0
    p2r1, p2r2, p2r3, p2c1, p2c2, p2c3, p2d1, p2d2 = 0, 0, 0, 0, 0, 0, 0, 0

    size = (1000, 700)
    screen = pygame.display.set_mode(size)
         
    pygame.display.set_caption("Tic-Tac-Toe")
         
    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
                    
            if event.type == pygame.MOUSEBUTTONDOWN :
                pos = pygame.mouse.get_pos()
                j = (pos[0] - 150) / (width + margin)
                i = (pos[1] - 170) / (height + margin)
                if i in [0, 1, 2] and j in [0, 1, 2]:
                    c += 1
                    
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
                            
                    elif turn == 0:
                            
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
                        
                for x in [p1r1, p1r2, p1r3, p1c1, p1c2, p1c3, p1d1, p1d2]:
                    if x == 3:
                        w1 += 1
                        b += 1
                        #result.results(t14)
                        break
                    
                for y in [p2r1, p2r2, p2r3, p2c1, p2c2, p2c3, p2d1, p2d2]:
                    if y == 3:
                        w2 += 1
                        b += 1
                        #result.results(t15)
                        break

                if b != 0 or c == 9:
                    p1r1, p1r2, p1r3, p1c1, p1c2, p1c3, p1d1, p1d2 = 0, 0, 0, 0, 0, 0, 0, 0
                    p2r1, p2r2, p2r3, p2c1, p2c2, p2c3, p2d1, p2d2 = 0, 0, 0, 0, 0, 0, 0, 0
                                       
                    if c == 9:
                        if b == 0:
                            d += 1
                        c = 0
                        #result.results(t16)
                    elif b != 0:
                        b = 0
                                    
                if pos[0] in range(850, 950) and pos[1] in range(10, 60) and (b == 0 or c == 0):
                    p1r1, p1r2, p1r3, p1c1, p1c2, p1c3, p1d1, p1d2 = 0, 0, 0, 0, 0, 0, 0, 0
                    p2r1, p2r2, p2r3, p2c1, p2c2, p2c3, p2d1, p2d2 = 0, 0, 0, 0, 0, 0, 0, 0
                    grid = [[0 for i in range(3)] for j in range(3)]
                    b, c = 0, 0
                    
        # --- Drawing code should go here
     
        screen.fill(white)
        
        for i in range(3):
            for j in range(3):
                color = black
                if grid[i][j] == 1:
                    color = green
                    screen.blit(t1, [(margin + width) * (j + 0.45)+150, (margin + height) * (i + 0.4)+170])
                if grid[i][j] == 2:
                    color = red
                    screen.blit(t2, [(margin + width) * (j + 0.45)+150, (margin + height) * (i + 0.4)+170])
                pygame.draw.rect(screen, color, [150+(margin + width) * j + margin,
                                                 170+(margin + height) * i + margin,
                                                  width, height], 2)

        screen.blit(t3, [520, 360])#p1
        screen.blit(t4, [520, 430])#p2
        screen.blit(t5, [640, 300])#won
        screen.blit(t6, [740, 300])#lost
        screen.blit(t7, [840, 300])#draw
        pygame.draw.rect(screen, black, [510, 275, 400, 200], 2)#box
        pygame.draw.line(screen, black, [610, 275], [610, 475], 2)#vr1
        pygame.draw.line(screen, black, [710, 275], [710, 475], 2)#vr2
        pygame.draw.line(screen, black, [810, 275], [810, 475], 2)#vr3
        pygame.draw.line(screen, black, [510, 335], [910, 335], 2)#hr1
        pygame.draw.line(screen, black, [510, 405], [810, 405], 2)#hr2
        t8 = font1.render(str(w1), True, black)
        t9 = font1.render(str(w2), True, black)
        t10 = font1.render(str(w2), True, black)
        t11 = font1.render(str(w1), True, black)
        t12 = font1.render(str(d), True, black)
        screen.blit(t8, [650, 360])
        screen.blit(t9, [650, 430])
        screen.blit(t10, [750, 360])
        screen.blit(t11, [750, 430])
        screen.blit(t12, [850, 400])
        
        pygame.draw.rect(screen, black, [850, 10, 135, 50], 2)
        screen.blit(t13, [855, 25])
        screen.blit(t17, [450, 50])
            
        pygame.display.flip()
            
        clock.tick(10)

    if w1 > w2:
        print name1, 'has won more games'
    elif w1 < w2:
        print name2, 'has won more games'
    else:
        print 'Both have won equal number of games'
            

#Hangman()
#Bingo()
#Tic_tac_toe()


