import pygame

def Store():
    black   = [   0,   0,   0]
    white   = [ 255, 255, 255]
    red     = [ 255,   0,   0]
    green   = [   0, 255,   0]
    blue    = [   0,   0, 255]
    yellow  = [ 245, 239,  59]

        
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
    pygame.mixer.init()

    size = [1000,708]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Al Khor Community Supermarket')

    pic9 = pygame.image.load("layout.jpg").convert()
    sound = pygame.mixer.Sound("Elevator Music Careless Whisper (Alto Sax score).mp3")

    continues = 5
    sumn = 0
    ext = 0
    done = False

    clock = pygame.time.Clock()

    pygame.mouse.set_visible(1)

    pygame.mixer.music.load("sound.ogg")
    pygame.mixer.music.play(-1)

    font = pygame.font.Font(None, 40)
    font1 = pygame.font.Font(None, 35)
    font2 = pygame.font.Font(None, 30)

    x_coord = 450
    y_coord = 650

    x_speed = 0
    y_speed = 0

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
                    
        
            #Frozen Food
            if x_coord in range(75,455) and y_coord in range(0,65):
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
                    item_number = input("Enter Item Number >>> ")
                    selection = {1:11,2:12,3:10,4:18,5:5,6:10,7:5}
                    if item_number in selection:
                        quantity = input("Enter Quantity >>> ")
                        sumn = sumn + (selection[item_number]*quantity)
                        co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                        if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                            continues = 5
                        if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                            continues = 100
                    else:
                        print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                        item_number = input("Enter Item Number >>> ")
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                                continues = 5
                            if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                                continues = 100
                            
                x_coord = 450
                y_coord = 650
            #Dairy Products
            if x_coord in range(515,850) and y_coord in range(0,65):
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
                    item_number = input("Enter Item Number >>> ")
                    selection = {1:11,2:12,3:10,4:18,5:5}
                    if item_number in selection:
                        quantity = input("Enter Quantity >>> ")
                        sumn = sumn + (selection[item_number]*quantity)
                        co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                        if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                            continues = 5
                        if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                            continues = 100
                    else:
                        print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                        item_number = input("Enter Item Number >>> ")
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                                continues = 5
                            if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                                continues = 100
                x_coord = 450
                y_coord = 650

            #Food
            if x_coord in range(0,55) and y_coord in range(115,265):
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
                    item_number = input("Enter Item Number >>> ")
                    selection = {1:3,2:6,3:2,4:2,5:7,6:8,7:6,8:6,9:5,10:3}
                    if item_number in selection:
                        quantity = input("Enter Quantity >>> ")
                        sumn = sumn + (selection[item_number]*quantity)
                        co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                        if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                            continues = 5
                        if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                            continues = 100
                    else:
                        print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                        item_number = input("Enter Item Number >>> ")
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                                continues = 5
                            if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                                continues = 100
                x_coord = 450
                y_coord = 650
            #Products
            if x_coord in range(0,55) and y_coord in range(300,475):
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
                    item_number = input("Enter Item Number >>> ")
                    selection = {1:16,2:45,3:1,4:1.5,5:4,6:5,7:4}
                    if item_number in selection:
                        quantity = input("Enter Quantity >>> ")
                        sumn = sumn + (selection[item_number]*quantity)
                        co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                        if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                            continues = 5
                        if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                            continues = 100
                    else:
                        print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                        item_number = input("Enter Item Number >>> ")
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                                continues = 5
                            if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                                continues = 100
                x_coord = 450
                y_coord = 650
                    
            #Trolley
            if x_coord in range(0,55) and y_coord in range(520,708):
                print "You Have Taken A Trolley"

                x_coord = 450
                y_coord = 650

            #Utilities
            if x_coord in range(115,380) and y_coord in range(160,450):
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
                    item_number = input("Enter Item Number >>> ")
                    selection = {1:10,2:15,3:7,4:25,5:60}
                    if item_number in selection:
                        quantity = input("Enter Quantity >>> ")
                        sumn = sumn + (selection[item_number]*quantity)
                        co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                        if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                            continues = 5
                        if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                            continues = 100
                    else:
                        print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                        item_number = input("Enter Item Number >>> ")
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                                continues = 5
                            if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                                continues = 100
                x_coord = 450
                y_coord = 650
                        
            #Fresh Food & Packed Food
            if x_coord in range(425,850) and y_coord in range(130,475):
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
                    item_number = input("Enter Item Number >>> ")
                    selection = {1:11,2:12,3:10,4:18,5:5,6:10,7:5}
                    if item_number in selection:
                        quantity = input("Enter Quantity >>> ")
                        sumn = sumn + (selection[item_number]*quantity)
                        co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                        if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                            continues = 5
                        if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                            continues = 100
                    else:
                        print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                        item_number = input("Enter Item Number >>> ")
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                                continues = 5
                            if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                                continues = 100
                x_coord = 450
                y_coord = 650
       
            #Deli & Bakery
            if x_coord in range(900,1000) and y_coord in range(240,700):
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
                    item_number = input("Enter Item Number >>> ")
                    selection = {1:11,2:12,3:15,4:2,5:1}
                    if item_number in selection:
                        quantity = input("Enter Quantity >>> ")
                        sumn = sumn + (selection[item_number]*quantity)
                        co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                        if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                            continues = 5
                        if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                            continues = 100
                    else:
                        print "The Given Selection Does Not Exist. Please Enter Valid Item Code"
                        item_number = input("Enter Item Number >>> ")
                        if item_number in selection:
                            quantity = input("Enter Quantity >>> ")
                            selection = {1:11,2:12,3:10,4:18,5:5,6:10,7:5}
                            sumn = sumn + (selection[item_number]*quantity)
                            co = raw_input ("Do You Want To Buy Anything Else From This Section ?")
                            if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                                continues = 5
                            if co in ("no","n","NO","No","nah","NAH","Nah","nope","NOPE","Nope","NA","Na","na"):
                                continues = 100
                x_coord = 450
                y_coord = 650

            #Cashier
            if x_coord in range(240,720) and y_coord in range(545,615):
                co = raw_input("Do You Want To Checkout And Exit ?")
                if co in ("yes","y","YES","Yes","ya","YA","Ya","Yeah","YEAH"):
                    print "The Amounnt To Be Paid Is Qr",sumn
                    print "How Would You Like To Pay It ?"
                    ans = raw_input('Credit card/ Cash:')
                    if ans.lower() == 'credit card':
                        credit -= sumn
                    elif ans.lower() == 'cash':
                        cash -= sumn
                    ext = 1
                else:
                    print 'Happy shopping'
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
    print credit
#Store()
    
