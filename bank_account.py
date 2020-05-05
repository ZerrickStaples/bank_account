class BankAccount(object):
    def __init__(self, object):
        self.name = object
        self.balance = 0

bank_account = BankAccount("Zerrick")
print(bank_account.__dict__)
