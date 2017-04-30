import pygame
import math
import random
import time
import Games

pi=math.pi

tym = time.strftime("%H:%M:%S")
date = time.strftime("%d/%m/%Y")
z = 0
dt = ''
for i in date:
    dt = dt + i
    z += 1
    if z == 2:
        break
odt = int(dt)
z = 0
ty = ''
for i in tym:
    ty = ty + i
    z += 1
    if z == 2:
        break
oty = int(ty)
    
#print dt + time.strftime('/%m/%Y')
#print ty + time.strftime(':%M:%S')

black   = [   0,   0,   0]
white   = [ 255, 255, 255]
red     = [ 255,   0,   0]
green   = [   0, 255,   0]
blue    = [   0,   0, 255]
yellow  = [ 245, 239,  59]

def Store():       
    def draw_stick_figure(x_coord, y_coord):
        #Head
        pygame.draw.ellipse(screen, black,[1 + x_coord, y_coord, 10, 10])

        #Legs
        pygame.draw.line(screen, black, [5 + x_coord, 17 + y_coord],[10 + x_coord, 27 + y_coord], 2)
        pygame.draw.line(screen, black, [5 + x_coord, 17 + y_coord],[x_coord, 27 + y_coord], 2)

        #Body
        pygame.draw.line(screen, red, [5 + x_coord, 17 + y_coord],[5 + x_coord,7 + y_coord], 2)

        #Arms
        pygame.draw.line(screen, black, [5 + x_coord, 7 + y_coord],[9 + x_coord, 17 + y_coord], 2)
        pygame.draw.line(screen, black, [5 + x_coord, 7 + y_coord],[1 + x_coord, 17 + y_coord], 2)    
        
    pygame.init()

    size = [1000,708]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Al Khor Community Supermarket')

    pic9 = pygame.image.load("layout.jpg").convert()

    continues = 5
    sumn = 0
    ext = 0
    done = False

    clock = pygame.time.Clock()

    pygame.mouse.set_visible(1)

    font = pygame.font.Font(None, 40)
    font1 = pygame.font.Font(None, 35)
    font2 = pygame.font.Font(None, 30)

    x_coord = 450
    y_coord = 650

    x_speed = 0
    y_speed = 0
    tr = 0
    
    global credit
    global cash

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x_coord = pos[0]
                y_coord = pos[1]
                           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed = -5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP:
                    y_speed = 0
                elif event.key == pygame.K_DOWN:
                    y_speed = 0
                    
            #Trolley
            if x_coord in range(0,55) and y_coord in range(520,708):
                print "You Have Taken A Trolley"
                tr = 1

                x_coord = 450
                y_coord = 650
            
            #Frozen Food
            elif x_coord in range(75,455) and y_coord in range(0,65):
                if tr == 1:
                    continues = 5
                    while continues == 5:
                        print
                        print "What Do You Want To Buy >>> "
                        print
                        print "1) Al Marai Full Fat Milk 2L(QR. 11)"
                        print "2) Al Marai Vetal Milk 2L (QR. 12)"
                        print "3) Amul Paneer 200gms (QR. 6)"
                        print "4) Amul Paneer 500gms (QR. 13)"
                        print "5) Amul Butter 250gms (QR. 5)"
                        print "6) Al Marai Full Fat Yogurt 1L (QR. 10)"
                        print "7) Al Marai Low Fat  Yogurt 500 mL (QR. 5)"
                        print
                        print "Hit 100 to exit"
                        print
                        item_number = input("Enter Item Number >>> ")
                        selection = {1:11,2:12,3:10,4:18,5:5,6:10,7:5}
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co.lower() in ("yes","y","ya", "yeah"):
                                continues = 5
                            elif co.lower() in ("no","n","nope","na"):
                                continues = 100
                        elif item_number == 100:
                            continues = 100
                        else:
                            print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                            item_number = input("Enter Item Number >>> ")
                            if item_number in selection:
                                quantity = input("Enter Quantity >>> ")
                                sumn = sumn + (selection[item_number]*quantity)
                                co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                                if co.lower() in ("yes","y","ya", "yeah"):
                                    continues = 5
                                elif co.lower() in ("no","n","nope","na"):
                                    continues = 100
                else:
                    print 'Please get yourself a trolley'
                            
                x_coord = 450
                y_coord = 650
            #Dairy Products
            elif x_coord in range(515,850) and y_coord in range(0,65):
                if tr == 1:
                    continues = 5
                    while continues == 5:
                        print
                        print "Welcome To Dairy Section."
                        print
                        print "1) Al Marai Full Fat Milk 2L(QR. 11)"
                        print "2) Al Marai Vetal Milk 2L (QR. 12)"
                        print "3) Amul Paneer 250gms (QR. 10)"
                        print "4) Amul Paneer 500gms (QR. 18)"
                        print "5) Amul Butter 250gms (QR. 5)"
                        print
                        print "Hit 100 to exit"
                        print
                        item_number = input("Enter Item Number >>> ")
                        selection = {1:11,2:12,3:10,4:18,5:5}
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co.lower() in ("yes","y","ya", "yeah"):
                                continues = 5
                            elif co.lower() in ("no","n","nope","na"):
                                continues = 100
                        elif item_number == 100:
                            continues = 100
                        else:
                            print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                            item_number = input("Enter Item Number >>> ")
                            if item_number in selection:
                                quantity = input("Enter Quantity >>> ")
                                sumn = sumn + (selection[item_number]*quantity)
                                co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                                if co.lower() in ("yes","y","ya", "yeah"):
                                    continues = 5
                                elif co.lower() in ("no","n","nope","na"):
                                    continues = 100
                else:
                    print 'Please get yourself a trolley'
                x_coord = 450
                y_coord = 650

            #Food
            elif x_coord in range(0,55) and y_coord in range(115,265):
                if tr == 1 :
                    continues = 5
                    while continues == 5:
                        print
                        print "Welcome To the Restaurant."
                        print
                        print "1) Falafel Sandwich(QR. 3)"
                        print "2) Chicken Shawarma (QR. 6)"
                        print "3) Croissant (QR. 2)"
                        print "4) Vada (QR. 2)"
                        print "5) Veg Burger (QR. 7)"
                        print "6) Chicken Burger (QR. 8)"
                        print "7) Veg Club Sandwich (QR. 6)"
                        print "8) Chicken Nuggets (QR. 6)"
                        print "9) French Fries (QR. 5)"
                        print "10) Garlic Cheese Bread (QR. 3)"
                        print
                        print "Hit 100 to exit"
                        print
                        item_number = input("Enter Item Number >>> ")
                        selection = {1:3,2:6,3:2,4:2,5:7,6:8,7:6,8:6,9:5,10:3}
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co.lower() in ("yes","y","ya", "yeah"):
                                continues = 5
                            elif co.lower() in ("no","n","nope","na"):
                                continues = 100
                        elif item_number == 100:
                            continues = 100
                        else:
                            print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                            item_number = input("Enter Item Number >>> ")
                            if item_number in selection:
                                quantity = input("Enter Quantity >>> ")
                                sumn = sumn + (selection[item_number]*quantity)
                                co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                                if co.lower() in ("yes","y","ya", "yeah"):
                                    continues = 5
                                elif co.lower() in ("no","n","nope","na"):
                                    continues = 100
                else:
                    print 'Please get yourself a trolley'
                x_coord = 450
                y_coord = 650
            #Products
            elif x_coord in range(0,55) and y_coord in range(300,475):
                if tr == 1:
                    continues = 5
                    while continues == 5:
                        print
                        print "Welcome To Products Section."
                        print
                        print "1) Al Meera Cornflakes (QR. 16 )"
                        print "2) Al Meera Honey (QR. 45)"
                        print "3) Al Meera Water 500 mL (QR. 1)"
                        print "4) Al Meera Water 1 L (QR. 1.5)"
                        print "5) Al Meera Tissue Box(QR. 4)"
                        print "6) Al Meera Ball Pen 3pcs(QR. 5)"
                        print "7) Al Meera Pencils 12pcs(QR. 4)"
                        print
                        print "Hit 100 to exit"
                        print
                        item_number = input("Enter Item Number >>> ")
                        selection = {1:16,2:45,3:1,4:1.5,5:4,6:5,7:4}
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co.lower() in ("yes","y","ya", "yeah"):
                                continues = 5
                            elif co.lower() in ("no","n","nope","na"):
                                continues = 100
                        elif item_number == 100:
                            continues = 100
                        else:
                            print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                            item_number = input("Enter Item Number >>> ")
                            if item_number in selection:
                                quantity = input("Enter Quantity >>> ")
                                sumn = sumn + (selection[item_number]*quantity)
                                co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                                if co.lower() in ("yes","y","ya", "yeah"):
                                    continues = 5
                                elif co.lower() in ("no","n","nope","na"):
                                    continues = 100
                else:
                    print 'Please get yourself a trolley'
                x_coord = 450
                y_coord = 650
                    
            #Utilities
            elif x_coord in range(115,380) and y_coord in range(160,450):
                if tr == 1:
                    continues = 5
                    while continues == 5:
                        print
                        print "Welcome To Utilities Section."
                        print
                        print "1) Clorox Bleach 500 mL(QR. 10)"
                        print "2) Clorox Bleach 1 L (QR. 15)"
                        print "3) OMO Top Load 1Kg (QR. 7)"
                        print "4) OMO Top Load 5Kg (QR. 25)"
                        print "5) OMO Top Load 10Kg (QR. 60)"
                        print
                        print "Hit 100 to exit"
                        print
                        item_number = input("Enter Item Number >>> ")
                        selection = {1:10,2:15,3:7,4:25,5:60}
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co.lower() in ("yes","y","ya", "yeah"):
                                continues = 5
                            elif co.lower() in ("no","n","nope","na"):
                                continues = 100
                        elif item_number == 100:
                            continues = 100
                        else:
                            print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                            item_number = input("Enter Item Number >>> ")
                            if item_number in selection:
                                quantity = input("Enter Quantity >>> ")
                                sumn = sumn + (selection[item_number]*quantity)
                                co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                                if co.lower() in ("yes","y","ya", "yeah"):
                                    continues = 5
                                elif co.lower() in ("no","n","nope","na"):
                                    continues = 100
                else:
                    print 'Please get yourself a trolley'
                x_coord = 450
                y_coord = 650
                        
            #Fresh Food & Packed Food
            elif x_coord in range(425,850) and y_coord in range(130,475):
                if tr == 1:
                    continues = 5
                    while continues == 5:
                        print
                        print "Welcome To Fresh Food & Packed Food Section."
                        print
                        print "1) Al Marai Full Fat Milk 2L(QR. 11)"
                        print "2) Al Marai Vetal Milk 2L (QR. 12)"
                        print "3) Amul Paneer 250gms (QR. 10)"
                        print "4) Amul Paneer 500gms (QR. 18)"
                        print "5) Amul Butter 250gms (QR. 5)"
                        print
                        print "Hit 100 to exit"
                        print
                        item_number = input("Enter Item Number >>> ")
                        selection = {1:11,2:12,3:10,4:18,5:5,6:10,7:5}
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co.lower() in ("yes","y","ya", "yeah"):
                                continues = 5
                            elif co.lower() in ("no","n","nope","na"):
                                continues = 100
                        elif item_number == 100:
                            continues = 100
                        else:
                            print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                            item_number = input("Enter Item Number >>> ")
                            if item_number in selection:
                                quantity = input("Enter Quantity >>> ")
                                sumn = sumn + (selection[item_number]*quantity)
                                co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                                if co.lower() in ("yes","y","ya", "yeah"):
                                    continues = 5
                                elif co.lower() in ("no","n","nope","na"):
                                    continues = 100
                else:
                    print 'Please get yourself a trolley'
                x_coord = 450
                y_coord = 650
       
            #Deli & Bakery
            elif x_coord in range(900,1000) and y_coord in range(240,700):
                if tr == 1:
                    continues = 5
                    while continues == 5:
                        print
                        print "Welcome To Deli & Bakery Section."
                        print
                        print "1) London Bakery White Bread(QR. 11)"
                        print "2) London Bakery Brown Bread (QR. 12)"
                        print "3) London Bakery Multigrain Bread (QR. 15)"
                        print "4) London Bakery Croissant (QR. 2)"
                        print "5) London Bakery Muffins  (QR. 1)"
                        print
                        print "Hit 100 to exit"
                        print
                        item_number = input("Enter Item Number >>> ")
                        selection = {1:11,2:12,3:15,4:2,5:1}
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co.lower() in ("yes","y","ya", "yeah"):
                                continues = 5
                            elif co.lower() in ("no","n","nope","na"):
                                continues = 100
                        elif item_number == 100:
                            continues = 100
                        else:
                            print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                            item_number = input("Enter Item Number >>> ")
                            if item_number in selection:
                                quantity = input("Enter Quantity >>> ")
                                selection = {1:11,2:12,3:10,4:18,5:5,6:10,7:5}
                                sumn = sumn + (selection[item_number]*quantity)
                                co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                                if co.lower() in ("yes","y","ya", "yeah"):
                                    continues = 5
                                elif co.lower() in ("no","n","nope","na"):
                                    continues = 100
                else:
                    print 'Please get yourself a trolley'
                x_coord = 450
                y_coord = 650

            #Cashier
            elif x_coord in range(240,720) and y_coord in range(545,615):
                print
                co = raw_input("Do You Want To Checkout And Exit ?")
                if co.lower() in ("yes","y","ya","yeah"):
                    if sumn == 0:
                        print 'Thank You for shopping'
                        ext = 1
                    else:
                        print "The Amounnt To Be Paid Is Qr",sumn
                        print "How Would You Like To Pay It ?"
                        while 1:
                            ans = raw_input('Credit card/ Cash:')
                            if ans.lower() == 'credit card':
                                if credit < sumn:
                                    print 'Not enough money'
                                else:
                                    credit -= sumn
                                    print 'Amount successfully paid'
                                    print 'Thank You for shopping'
                                    ext = 1
                                    break
                            elif ans.lower() == 'cash':
                                if cash < sumn:
                                    print 'Not enough money'
                                else:
                                    cash -= sumn
                                    print 'Amount successfully paid'
                                    print 'Thank You for shopping'
                                    ext = 1
                                    break
                            else:
                                print 'Invalid Input' 
                else:
                    x_coord = 450
                    y_coord = 650
                      
        #All event processing above this comment
                
        #All logic below
        
        x_coord += x_speed
        y_coord += y_speed
        
        #All logic above

        screen.fill(white)

        #All code to draw below this comment
        screen.blit(pic9,(0,0))
        draw_stick_figure(x_coord, y_coord)
        if ext == 1:
            break
        #All code to draw above this comment

        pygame.display.flip()
        
        clock.tick(60)

