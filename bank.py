class Account:
    def __init__(self, name, balance, min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance-=amount
        else:
            print("Sorry, not enough funds!")

            
    def statement(self):
        print("Account balance : Rs{} ".format(self.balance))

class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)

    def __str__(self):
        return "{}'s current account balance is: Rs {} ".format(self.name,self.balance)

class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)
        
    def __str__(self):
        return "{}'s current account balance is: Rs {} ".format(self.name,self.balance)        


x=Current("Kaushik",10000)
z=Savings("Raj",120000)

