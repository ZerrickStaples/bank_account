from helpers import BankAccount

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
        if bank_account.check_balance(40) and bank_account.is_positive_balance():
            bank_account.make_withdrawl(40)
            print(f'Thank you for your puchase. Your current balance is: ${bank_account.balance}')
        else:
            print("You do not have sufficient funds to make this purchase. Please make a deposit. ")
    
    if choice == 2:
        if bank_account.check_balance(500) and bank_account.is_positive_balance():
            bank_account.make_withdrawl(500)
            print(f'Thank you for your puchase. Your current balance is: ${bank_account.balance}')
        else:
            print("You do not have sufficient funds to make this purchase. Please make a deposit. ")
    
    if choice == 3:
        if bank_account.check_balance(10) and bank_account.is_positive_balance():
            bank_account.make_withdrawl(10)
            print(f'Thank you for your puchase. Your current balance is: ${bank_account.balance}')
        else:
            print("You do not have sufficient funds to make this purchase. Please make a deposit. ")
    
    if choice == 4:
        deposit = input("How much would you like to deposit?: $")
        bank_account.make_deposit(int(deposit))
        print(f"Thank you for your deposit. Your balance is ${bank_account.balance} ")

    shopping_status = input("Hit enter to continue shopping. Enter Q to quit shopping ")