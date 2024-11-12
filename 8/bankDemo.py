class Bank:
    def __init__(self,bname):
        self.bname = bname
    
    def Display1(self):
        print("\nBank name:",self.bname)
        
class AccHolder(Bank):
    def __init__(self,bname,accholdername,balance):
        super().__init__(bname)
        self.accholdername = accholdername
        self.balance = balance
        
    def Display2(self):
        print("Account holder name:",self.accholdername)
        print("Balance:",self.balance)

'''class SavingAcc(AccHolder):
    def __init__(self,bname,accholdername,balance,minBal):
        super().__init__(bname,accholdername,balance)
        self.minBal = minBal
        
    def Display3(self):
        print("Min Balance limit:",self.minBal)'''

class operations(AccHolder):
    def __init__(self,bname,accholdername,balance,bal1,bal2):
        super().__init__(bname,accholdername,balance)
        self.bal1 = bal1
    
    def depo(self,bal1):
        self.bal1 = bal1
        self.balance += self.bal1
        print("Deposit amount:", self.bal1)
        print("Current balance:",self.balance)
    
    def withd(self,bal2):
        self.bal2 = bal2
        if self.bal2 > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= self.bal2
            print("Withdraw amount:",self.bal2)
            print("Current balance:",self.balance)
       
'''class withdraw(AccHolder):
    def __init__(self,bname,accholdername,balance,bal2):
        super().__init__(bname,accholdername,balance)
        self.bal2 = bal2
    
    def withd(self,bal2):
        self.bal2 = bal2
        if self.bal2 > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= self.bal2
            print("Withdraw amount:",self.bal2)
            print("Current balance:",self.balance)
    def __del__(self):
        print("Destructor called")'''
        
bname = input("Enter bank name: ") 
name = input("Enter name:")
totalBal = int(input("Enter Balance:"))

obj = operations(bname, name ,totalBal,0,0)
#obj = deposite(bname,name ,totalBal,0)
obj.Display1()
obj.Display2()

depoamt = int(input("Enter amount to deposite:"))
obj.depo(depoamt)

#obj.Display3()


withdrawamt = int(input("Enter amount to withdraw:"))
obj.withd(withdrawamt)
del obj