def kbc():
    pygame.init()

    money = {0:'0', 1:'250', 2:'500', 3:'1000', 4:'2000', 5:'4000', 6:'8000', 7:'16000', 8:'32000', 9:'64000', 10:'125000', 11:'250000', 12:'500000', 13:'1000000', 14:'2000000', 15:'5000000'}

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
    t5 = font3.render('X', True, red)

    while done == False:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print pos
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
                    fifty += 1
                    if fifty == 1:
                        print '50:50'
                if q != 0 and pos1[0] in range(845, 950) and pos1[1] in range(60, 115):
                    double += 1
                    if double == 1:
                        print 'Double dip'
                if q != 0 and pos1[0] in range(720, 825) and pos1[1] in range(135, 190):
                    flip += 1
                    if flip == 1:
                        print 'Flip the question'
                if q != 0 and pos1[0] in range(845, 950) and pos1[1] in range(135, 190):
                    close += 1
                        
        pos1 = pygame.mouse.get_pos()        
        lc = [black, black, black, black]
        
        if q != 0:
            current1 = font1.render('Current question for:', True, white)
            current2 = font1.render('QR ' + str(money[q]), True, white)
            winning1 = font1.render('Currently winning:', True, white)
            winning2 = font1.render('QR ' + str(money[q-1]), True, white)
        
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
        if double < 0:
            screen.blit(t5, [880, 62])
        if flip < 0:
            screen.blit(t5, [750, 135])
        if fifty < 0:
            screen.blit(t5, [750, 62])            
            
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
            global credit
            credit += int(money[q-1])
            break
        clock.tick(100)
    print 'You Have Won', money[q-1]

