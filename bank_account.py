from helpers import *

name = input("What is your name? ")
initial_deposit = int(input("Initial deposit: $"))

bank_account = BankAccount(name)
bank_account.make_deposit(initial_deposit)

shopping_status = ''

while shopping_status.lower() != 'q':
    print("""
    Please choose an option: 
    1.) Wine ($40)
    2.) Xbox ($500)
    3.) Cheap Wine ($10)
    4.) Make a deposit
    """)

    choice = int(input())

    if choice == 1:
        grocery_store(bank_account, products["Wine"])

    if choice == 2:
        grocery_store(bank_account, products["Xbox"])

    if choice == 3:
        grocery_store(bank_account, products["Cheap Wine"])

    if choice == 4:
        deposit = input("How much would you like to deposit?: $")
        bank_account.make_deposit(int(deposit))
        print(
            f"Thank you for your deposit. Your balance is ${bank_account.balance} ")

    shopping_status = input(
        "Hit enter to continue shopping. Enter Q to quit shopping ")
