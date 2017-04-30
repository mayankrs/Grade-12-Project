import pygame
import time

def kbc():
    black   = [   0,   0,   0]
    white   = [ 255, 255, 255]
    red     = [ 255,   0,   0]
    green   = [   0, 255,   0]
    blue    = [   0,   0, 255]
    yellow  = [ 245, 239,  59]

    pygame.init()

    money = {0:'0', 1:'5,000', 2:'10,000', 3:'20,000', 4:'40,000', 5:'80,000', 6:'1,60,000', 7:'3,20,000', 8:'6,40,000', 9:'15,00,000', 10:'25,00,000', 11:'50,00,000', 12:'1,00,00,000', 13:'3,00,00,000', 14:'5,00,00,000', 15:'7,00,00,000'}

    def Question1():
        t1 = font1.render("Q" + str(q) + ") Banganapalli and Kesar are varieties of which of these fruits?", True, white)
        op1 = font1.render('A) Apple', True, white)
        op2 = font1.render('B) Pear', True, white)
        op3 = font1.render('C) Guava', True, white)
        op4 = font1.render('D) Mango', True, white)##
        
        screen.blit(t1, [105, 450])
        
        if fifty == 1:
            screen.blit(op1, [115, 560])
            screen.blit(op4, [555, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])
        
    def Question2():
        t1 = font1.render("Q" + str(q) + ") Which of these animals is the largest member of the dog family?", True, white)
        op1 = font1.render('A) Jackal', True, white)
        op2 = font1.render('B) Hyena', True, white)
        op3 = font1.render('C) Wolf', True, white)##
        op4 = font1.render('D) Fox', True, white)
        screen.blit(t1, [100, 450])
        if fifty == 1:
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question3():
        t1 = font1.render("Q" + str(q) + ") The world's largest island Greenland is an autonomous", True, white)
        t2 = font1.render("       region within the kingdom of which country?", True, white)
        op1 = font1.render('A) England', True, white)
        op2 = font1.render('B) Denmark', True, white)##
        op3 = font1.render('C) Belgium', True, white)
        op4 = font1.render('D) Netherlands', True, white)
        screen.blit(t1, [115, 440])
        screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question4():        
        t1 = font1.render("Q" + str(q) + ") Which of these gases is named for it's color?", True, white)
        op1 = font1.render('A) Helium', True, white)
        op2 = font1.render('B) Methane', True, white)
        op3 = font1.render('C) Oxygen', True, white)
        op4 = font1.render('D) Chlorine', True, white)##
        screen.blit(t1, [110, 450])
        if fifty == 1:
            screen.blit(op2, [555, 560])
            screen.blit(op4, [555, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question5():
        t1 = font1.render("Q" + str(q) + ")  Which of these sports has 22 players playing on the field", True, white)
        t2 = font1.render("        at the same time?", True, white)
        op1 = font1.render('A) Cricket', True, white)
        op2 = font1.render('B) Hockey', True, white)##
        op3 = font1.render('C) Rugby', True, white)
        op4 = font1.render('D) Basketball', True, white)
        screen.blit(t1, [115, 440])
        screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question6():
        t1 = font1.render("Q" + str(q) + ") What is the minimum number of coins of current denomination", True, white)
        t2 = font1.render("       that will add up to make 8 Indian rupees?", True, white)
        op1 = font1.render('A) Two', True, white)
        op2 = font1.render('B) Three', True, white)##
        op3 = font1.render('C) Four', True, white)
        op4 = font1.render('D) Five', True, white)
        screen.blit(t1, [110, 440])
        screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question7():
        t1 = font1.render("Q" + str(q) + ") How many watts equal a megawatt?", True, white)
        op1 = font1.render('A) One hundred', True, white)
        op2 = font1.render('B) One thousand', True, white)
        op3 = font1.render('C) Ten thousand', True, white)
        op4 = font1.render('D) One lakh', True, white)##
        screen.blit(t1, [105, 450])
        if fifty == 1:
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question8():
        t1 = font1.render("Q" + str(q) + ") In Feb 2014, Indian-origin Satya Nadella became the CEO of", True, white)
        t2 = font1.render("       which company?", True, white)
        op1 = font1.render('A) IBM', True, white)
        op2 = font1.render('B) Microsoft', True, white)##
        op3 = font1.render('C) Apple', True, white)
        op4 = font1.render('D) Wibro', True, white)
        screen.blit(t1, [115, 440])
        screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question9():
        t1 = font1.render("Q" + str(q) + ") The Krishna-Godavari Basin is one of the largest reserves", True, white)
        t2 = font1.render("        in India of which natural resources?", True, white)
        op1 = font1.render('A) Aluminium', True, white)
        op2 = font1.render('B) Natural Gas', True, white)##
        op3 = font1.render('C) Coal', True, white)
        op4 = font1.render('D) Zinc', True, white)
        screen.blit(t1, [115, 440])
        screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])
            
    def Question10():
        t1 = font1.render("Q" + str(q) + ") With which of these states does Telengana not share", True, white)
        t2 = font1.render("        its border?", True, white)
        op1 = font1.render('A) Tamil Nadu', True, white)##
        op2 = font1.render('B) Karnataka', True, white)
        op3 = font1.render('C) Chattisgarh', True, white)
        op4 = font1.render('D) Maharashtra', True, white)
        screen.blit(t1, [115, 440])
        screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op1, [115, 560])
            screen.blit(op4, [555, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question11():
        t1 = font1.render("Q" + str(q) + ") Which of these MPs became the first BJP leader to present", True, white)
        t2 = font1.render('        the rail budget in the Parliament?', True, white)
        op1 = font1.render('A) Sadanand Gowda', True, white)##
        op2 = font1.render('B) Ram Naik', True, white)
        op3 = font1.render('C) Yaswant Sinha', True, white)
        op4 = font1.render('D) Jaswant Singh', True, white)
        screen.blit(t1, [115, 440])
        screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question12():
        t1 = font1.render("Q" + str(q) + ") According to the media campaign 'Power of 49', who form", True, white)
        t2 = font1.render("       as much as 49% percent of the Indian voter base?", True, white)
        op1 = font1.render('A) Youth', True, white)
        op2 = font1.render('B) First time voters', True, white)
        op3 = font1.render('C) Women', True, white)##
        op4 = font1.render('D) Men', True, white)
        screen.blit(t1, [115, 440])
        screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op1, [115, 560])
            screen.blit(op3, [115, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question13():
        t1 = font1.render("Q" + str(q) + ") Which of these battles didn't involve the Mughal army?", True, white)
        op1 = font1.render('A) Battle of Buxar', True, white)
        op2 = font1.render('B) Battle of Haldighati', True, white)
        op3 = font1.render('C) Second battle of Panipat', True, white)
        op4 = font1.render('D) Third battle of Panipat', True, white)##
        screen.blit(t1, [110, 450])
        if fifty == 1:
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question14():
        t1 = font1.render("Q" + str(q) + ") Before 2014,when was the last time in India that a single", True, white)
        t2 = font1.render("party majority was formed at the centre?", True, white)
        op1 = font1.render('A) 1991', True, white)
        op2 = font1.render('B) 1990', True, white)
        op3 = font1.render('C) 1984', True, white)##
        op4 = font1.render('D) 1999', True, white)
        screen.blit(t1, [115, 440])
        screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])
        
    def Question15():
        t1 = font1.render("Q" + str(q) + ") What discovery in 1823 is credited to the British", True, white)
        t2 = font1.render('      official Robert Bruce?', True, white)
        op1 = font1.render('A) Oil', True, white)
        op2 = font1.render('B) Tea', True, white)##
        op3 = font1.render('C) Murga silk', True, white)
        op4 = font1.render('D) Jute', True, white)
        screen.blit(t1, [115, 440])
        screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question16():
        t1 = font1.render("Q" + str(q) + ") Which scientist has been named for the Bharat Ratna in 2013?", True, white)
        #t2 = font1.render('      official Robert Bruce?', True, white)
        op1 = font1.render('A) Prof C N R Rao', True, white)##
        op2 = font1.render('B) Prof U R Rao', True, white)
        op3 = font1.render('C) Prof Yash Pal', True, white)
        op4 = font1.render('D) Dr K Radhakrishnan', True, white)
        screen.blit(t1, [105, 450])
        #screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question17():
        t1 = font1.render("Q" + str(q) + ") Which is the oldest mountain range in India?", True, white)
        #t2 = font1.render('      official Robert Bruce?', True, white)
        op1 = font1.render('A) Nilgiris', True, white)
        op2 = font1.render('B) Aravalli', True, white)##
        op3 = font1.render('C) Vindhya', True, white)
        op4 = font1.render('D) Satpura', True, white)
        screen.blit(t1, [115, 440])
        #screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Question18():
        t1 = font1.render("Q" + str(q) + ") Which animal experiences the maximum amount of daylight in a year?", True, white)
        #t2 = font1.render('      official Robert Bruce?', True, white)
        op1 = font1.render('A) Atlantic Salmon', True, white)
        op2 = font1.render('B) Grey Whale', True, white)
        op3 = font1.render('C) Arctic Tern', True, white)##
        op4 = font1.render('D) Monarch Butterfly', True, white)
        screen.blit(t1, [115, 440])
        #screen.blit(t2, [115, 475])
        if fifty == 1:
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])
        else:
            screen.blit(op1, [115, 560])
            screen.blit(op2, [555, 560])
            screen.blit(op3, [115, 650])
            screen.blit(op4, [555, 650])

    def Extra():
    ##    ques = {1:Question16(), 2:Question17(), 3:Question18()}
    ##    ques[1]
        Question16()
        
    size = [1000,700]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Al Khor Community Gate')

    done = False

    clock = pygame.time.Clock()

    pygame.mouse.set_visible(1)

    font = pygame.font.Font(None, 40)
    font1 = pygame.font.Font(None, 35)
    font2 = pygame.font.Font(None, 30)
    font3 = pygame.font.Font(None, 80)

    pic1 = pygame.image.load('kbc.png')
    pic2 = pygame.image.load('life.png')
    pic3 = pygame.image.load('kbc1.png')

    q = 0
    y = 0
    click = -1
    close = 0
    flip = 0
    double = 0
    fifty = 0

    t1 = font.render('50:50', True, white)
    t2 = font.render('Double dip', True, white)
    t3 = font.render('Flip the question', True, white)
    t4 = font.render('Quit', True, white)

    while done == False:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(110, 440) and pos[1] in range(550, 660) and q == 0:
                    q += 1
                if pos[0] in range(540, 880) and pos[1] in range(550, 660) and q == 0:
                    close += 1

                if pos[0] in range(115, 450) and pos[1] in range(540, 605):
                    click, m = 0, 0
                    if flip == 0:
                        if q in [10, 11]:
                            y = 1                        
                        elif q in [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15]:
                            if double != 1:
                                y += -1
                            elif double == 1:
                                y += -0.5
                    elif flip == 1:
                        y = 1
                if pos[0] in range(550, 915) and pos[1] in range(540, 605):
                    click, m = 1, 1
                    if q in [3, 5, 6, 8, 9, 15]:
                        y = 1
                    elif q in [1, 2, 4, 7, 10, 11, 12, 13, 14, 15]:
                        if double != 1:
                            y += -1
                        elif double == 1:
                            y += -0.5
                if pos[0] in range(115, 450) and pos[1] in range(630, 685):
                    click, m = 2, 2
                    if q in [2, 12, 14]:
                        y = 1
                    elif q in [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]:
                        if double != 1:
                            y += -1
                        elif double == 1:
                            y += -0.5
                if pos[0] in range(550, 915) and pos[1] in range(630, 685):
                    click, m = 3, 3
                    if q in [1, 4, 7, 13]:
                        y = 1
                    elif q in [2, 3, 5, 6, 8, 9, 10, 11, 12, 14, 15]:
                        if double != 1:
                            y += -1
                        elif double == 1:
                            y += -0.5

                if q != 0 and pos1[0] in range(720, 825) and pos1[1] in range(60, 115):
                    print '50:50'
                    fifty += 1
                if q != 0 and pos1[0] in range(845, 950) and pos1[1] in range(60, 115):
                    print 'Double dip'
                    double += 1
                if q != 0 and pos1[0] in range(720, 825) and pos1[1] in range(135, 190):
                    print 'Flip the Question'
                    flip += 1
                if q != 0 and pos1[0] in range(845, 950) and pos1[1] in range(135, 190):
                    print 'Quit'
                    close += 1
                        
        pos1 = pygame.mouse.get_pos()        
        lc = [black, black, black, black]
        
        if q != 0:
            current1 = font1.render('Current question for:', True, white)
            current2 = font1.render('Rs' + str(money[q]), True, white)
            winning1 = font1.render('Currently winning:', True, white)
            winning2 = font1.render('Rs' + str(money[q-1]), True, white)
        
        screen.fill(white)
        
        if q != 0:
            screen.blit(pic1, [0, 0])
        
        if q == 0:
            screen.blit(pic3, [0, 0])
            
        if click in [0, 1, 2, 3]:
            lc[click] = yellow

        if q in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
            if flip != 1 and double != 1:
                if q in [1, 4, 7, 13]:
                    if (y == 1 or y == -1) and click == -1:
                        lc[3] = green
                        if y == -1:
                            lc[m] = red
                elif q in [2, 12, 14]:
                    if (y == 1 or y == -1) and click == -1:
                        lc[2] = green
                        if y == -1:
                            lc[m] = red
                elif q in [3, 5, 6, 8, 9, 15]:
                    if (y == 1 or y == -1) and click == -1:
                        lc[1] = green
                        if y == -1:
                            lc[m] = red
                elif q in [10, 11]:
                    if (y == 1 or y == -1) and click == -1:
                        lc[0] = green
                        if y == -1:
                            lc[m] = red
            elif double == 1:
                if q in [1, 4, 7, 13]:
                    if (y == 1 or y == -1 or y == -0.5) and click == -1:
                        if y == 1:
                            lc[3] = green
                        if y == -1 or y == -0.5:
                            lc[m] = red
                elif q in [2, 12, 14]:
                    if (y == 1 or y == -1 or y == -0.5) and click == -1:
                        if y == 1:
                            lc[2] = green
                        if y == -1 or y == -0.5:
                            lc[m] = red
                elif q in [3, 5, 6, 8, 9, 15]:
                    if (y == 1 or y == -1 or y == -0.5) and click == -1:
                        if y == 1:
                            lc[1] = green
                        if y == -1 or y == -0.5:
                            lc[m] = red
                elif q in [10, 11]:
                    if (y == 1 or y == -1 or y == -0.5) and click == -1:
                        if y == 1:
                            lc[0] = green
                        if y == -1 or y == -0.5:
                            lc[m] = red 
                    
            elif flip == 1:
                screen.blit(pic1, [0, 0])
                if (y == 1 or y == -1) and click == -1:
                    if y == 1:
                        lc[0] = green
                    if y == -1 or y == -0.5:
                        lc[m] = red
                
            pygame.draw.polygon(screen, lc[0], [[90,570], [115,540], [450,540], [480, 570], [450, 600], [115, 600]])
            pygame.draw.polygon(screen, lc[1], [[525,570], [555,540], [887,540], [915, 570], [888, 600], [555, 600]])
            pygame.draw.polygon(screen, lc[2], [[90,660], [115,630], [450,630], [480, 660], [450, 690], [115, 690]])
            pygame.draw.polygon(screen, lc[3], [[525,660], [555,630], [887,630], [915, 660], [888, 690], [555, 690]])

            if flip != 1:
                if q == 1:
                    Question1()
                elif q == 2:
                    Question2()
                elif q == 3:
                    Question3()
                elif q == 4:
                    Question4()
                elif q == 5:
                    Question5()
                elif q == 6:
                    Question6()
                elif q == 7:
                    Question7()
                elif q == 8:
                    Question8()
                elif q == 9:
                    Question9()
                elif q == 10:
                    Question10()
                elif q == 11:
                    Question11()
                elif q == 12:
                    Question12()
                elif q == 13:
                    Question13()
                elif q == 14:
                    Question14()
                elif q == 15:
                    Question15()
            else:
                Extra()
            
        if q != 0:
            screen.blit(pic2, [710, 50])
            screen.blit(current1, [710, 240])
            screen.blit(current2, [710, 265])
            screen.blit(winning1, [710, 310])
            screen.blit(winning2, [710, 335])
        if q != 0 and pos1[0] in range(720, 825) and pos1[1] in range(60, 115):
            screen.blit(t1, [10, 10])
        if q != 0 and pos1[0] in range(845, 950) and pos1[1] in range(60, 115):
            screen.blit(t2, [10, 10])
        if q != 0 and pos1[0] in range(720, 825) and pos1[1] in range(135, 190):
            screen.blit(t3, [10, 10])
        if q != 0 and pos1[0] in range(845, 950) and pos1[1] in range(135, 190):
            screen.blit(t4, [10, 10])
            
        pygame.display.flip()
        
        if click in [0, 1, 2, 3]:
            time.sleep(1)
            click = -1
        elif y == 1:
            time.sleep(1)
            if flip == 1:
                flip = -100
            if double == 1:
                double = -100
            if fifty == 1:
                fifty = -100
            if q < 15:
                 q += 1
            y = 0
        elif y == -1 or q > 15 or close == 1:
            time.sleep(1)
            print 'Game Over'
            #global credit
            #credit += money[q-1]
            break
        clock.tick(100)
    print 'You have won', money[q-1]
