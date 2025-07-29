class bankaccount():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print(f"Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining Balance: ${self.balance}")
        else:
            print("Insufficient balance!")

    def getbalance(self):
        return self.balance
    

account = bankaccount("Mohan", 1000)

account.deposit(5000)
account.withdraw(1000)
print("Final Balance", account.getbalance())