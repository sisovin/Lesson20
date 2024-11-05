# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:58:04 2024

@author: chien 
"""

from bank_accounts import *
from turtle import tilt


tilt = " Chapter 20 - OOP Project in oop_project.py "
print(f"{tilt}".upper().center(80, "="))
print("")
tilt = " # Import * from bank_account # "
print(f"{tilt}".center(80, "#"))

Sisovin = BankAccount(1000, "Sisovin")
Sovanny = BankAccount(2000, "Sovanny")

Sisovin.get_balance()
Sovanny.get_balance()

Sovanny.deposit(500)

Sisovin.withdraw(1000)
Sisovin.withdraw(10)

Sisovin.transfer(1000, Sovanny)
Sisovin.transfer(100, Sovanny)

Viphop = InterestRewardsAcct(1000, "Viphop")

Viphop.get_balance()

Viphop.deposit(100)

Viphop.transfer(400, Sisovin)

Viphea = SavingsAcct(1000, "Viphea")

Viphea.get_balance()

Viphea.deposit(100)

Viphea.transfer(10000, Sovanny)
Viphea.transfer(1000, Sovanny)




