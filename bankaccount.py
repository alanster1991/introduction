class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()
#            print(account)

savings = BankAccount( 0.05, 1000)
checking = BankAccount( 0.02 , 5000)

savings.deposit(100).deposit(200).deposit(500).withdraw(600).yield_interest().display_account_info()
checking.deposit(1000).deposit(2000).deposit(4000).withdraw(4500).yield_interest().display_account_info()

BankAccount.print_all_accounts()