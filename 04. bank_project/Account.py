class Account():
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

    def get_balance(self, password):
        if password == self.password:
            if self.balance > 0:
                return self.balance
            else:
                return None
        else:
            return "Incorrect password!"

    def deposit(self, password, amount):
        if password == self.password:
            if amount < 0:
                print("You cannot deposit a negative amount")
            else:
                self.balance += amount
                print(f"{self.username}, your new balance is: {self.balance}$")
        else:
            print("Incorrect password!")

    def withdraw(self, password, amount):
        if password == self.password:
            if self.balance < amount:
                print("You can not withdraw more than you have in your account")
            elif amount < 0:
                print("You cannot withdraw a negative amount")
            else:
                self.balance -= amount
                print(f"{self.username}, you successfully withdrew {amount} dollars from your account.")
                print(f"Your current balance is {self.balance}$")
        else:
            print("Incorrect password!")

    def show(self):
        print("Account information:")
        print(f"         Username: {self.username}")
        print(f"         Password: {self.password}")
        print(f"         Balance: {self.balance}")
        print()
