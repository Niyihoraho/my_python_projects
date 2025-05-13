class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def get_balance(self):
        return self.balance

account=BankAccount("Heroic",20000)
account.deposit(10000)
print(account.get_balance())