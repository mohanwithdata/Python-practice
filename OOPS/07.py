class bankaccount():
    def __init__(self, owner, balance=0, acct_type="savings"):
        self.owner = owner
        self.balance = balance
        self.acct_type = acct_type
    
    def acct_info(self):
        print(f"Account Holder: {self.owner}")
        print(f"Account Type: {self.acct_type}")
        print(f"Account Balance: {self.balance}")

account1 = bankaccount("Mohan", 5000)
account2 = bankaccount("Balor", 5000, "Current")

account1.acct_info()

print("-"*30)

account2.acct_info()
