class BankAccount(object):
    def __init__(self, object):
        self.name = object
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawl(self, amount):
        self.balance -= amount

    def check_balance(self, amount):
        return (self.balance - amount) >= 0

    def is_positive_balance(self):
        return self.balance > 0
            
products = {"Wine": 40, "Xbox": 500, "Cheap Wine": 10}

def grocery_store(bank_account, amount):
    if bank_account.check_balance(amount) and bank_account.is_positive_balance():
        bank_account.make_withdrawl(amount)
        print(
            f'Thank you for your puchase. Your current balance is: ${bank_account.balance}')
    else:
        print("You do not have sufficient funds to make this purchase. Please make a deposit. ")
