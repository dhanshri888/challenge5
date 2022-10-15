# challenge 5 


class Account:

    def __init__(self, title, balance):
        self.title = title
        self.balance = balance 

    def withdrawal(self, amount):
        self.balance -= amount
        
    def deposit(self, amount):
        self.balance += amount
    
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):

    def __init__(self, title, balance, interestRate):
            super().__init__(title, balance)
            self.interestRate = interestRate

    def interestAmount(self):
        interestAmount = (self.interestRate * self.balance ) / 100
        return interestAmount

title = input("Enter a title ")
balance = int(input("Enter a balance :"))
interestRate = int(input("Enter an interest rate :"))

SavingsAccount_obj = SavingsAccount(title,balance,interestRate)

SavingsAccount_obj.withdrawal(int(input("Enter a withdrawal amount :")))
SavingsAccount_obj.deposite(int(input("Enter a deposite amount :")))


print(SavingsAccount_obj.getBalance())
print(SavingsAccount_obj.interestAmount())
