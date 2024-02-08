from bank_acounts import *
dave = BankAccount(1000,"dave")
sara = BankAccount(2000,"sara")
dave.getBalance()
sara.getBalance()

sara.deposit(1000)
sara.getBalance()
print("before  money transfer ")
dave.getBalance()
sara.transfer(1500,dave)
