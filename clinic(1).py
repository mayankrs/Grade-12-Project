doctor=['Dr. Suman','Dr. Sarah','Dr. Andrio','Dr. Navin ']
import random
print "Health Check Up program!"
q=raw_input("Do you want to register in this program?")
if q=='y':
    m=raw_input("Okay! Hold on a minute!...")
    print "Okay! Before everything, let's know your age and basic dimensions! :)"
    age=input("Enter your age please!")
    height=input("Tell me your height please!(cms)")
    weight=input("And tell me your weight please!(kgs)")
    print "Hmmm..that's not bad..Now let's Calculate your BMI.. ;)"
    Q=raw_input("Calculating your BMI...")
    bmi=weight/((height/100))**2
    print "And Yeah...Your BMI is",bmi
    if bmi<18.5:
        print "You are slightly underweight, why don't you try eating a little more and do a bit more of Body builing and exercise? :)"
        
    if 18.5<bmi<25:
        print "You have optimal weight. Congratulations! Keep it up!"

    if bmi>25:
        print "You are slightly overweight, You should avoid taking heavy amounts of food. Restrict your food upto 2400 calories per day. Take diets often and do a little more of exercise! :)"
    print
    print
    print
    Q=raw_input("Okay let's proceed onto your health check up!")
    c=random.randint(1000,2000)
    print "Your register number is",c
    print
    Q=raw_input("Now please proceed to the reception :)")

    print "*"*50
    print
    print "                                                 RECEPTION"
    print
    print "*"*50

    regno=input("Receptionist : Hello! Please could you let me know your registration number?")
    if regno==c:
        print "Your doctor will be",doctor[random.randint(0,3)],". Your Room no. will be R" + random.randint(1,100)
    else:
        print "Sorry that number doesnt exist....plzzz check your register number again"

    
    print "Patient:Hello,Good Morning sir"
    print "Doctor:Good Morning"
    q1=raw_input("So...how are you feeling?")
    
    
    
    print dic      
    b=raw_input("May I know what is your problem ?")
    print "Okay, I'm prescribing a medicine for this,Please visit the pharmacy for the medicine"
    print"Welcome to the pharmacy.These are your medicines"
    dic={'fever':'1','cold':'2','Itching':'3','Dandruff':'4','Diabetes':'5','Dry Eyes':'6','Ear Allergies':'7','Hair Loss ':'8','Leg Pain or Cramps':'9','Malaria':'10','Muscle Cramp,':'11','Vomiting':'12','Wrinkles':'13','Sunburn':'14','Urine Acidity':'15'}
    k=0
    l=dic.keys()
    for i in l:
        if (cmp(i,b)==0):
            b=int(dic[i])
            if b==1:
                print "Paracetamol"
            if b==2:
                print "Aspirin"
            if b==3:
                print "Pandel"
            if b==4:
                print "Coal Tar"
            if b==5:
                print "Metformin"
            if b==6:
                print "Protectant"
            if b==7:
                print "Steriodal "
            if b==8:
                print "Minoxidil"
            if b==9:
                print "Quinine"
            if b==10:
                print "Proguanil"
            if b==11:
                print "Dantrolene"    
            if b==12:
                print "Nabilone"
            if b==13:
                print "Botulinum Toxin"
            if b==14:
                print "Adrenocorticoids"
            if b==15:
                print "Citrates "
            
print"Use the medicines as prescribed on the cover."
print "We wish you to get well soon"
print"Thanks for visiting our hospital"
        
            

            
            

    
    
    
    
     
