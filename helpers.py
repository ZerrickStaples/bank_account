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

    def is_positive_balance(self):
        if self.balance <= 0:
            print('You do not have a positive balance.')