class Student():
    def __init__(self):
        self.name=''
        self.s1=0
        self.s2=0
        self.s3=0
        self.s4=0
        self.s5=0
        self.total=0
        self.percentage=0
        self.outof=0
    def inputdata(self):
        self.name=raw_input('Enter student\'s name:')
        self.s1=input('English:')
        self.s2=input('Physics:')
        self.s3=input('Computer Science:')
        self.s4=input('Chemistry:')
        self.s5=input('Maths:')
        self.outof=input('Exam is out of:')
        self.compute_percentage()
    def compute_percentage(self):
        self.total=self.s1+self.s2+self.s3+self.s4+self.s5
        self.percentage=(self.total/5.0)*100/self.outof
    def showdata(self):
        print '**************************************************'
        print 'Name:',self.name
        print
        print 'English                 :',self.s1
        print 'Physics                 :',self.s2
        print 'Computer Science        :',self.s3
        print 'Chemistry               :',self.s4
        print 'Maths                   :',self.s5
        print 'Total marks             :',self.total
        print 'Percentage              :',self.percentage
        print '**************************************************'

class IDPass():
    def __init__(self):
        self.name = "No Name Given."
        self.dob = "No Date Of Birth Given."
        self.pno = "No Phone Number Given."
        self.dur = "No Duration of Stay Given."
        self.id = 'TM' + str(random.randint(1000, 3000))

    def inp(self):
        while 1:
            self.mem = raw_input('Are you a member of this community?(Y/N)')
            if self.mem in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                nm = raw_input('Enter your name:')
                idd = raw_input('Enter your Id:')
                check = nm + ',' + idd
                with open('IDs.txt', 'r') as f:
                    if check in f.readlines():
                        print 'You may pass'
                        self.mem = 1
                    else:
                        print 'You are not a member so please make your visiting card'
            elif self.mem == 1:
                break
            else:
                self.mem = 0
                self.name = raw_input("Enter Name Of Visitor      :")
                self.dob = raw_input("Enter Date Of Birth        :")
                self.pno = raw_input("Enter Phone Number         :")
                self.dur = raw_input("Enter Duration Of Stay     :")
                while int(self.dur) >= 5:
                    print 'You can\'t stay in the community for any longer than 4 days if you are not a member.'
                    self.dur = raw_input("Enter Duration Of Stay     :")
                break

    def printing(self):
        print
        print "---------------------------------------------------"
        print "                 Visiting Card                    "
        print "---------------------------------------------------"
        print
        print "    Name              :", self.name
        print "    Date Of Birth     :", self.dob
        print "    Phone Number      :", self.pno
        print "    Duration Of Stay  :", self.dur
        print "    ID Number         :", self.id
        print
        print "---------------------------------------------------"

