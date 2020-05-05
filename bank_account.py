from helpers import BankAccount

name = input("What is your name? ")
initial_deposit = input("Initial deposit: $")

bank_account = BankAccount(name)
bank_account.make_deposit(initial_deposit)

print(bank_account.__dict__)