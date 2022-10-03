class AbortTransaction(Exception):
    ''' raise this exception to abort a bank transaction '''
    pass

class Account():
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = self.validate_amount(balance)

    def validate_amount(self, balance):
        try:
            balance = int(balance)
        except ValueError:
            raise AbortTransaction("Balance must be an integer")
        if balance < 0:
            raise AbortTransaction("Balance must be positive")
        return balance

    def check_pass(self, password):
        if password != self.password:
            raise AbortTransaction("Incorrect password for this account")

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        amount_to_deposit = self.validate_amount(amount)
        self.balance += amount_to_deposit
        return self.balance

    def withdraw(self, amount):
        amount_to_withdraw = self.validate_amount(amount)
        if amount_to_withdraw > self.balance:
            raise AbortTransaction("You cannot withdraw more than you have in your account")
        self.balance -= amount_to_withdraw
        return self.balance

    def show(self):
        print("Account information:")
        print(f"         Username: {self.username}")
        print(f"         Password: {self.password}")
        print(f"         Balance: {self.balance}")
        print()