def maping():
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

    text = font.render('Exit', True, black)
    screen.blit(text, [42, 42])

    text1 = font2.render('Youth Club', True, black)
    screen.blit(text1, [130, 550])

    text2 = font2.render('Al Meera', True, black)
    screen.blit(text2, [695, 550])

    text3 = font2.render('Home', True, black)
    screen.blit(text3, [380, 100])

    text4 = font2.render('School', True, black)
    screen.blit(text4, [600, 300])

    text5 = font2.render('Clinic', True, black)
    screen.blit(text5, [155, 300])

    text6 = font2.render('Gate', True, black)
    screen.blit(text6, [388, 650])

def draw_stick_figure(x_coord, y_coord):
    #Head
    pygame.draw.ellipse(screen, black,[1 + x_coord, y_coord, 10, 10])

    #Legs
    pygame.draw.line(screen, black, [5 + x_coord, 17 + y_coord],[10 + x_coord, 27 + y_coord], 2)
    pygame.draw.line(screen, black, [5 + x_coord, 17 + y_coord],[x_coord, 27 + y_coord], 2)

    #Body
    pygame.draw.line(screen, red, [5 + x_coord, 17 + y_coord],[5 + x_coord,7 + y_coord], 2)

    #Arms
    pygame.draw.line(screen, black, [5 + x_coord, 7 + y_coord],[9 + x_coord, 17 + y_coord], 2)
    pygame.draw.line(screen, black, [5 + x_coord, 7 + y_coord],[1 + x_coord, 17 + y_coord], 2)

