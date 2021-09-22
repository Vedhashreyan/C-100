class atm(object):
    def __init__(self,name,balance_amount,pin,accountNumber):
        self.name=name
        self.balance=balance_amount
        self.pin=pin
        self.accountNumber = accountNumber
    def playingWithCash(self):
        name = input("Enter your name: ")
        accNumber = input("Enter your Account Number: ")
        if name == self.name and accNumber==self.accountNumber:
            print("Logged in successfully")
            w = input("Do you want to with draw money or do you want to deposit money?(press w for with draw and d for deposit): ")
            if w=="w":
                money = int(input("Enter amount you want to with draw: "))
                verify = int(input("Enter your pin: "))
                if verify==self.pin:
                    if money<self.balance and money>0:
                        print("With drawed succesful","Your current balance is ",(self.balance)-money)
                    else:
                        print("You don't have that much money to draw","your current balance is: ",self.balance)
                else:
                    print("invalid pin")
            elif w=="d":
                 m = int(input("Enter amount you want to deposit: "))
                 v = int(input("Enter your pin: "))
                 if v == self.pin:
                    if m>0:
                        print("Deposited succesful","Your current balance is ",(self.balance)+m)
                    else:
                        print("You can't deposit negative amount","your current balance is: ",self.balance)
                 else:
                    print("invalid pin")

        else:
            print("User not found with name", name,"or with Account Number",accNumber)
man1 = atm("Vedh",3000,1234,"173371")
print(man1.playingWithCash())


        