class BalanceException(Exception):
    pass
class BankAccount:
    
    def __init__(self,initialAccount,acctName):
        self.balance = initialAccount
        self.name = acctName
        print("\n Acount name ",self.name," created\nBalance $",self.balance)
    
    def getBalance(self):
        print("\n Account ",self.name,"\n Balance ",self.balance)
    
    def deposit(self,amount):
        self.balance = self.balance +amount
        print("\n Depost\ite complete")
        self.getBalance()
    
    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException("\nSorry ,account ",self.name,"\nonly has a balance of $",self.balance)
    
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error :
            print("\n withdraw interrupted:",error)
    
    def transfer(self,amount,account):
        try:
            print("\n *********** \nBeginning Transfer....")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!! \n")
        except BalanceException as error:
            print("\nTransfer interrupted as ",error)
class InterestRewardacct(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print(("\ndeposit complete"))
        self.getBalance()
         
class SavingAcct(InterestRewardacct):
    def __init__(self,initialAmount,acctName):
        super().__init__(initialAmount,acctName)
        self.fee = 5
    
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount +self.fee)
            self.balance = self.balance -(amount + self.fee)
            print('\nWithdraw complete.')
            self.balance()
        except BalanceException as error :
            print ('\nWithdraw interrupted : ',error)
            