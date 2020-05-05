class BankAccount(object):
    def __init__(self, object):
        self.name = object
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawl(self, amount):
        self.balance -= amount


bank_account = BankAccount("Zerrick")
bank_account.make_deposit(1200)
bank_account.make_withdrawl(40)
print(bank_account.__dict__)
