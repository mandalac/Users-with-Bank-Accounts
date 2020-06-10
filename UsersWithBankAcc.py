class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        sum = 0
        if self.balance > 0:
            sum = self.balance * self.int_rate
        self.balance += sum
        return self

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.amount  = amount
    def make_withdraw(self, amount):
        self.balance = balance
    def display_account_info(self, balance):
        self.balance = balance
        
b1 = BankAccount(5, 1000)
b1.deposit(100).deposit(100).deposit(100).withdraw(30).display_account_info()

b2 = BankAccount(5, 2000)
b2.deposit(100).deposit(100).withdraw(30).withdraw(
    25).withdraw(20).withdraw(15).display_account_info()
