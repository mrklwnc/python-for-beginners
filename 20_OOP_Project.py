# Lesson 20: OOP Project

from modules.bank.bank_accounts import *

mark = BankAccount(1000, "Mark")
john = BankAccount(2000, "John")

mark.getBalance()
john.getBalance()

mark.deposit(2500)
john.deposit(2000)

mark.withdraw(1000)

john.transfer(2000, mark)

jane = InterestRewardsAcct(1000, "Jane")

jane.getBalance()
jane.deposit(100)

jane.transfer(100, john)

cooper = SavingsAcct(1000, "Cooper")

cooper.getBalance()
cooper.deposit(100)
cooper.transfer(1000, mark)
