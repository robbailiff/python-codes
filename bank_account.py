class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"You added {amount} to your account")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("You cannot withdraw more than your current balance")
        else:
            self.balance = self.balance - amount
            print(f"You have withdrawn {amount} from your account")
            
            
account = BankAccount('Rob',100)
print(account)
print(account.owner)
print(account.balance)
account.deposit(50)
account.withdraw(75)
account.withdraw(500)
print("You are broke!")
print("You spend your last quid on a lottery ticket")
print("You win the lottery!")
account.deposit(1000000)
print("You are a millionaire!!!")
