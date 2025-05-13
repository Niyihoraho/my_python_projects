class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
    def get_balance(self):
        return self.balance
    def __str__(self):
        return (f"Account Ower: {self.owner}\nBalance: {self.balance}")

account=BankAccount("Niyihoraho Heroic",300000)
account.deposit(700000)
print(account)
        