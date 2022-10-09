class User:
    
    def __init__(self, name, int_rate):
        self.name = name
        self.int_rate = int_rate
        self.account = BankAccount(balance = 0, int_rate = 0)

    def make_deposit(self, amount):
        print("Depositing: $" + str(amount))
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(self.name)
        self.account.display_account()
        return self
    
    def yield_interest(self):
        self.account.yield_interest()
        return self



class BankAccount:
    def __init__(self, balance, int_rate):
        
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a 5 fee")
            self.balance -= 5
        return self
    
    def display_account(self):  
        print(f'Balance {self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

alan = User("Alan Chin", 0.4)
alan.display_user_balance().make_deposit(1000).display_user_balance()
alan.make_withdrawal(555).display_user_balance()
alan.yield_interest().display_user_balance()

myo = User("Myo TUN", 0.5)
myo.display_user_balance().make_deposit(500)
myo.make_withdrawal(350).display_user_balance()
myo.yield_interest().display_user_balance()
