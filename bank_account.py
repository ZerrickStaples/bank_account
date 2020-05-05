class BankAccount(object):
    def __init__(self, object):
        self.name = object
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawl(self, amount):
        self.balance -= amount

    def check_balance(self, amount):    
        if (self.balance - amount) < 0:
            print("Insufficient funds ")


bank_account = BankAccount("Zerrick")
bank_account.make_deposit(1200)
bank_account.check_balance(1201)
#bank_account.make_withdrawl(1201)
print(bank_account.__dict__)
