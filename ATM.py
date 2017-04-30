import random
def account():
    print ("Hello, welcome to Bank of Python!")
    print ("Please enter your account pin number")
    account = raw_input("Account pin number is: ")
    

account()

def balance():
    print ("would you like to see your account balance?")
    see = raw_input("Enter Y or N: ")
    if (see == "Y") or (see == "y"):
        balance = random.randint(1000,2000)
    print ("Current balance: $" + str(balance))

balance()

def transaction():
    print ("Would you like to make a transaction?")
    more = raw_input("Enter Y or N: ")

    if (more == "Y") or (more == "y"):
        print ("Would you like to make a deposit or withdraw? Or would you like to end this transaction?")
        answer = raw_input("Enter D for deposit; W for withdraw; E for end: ")

transaction()

def deposit():
    if (answer == "D") or (answer == "d"):
        print ("How much would you like to deposit?")
        deposit = input("Enter amount to deposit: ")
        deposit = int(deposit)

        currentbalance = deposit + balance
        print ("Deposited: $" + str(deposit))
        print ("Current Balance: $" + str(currentbalance))

deposit()

def withdraw():    
    if (answer == "W") or (answer == "w"):
        print ("How much would you like to withdrawl?")
        withdraw = input("Enter amount to withdraw: ")
        withdraw = int(withdraw)

        currentbalance = withdraw - balance
        print ("Withdrew: $" + str(withdraw))
        print ("Current Balance: $" + str(currentbalance))

withdraw()        

def end():
    if (answer == "E") or (answer == "e"):
        exit ("Thank you for Banking with Bank of Python, goodbye!")

    else:
        exit ("Thank you for Banking with Bank of Python, goodbye!")

end()
