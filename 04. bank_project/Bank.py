from Account import *

class Bank():
    def __init__(self):
        self.accounts_dict = {}
        self.next_account_number = 0
        #self.hours = hours
        #self.address = address
        #self.phone = phone

    def validate_account_number(self):
        account_number = input("What is your account number? ")
        try:
            account_number = int(account_number)
        except ValueError:
            raise AbortTransaction("The account number must be an integer")
        if account_number not in self.accounts_dict:
            raise AbortTransaction(f"Account number '{account_number}' does not exist")
        return account_number

    def ask_for_valid_pass(self, obj_account):
        password = input("Enter your password: ")
        obj_account.check_pass(password)

    def get_users_account(self):
        account_number = self.validate_account_number()
        obj_account = self.accounts_dict[account_number]
        self.ask_for_valid_pass(obj_account)
        return obj_account

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
        obj_account = self.get_users_account()
        accounts_balance = obj_account.get_balance()
        if accounts_balance > 0:
            raise AbortTransaction("Cannot delete your account while having money in it.")
        for account_num, account in self.accounts_dict.items():
            if account == obj_account:
                del self.accounts_dict[account_num]
                print(f"Account {account_num} has successfully been deleted.")
                break

    def balance(self):
        print("*** Get Balance ***")
        obj_account = self.get_users_account()
        balance = obj_account.get_balance()
        print(f"Your balance is: {balance}")

    def deposit(self):
        print("*** Deposit ***")
        obj_account = self.get_users_account()
        user_amount = input("Please enter the amount you want to deposit: ")
        balance = obj_account.deposit(user_amount)
        print("Deposited:", user_amount)
        print("Current balance:", balance )


    def withdraw(self):
        print("*** Withdraw ***")
        obj_account = self.get_users_account()
        user_amount = input("Enter the amount you want to withdraw: ")
        balance = obj_account.withdraw(user_amount)
        print("Withdrew:", user_amount)
        print("Current balance:", balance)


    def show(self):
        print("*** Show ***")
        for acc_num in self.accounts_dict.keys():
            obj_account = self.accounts_dict[acc_num]
            print(f"Account number: {acc_num}")
            obj_account.show()









        