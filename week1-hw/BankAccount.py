# Account class
#   This is not an account.
#   Instead, this is a blueprint (for a bank account)
#   The thing that shows what an account would look like.
#   What data does it have (instance variables) and what functions does it have (called methods)

class Account:
    
    def __init__(self, name, balance, password):
        # This is called when you create a new account
        self.name = name
        self.balance = float(balance)
        self.password = password
   
    def show(self):
        # Call this to write out details of account
        print('Account')
        print('       Name', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)
        print()

    def getBalance(self, password):
        # Call this to get the balance of the account
        if password != self.password:
            print('Sorry, incorrect password')
            return -1
        return self.balance


    def deposit(self, amountToDeposit, password):
        # Call this to make a deposit
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount!')
            return -1

        if password != self.password:
            print('Sorry, incorrect password')
            return -1
            
        self.balance = self.balance + amountToDeposit
        return self.balance
        
    def withdraw(self, amountToWithdraw, password):
        # Call this to make a withdrawl
        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return -1

        if amountToWithdraw > self.balance:
            print('You cannot withdraw more than you have in your account')
            return -1

        if password != self.password:
            print('Incorrect password for this account')
            return -1
        
        self.balance = self.balance - amountToWithdraw
        return self.balance

    # Add "addInterest" method here


# Test code
# First, create an account
oAccount = Account('Joe Schmoe', 1200.00, 'myPassword')
print(oAccount.getBalance('myPassword')) # should show starting balance
oAccount.addInterest()
print(oAccount.getBalance('myPassword')) # should show balance with interest
oAccount.addInterest()
print(oAccount.getBalance('myPassword'))    # output should *not* change
oAccount.addInterest()
print(oAccount.getBalance('myPassword'))    # output should *not* change