def gate():
    pygame.draw.line(screen, black, [50, 50], [950, 50], 2)
    pygame.draw.line(screen, black, [50, 50], [50, 550], 2)
    pygame.draw.line(screen, black, [50, 550], [550, 550], 2)
    pygame.draw.line(screen, black, [950, 50], [950, 550], 2)
    pygame.draw.line(screen, black, [950, 550], [800, 550], 2)

    #Main gate shape
    pygame.draw.arc(screen, black, [550, 250, 250, 200], 0, pi, 2)
    pygame.draw.line(screen, black, [550, 340], [550, 550], 2)
    pygame.draw.line(screen, black, [800, 340], [800, 550], 2)

    pygame.draw.rect(screen, black, [180, 250, 250, 200], 2)#Map

    t1 = font.render('Al Khor Community Gate', True, black)
    screen.blit(t1, [330, 100])

    t2 = font1.render('Community Map', True, black)
    screen.blit(t2, [200, 275])

def school():
    screen.blit(pic6, [522, 120])
    screen.blit(pic12, [650, 450])

    for i in range(13):
        screen.blit(pic8, [930, i * 50])
    for i in range(13):
        screen.blit(pic8, [i * 70 + 10, 0])

    '''for i in range(9):
        for j in range(2):
            screen.blit(pic3, [j*35 + 450, i * 35 + 382])
    for i in range(2):
        for j in range(19):
            screen.blit(pic3, [j*35, 325 + i * 35])
    for i in range(3):
        screen.blit(pic3, [650, i * 35 + 290])'''

def store():
    screen.blit(pic2, [145, 100])

    for i in range(13):
        if i in range(5,7):
            continue
        else:
            screen.blit(pic8, [i*70 + 70, 600])
    for i in range(13):
        screen.blit(pic8, [0, i*50])

    '''for i in range(20):
        for j in range(2):
            screen.blit(pic3, [j*35 + 450, i * 35])
    for i in range(2):
        for j in range(8):
            screen.blit(pic3, [j*35 + 168, 420 + i * 35])
    for i in range(2):
        for j in range(14):
            screen.blit(pic3, [j*35 + 520, 315 + i * 35])'''

def club_clinic():
    screen.blit(pic4, [145, 100])
    screen.blit(pic5, [600, 330])

    for i in range(13):
        screen.blit(pic8, [920, i * 50])
    for i in range(13):
        screen.blit(pic8, [i*70, 600])

    '''for i in range(15):
        for j in range(2):
            screen.blit(pic3, [j*35 + 450, i * 35])
    for i in range(2):
        for j in range(13):
            screen.blit(pic3, [j*35, 315 + i * 35])
    for i in range(7):
        screen.blit(pic3, [i * 35 + 495, 490])'''

def house():
    screen.blit(pic7, [400, 225])

    for i in range(14):
        screen.blit(pic8, [i*70, 0])
    for i in range(13):
        screen.blit(pic8, [0, i*50])

    '''for i in range(9):
        for j in range(2):
            screen.blit(pic3, [j*35 + 450, 390+i*35])
    for i in range(2):
        for j in range(9):
            screen.blit(pic3, [j*35 + 750, 325 + i * 35])
    for i in range(2):
        for j in range(9):
            screen.blit(pic3, [j*35 + 520, 430 + i * 35])
    for i in range(2):
        screen.blit(pic3, [i * 35 + 750, 395])
'''
def text1():
    detail = 0
    if KKK >= 2 and pos[0] in range(800, 950) and pos[1] in range(10, 60):
        detail = 1 
    if detail == 0:
        t8 = font2.render('Details', True, black)
        screen.blit(t8, [825, 25])
        pygame.draw.rect(screen, black, [800, 10, 150, 50], 1)
    elif detail == 1:
        pygame.draw.rect(screen, black, [700, 10, 250, 210], 1)
        t9 = font2.render('Name : ' + Name, True, black)
        t10 = font2.render('Id  : ' + Id, True, black)
        t11 = font2.render('Phone number: ' + Ph, True, black)
        t12 = font2.render('Credit: ' + str(credit), True, black)
        t13 = font2.render('Date: ' + dt + time.strftime('/%m/%Y'), True, black)
        t14 = font2.render('Time: ' + ty + time.strftime(':%M:%S'), True, black)
        t15 = font2.render('Last day: ' + str(ldt) + time.strftime('/%m/%Y'), True, black) 

        screen.blit(t9, [710, 15])
        screen.blit(t10, [710, 45])
        screen.blit(t11, [710, 75])
        screen.blit(t12, [710, 105])
        screen.blit(t13, [710, 135])
        screen.blit(t14, [710, 165])
        screen.blit(t15, [710, 195])
        
        detail -= 1

