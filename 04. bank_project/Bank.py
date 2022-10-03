from Account import *

class Bank():
    def __init__(self):
        self.accounts_dict = {}
        self.next_account_number = 0
    
    def create_account(self, username, password, balance):
        account_object = Account(username, password, balance)
        new_account_number = self.next_account_number
        self.accounts_dict[new_account_number] = account_object
        self.next_account_number += 1
        return new_account_number
    
    def open_account(self):
        print("*** Open Account ***")
        username = input("What is the name of for the new user account? ")
        user_starting_balance = float(input("What is the starting balance for this account? "))
        password = input("What is the password you want to use for this account? ")
        user_account_number = self.create_account(username, password, user_starting_balance)
        print("Your new account number is: ", user_account_number)
        print()

    def close_account(self):
        print("*** Close Account ***")
        account_number = int(input("Enter your account number: "))
        password = input("Enter your password: ")
        object_account = self.accounts_dict[account_number]
        balance = object_account.get_balance(password)
        if balance is not None:
            if str(balance).isdigit():
                print("You have", balance, "in your account. "
                                           "Please withdraw everything from your account's balance before closing it.")
            else:
                print(balance)
        else:
            del self.accounts_dict[account_number]
            print("Your account has successfully been closed.")

    def balance(self):
        print("*** Get Balance ***")
        account_number = int(input("Enter your account number: "))
        password = input("Enter your password: ")
        object_account = self.accounts_dict[account_number]
        current_balance = object_account.get_balance(password)
        print(f"Your balance is: {current_balance}")

    def deposit(self):
        print("*** Deposit ***")
        account_number = int(input("Enter your account number: "))
        password = input("Enter your password: ")
        amount = float(input("Enter the amount you want to deposit: "))
        object_account = self.accounts_dict[account_number]
        object_account.deposit(password, amount)

    def withdraw(self):
        print("*** Withdraw ***")
        account_number = int(input("Enter your account number: "))
        password = input("Enter your password: ")
        amount = float(input("Enter the amount you want to withdraw: "))
        object_account = self.accounts_dict[account_number]
        object_account.withdraw(password, amount)

    def show(self):
        for acc_num in self.accounts_dict.keys():
            obj_account = self.accounts_dict[acc_num]
            print(f"Account number: {acc_num}")
            obj_account.show()






        