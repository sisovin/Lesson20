# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:51:46 2024

@author: chien
"""

from turtle import title


print("")
title = " Chapter 20 - OOP Project in bank_accounts.py "
print(f"{title}".upper().center(80, "="))
print("")

title = " # 1. Classes and Objects: # "
print(f"{title}".center(80, "#"))

class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_account, acct_name):
        self.balance = initial_account
        self.name = acct_name
        print(
              f"Account '{self.name}' created.\nBalance = ${self.balance:.2f}"
        )
    
    def get_balance(self):
        print(
              f"Account '{self.name}' balance = ${self.balance:.2f}"
        )
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.get_balance()
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
          raise BalanceException(
            f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
          )
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdrawal complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
    
    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer.. 🚀')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f'\nTransfer complete! ✅\n\n**********')
        except BalanceException as error:
            print(f"\nTransfer interrupted: ❌ {error}")
            
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_account, acct_name):
        super().__init__(initial_account, acct_name)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdrawal complete.")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
        