KKK = 0
days = 0
day = 10000
cash = 0
bal = 0
#####

pygame.init()
pygame.mixer.init()

size = [1000,700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Al Khor Community Gate')
pic1 = pygame.image.load('grass.png')
pic2 = pygame.image.load('store.png')
#pic3 = pygame.image.load('road.png')
pic4 = pygame.image.load('clinic.png')
pic5 = pygame.image.load('club.png')
pic6 = pygame.image.load('school.png')
pic7 = pygame.image.load('house.png')
pic8 = pygame.image.load('tree.png')
pic9 = pygame.image.load('gate.png')
pic12 = pygame.image.load('pond.png')

sound = pygame.mixer.Sound("Elevator Music Careless Whisper (Alto Sax score).mp3")

done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(1)

#pygame.mixer.music.load("sound.ogg")
#pygame.mixer.music.play(-1)

font = pygame.font.Font(None, 40)
font1 = pygame.font.Font(None, 35)
font2 = pygame.font.Font(None, 30)
font3 = pygame.font.Font(None, 80)

x_coord = 450
y_coord = 650

x_speed = 0
y_speed = 0

while done == False:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_coord = pos[0]
            y_coord = pos[1]
            #print pos

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP:
                y_speed = 0
            elif event.key == pygame.K_DOWN:
                y_speed = 0

        #MAP
        if KKK == 0 and x_coord in range(180, 430) and y_coord in range(250, 450) and (day - days) != 0:
            x_coord = -10
            y_coord = -10

            KKK += 1

        #gate
        if KKK == 1 and x_coord in range(25, 125) and y_coord in range(25, 125) and (day - days) != 0:
            x_coord = 480
            y_coord = 675

            KKK -= 1

        if KKK == 2 and x_coord in range(425, 500) and y_coord > 700:
            KKK -= 3

        #Entry Pass
        if  KKK == 0 and x_coord in range(550, 800) and y_coord in range(340, 550):
            print 'Before you enter our community, you will have to follow the following '
            print 'Rule and Regulations:'
            print
            print '1) You will be appointed a temporary house for the number of days you'
            print '   intend to stay.'
            print '2) The information you give us on entering the community will be used'
            print '   to access the facilities.'
            print '3) To call a day off you have to rest at home.'
            print '4) After the number of days of stay is over you will not be granted any'
            print '   service.'
            print
            print 'After you have read the rules'
            print 'a) Agree'
            print 'b) Disagree'
            print
            ans = raw_input('Enter your choice:')
            print
            print '=' * 80
            print
            if ans in ['a', 'A']:
                print "Welcome To Al Khor Community Security Gate System. Enter Following Information."
                print
                c = IDPass()
                c.inp()
                c.printing()
                print
                print 'Before entering our community, we will provide you with a credit card'
                while 1:
                    pin = raw_input('Choose the 4 digit pin')
                    if len(pin) == 4 and pin.isdigit():
                        break
                    else:
                        print 'Invalid input'
                print
                credit = 5000
                print 'You have a balance of', credit
                print
                print '=' * 80
                print
                day = int(c.dur)
                Name = c.name
                Id = c.id
                Ph = c.pno
                mem = c.mem
                ldt = odt + day
                
                x_coord = 480
                y_coord = 675

                KKK += 2
            else:
                print 'Sorry, you will not be allowed into the community'
                KKK -= 1          
        
        #sc2 from sc1
        if KKK == 2 and x_coord in range(450, 520) and y_coord <=0:
            x_coord = 480
            y_coord = 675

            KKK += 1

        #back to sc1 from sc2
        if KKK == 3 and x_coord in range(450, 520) and y_coord >=700:
            x_coord = 480
            y_coord = 5

            KKK -= 1

        #sc4 from sc1
        if KKK == 2 and x_coord > 1000 and y_coord in range(320, 390):
            x_coord = 5
            y_coord = 340

            KKK += 3

        #sc3 from sc2
        if KKK == 3 and x_coord > 1000 and y_coord in range(325, 400):
            x_coord = 5
            y_coord = 340

            KKK += 1

        #back to sc3 from sc4
        if KKK == 5 and x_coord in range(450, 525) and y_coord < 0:
            x_coord = 480
            y_coord = 680

            KKK -= 1

        #back to sc2 from sc3
        if KKK == 4 and x_coord < 0 and y_coord in range(325, 400):
            x_coord = 985
            y_coord = 340

            KKK -= 1

        #back to sc1 from sc4
        if KKK == 5 and x_coord < 0 and y_coord in range(320, 390):
            x_coord = 985
            y_coord = 340

            KKK -= 3

        #back to sc4 from sc3
        if KKK == 4 and x_coord in range(450, 525) and y_coord > 700:
            x_coord = 480
            y_coord = 5

            KKK += 1

        #house
        if KKK == 3 and x_coord in range(465, 515) and y_coord in range(365, 385) and (ldt - int(dt)) != 0:
            x_coord = 480
            y_coord = 390

            KKK += 4

        #school
        if KKK == 4 and x_coord in range(660, 685) and y_coord in range(255, 285) and (ldt - int(dt)) != 0:
            x_coord = 665
            y_coord = 290

            if int(ty) < 17 or int(ty) > 9:
                KKK += 4
            else:
                print 'School is closed. Please come between 9:00 am and 5:00 pm'

        #club
        if KKK == 5 and x_coord in range(695, 720) and y_coord in range(445, 470) and (ldt - int(dt)) != 0:
            x_coord = 700
            y_coord = 480

            if int(ty) < 17 or int(ty) > 9:
                KKK += 4
            else:
                print 'Club is closed. Please come between 9:00 am and 5:00 pm'

        #clinic
        if KKK == 5 and x_coord in range(260, 280) and y_coord in range(285, 305) and (ldt - int(dt)) != 0:
            x_coord = 265
            y_coord = 315

            if int(ty) < 17 or int(ty) > 9:
                KKK += 5
            else:
                print 'Clinic is closed. Please come between 9:00 am and 5:00 pm'
            
        #Store 1
        if KKK == 2 and x_coord in range(315, 335) and y_coord in range(350, 370) and (ldt - int(dt)) != 0:
            x_coord = 320
            y_coord = 380

            if int(ty) < 17 or int(ty) > 9:
                KKK += 4
            else:
                print 'Store is closed. Please come between 9:00 am and 5:00 pm'

        #store 2
        if KKK == 2 and x_coord in range(205, 225) and y_coord in range(350, 370) and (ldt - int(dt)) != 0:
            x_coord = 210
            y_coord = 380

            if int(ty) < 17 or int(ty) > 9:
                KKK += 4
            else:
                print 'Store is closed. Please come between 9:00 am and 5:00 pm'

    #All event processing above this comment

    #All logic below

    x_coord += x_speed
    y_coord += y_speed

    screen.fill(white)

    #All code to draw below this comment
    if KKK != 0:
        screen.blit(pic1, [0, 0])

    if KKK == -1:
        break

    elif KKK == 0:
        gate()

    elif KKK == 1:
        maping()

    elif KKK == 2:
        store()
        if mem != 1:
            text1()

    elif KKK == 3:
        house()
        if mem != 1:
            text1()

    elif KKK == 4:
        school()
        if mem != 1:
            text1()

    elif KKK == 5:
        club_clinic()
        if mem != 1:
            text1()

    elif KKK == 6:
        Store()
        KKK -= 4
        ty = str(int(ty) + 4)

    elif KKK == 7:#home
        print '=' * 80
        print
        print 'Welcome home'
        z = raw_input('Hit enter to have a good rest')
        dt = str(int(dt) + 1)
        if mem != 1:
            print 'Next day : Day', days + 1, 'of your stay'
        else:
            print 'Next day :', dt + time.strftime('/%m/%Y')
            
        print '=' * 80
        KKK -= 4
        ty = '09'

    elif KKK == 8:#school
        print '=' *80
        print
        print 'Welcome to the school'
        print 'What would you like to do?'
        print
        print '1) Parent Teacher Meeting(PTM)'
        print '2) Amitabh Bachchan has visited the school and is contesting rounds of KBC.'
        print '   Would you like to give it a try? This is your only chance in life.'

        c = input('Your choice:')
        if c == 1:
            s = Student()
            s.inputdata()
            s.compute_percentage()
            s.showdata()
        elif c == 2:
            kbc()
            ty = str(int(ty) + 5)
        print
        print '='*80
        KKK -= 4
        ty = str(int(ty) + 1)

    elif KKK == 9:#club
        print '=' * 80
        print
        print 'Welcome to the club'
        print 'Where you would like to go?'
        print '1) Games'
        print '2) Reception'
        print '3) ATM'
        print
        choice1 = raw_input('Enter your choice:')
        print 
        if choice1 == '1':
            print 'Which game would you like to play'
            print '1) Hangman'
            print '2) Bingo'
            print '3) Tic tac toe'
            print
            choice2 = raw_input('Enter your choice:')
            print
            if choice2 == '1':
                Games.Hangman()
            elif choice2 == '2':
                Games.Bingo()
            elif choice2 == '3':
                Games.Tic_tac_toe()
            else:
                print 'Invalid input'
            ty = str(int(ty) + 2)
        elif choice1 == '2':
            print 'Would you like to become a permanent member?'
            ans = raw_input('Y/N:')
            if ans.lower() in ("yes","y","ya","yeah"):
                print 
                print 'Enter following details as it is in your visiting pass'
                nm = raw_input('Name :')
                idno = raw_input('ID number :')
                print 
                de = nm + ',' + idno + '\n'
                with open('Ids.txt', 'r') as f:
                    if de in f.readlines():
                        print 'This user already exists'
                    else:
                        loop = 1
                with open('IDs.txt', 'a') as f:
                    while 1 and loop == 1:
                        f.write(de)
                        print 'You are now a member of the community'
                        print 'The membership fees are deducted from your account'
                        credit -= 1000
                        break
            else:   
                continue
        elif choice == '3':
            print 'RED CHILLIES ATM machine'
            acc = raw_input("Please enter your account pin number:")
            if acc == pin:
                ans = raw_input('Would you like to see your account balance?(y/n)')
                if ans == 'y':
                    print 'Currrent balance is', credit
                else:
                    continue
                ans = raw_input('Would you like make any transactions?(y/n)')
                if ans.lower() in ("yes","y","ya","yeah"):
                    print 'Which transaction?'
                    print '1) Deposit'
                    print '2) Withdraw'
                    print '3) Exit'
                    choice = raw_input('Enter your choice:')
                    if choice == '1':
                        depo = raw_input('Enter the amount to deposit:')
                        if depo > cash:
                            print 'Transaction Error'
                            print 'You don\'t have enough cash in hand'
                        else:
                            credit += depo
                            cash -= depo
                    elif choice == '2':
                        depo = raw_input('Enter the amount to withdraw:')
                        if depo > credit:
                            print 'Transaction Error'
                            print 'You don\'t have enough credit'
                        else:
                            credit -= depo
                            cash += depo
                    else:
                        print 'Thank you for using our services'
                else:
                    print 'Thank you for using our services'
            else:
                print 'Wrong pin entered'
            
        else:
            print 'Invalid input'
                
        print '=' * 80
        KKK -= 4
        ty = str(int(ty) + 1)
        
    elif KKK == 10:#clinic
        print '=' * 80
        print
        print '                         Welcome to the community clinic'
        print
        print 'Please fill in the details below'
        print
        while 1:
            ID = raw_input('ID Number:')
            if ID != Id:
                print '\n\nThis entry doesn\'t exist in our records'
                print 'Please enter your correct ID number'
            else:
                break
        print '\nWelcome To The Clinic,', Name
        print
        height=input("Please Enter Your Height in Metres: ")
        weight=input("Please Enter Your Weight In Kilograms: ")
        print
        bmi=weight/(height**2)
        print "Your BMI is",bmi
        if bmi<18.5:
            print "You are slightly underweight,"
            
        if 18.5<bmi<25:
            print "You have optimal weight."

        if bmi>25:
            print "You are slightly overweight."
        print
        print
        print
        doctor = ['Dr. Sarah', 'Dr. Andrio', 'Dr. Suman']
        doctor = doctor[random.randint(0,2)]
        print "Your doctor will be",doctor,". Your Room no. will be R",random.randint(1,100)
        print
        print
        q1=raw_input("What Are Your Symptomps ? ")
        dic={'Fever':'1','Cold':'2','Itching':'3','Dandruff':'4','Diabetes':'5','Dry Eyes':'6','Ear Allergies':'7','Hair Loss ':'8','Leg Pain or Cramps':'9','Malaria':'10','Muscle Cramp,':'11','Vomiting':'12','Wrinkles':'13','Sunburn':'14','Urine Acidity':'15'}
        print
        print
        print
        print 'Do you have any of these problems?'
        
        for i in dic.keys():
            print i
        asn = raw_input('>>>(Y/N)')
        if asn.lower() in ("yes","y","ya","yeah"):
            b=raw_input("May I know what is your problem ?")
            print "Okay, I'm prescribing a medicine for this,Please visit the pharmacy for the medicine"
            print
            print"Welcome to the pharmacy.These are your medicines"
            k=0
            l=dic.keys()
            for i in l:
                if (cmp(i,b)==0):
                    b=int(dic[i])
                    if b==1:
                        print "Paracetamol"
                    elif b==2:
                        print "Aspirin"
                    elif b==3:
                        print "Pandel"
                    elif b==4:
                        print "Coal Tar"
                    elif b==5:
                        print "Metformin"
                    elif b==6:
                        print "Protectant"
                    elif b==7:
                        print "Steriodal "
                    elif b==8:
                        print "Minoxidil"
                    elif b==9:
                        print "Quinine"
                    elif b==10:
                        print "Proguanil"
                    elif b==11:
                        print "Dantrolene"    
                    elif b==12:
                        print "Nabilone"
                    elif b==13:
                        print "Botulinum Toxin"
                    elif b==14:
                        print "Adrenocorticoids"
                    elif b==15:
                        print "Citrates "
                    print"Use the medicines as prescribed on the cover."
                    print "We wish you to get well soon"
        else:
            print 'Its good that you are healthy'
        print            
        print"Thanks for visiting our hospital"
        print '=' * 80
        KKK -= 5
        ty = str(int(ty) + 3)

    draw_stick_figure(x_coord, y_coord)

    if KKK == 2:
        screen.blit(pic9, [410, 590])

    #All code to draw above this comment
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
