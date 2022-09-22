# User data storage
class Account():
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

    def balance(self, password):
        if password == self.password:
            return f"{self.username}'s balance is {self.balance}$"
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


# Main body

# sample users
user0 = Account("Peter", "P123!", 500)
user1 = Account("Mark", "M123", 300)
users = [user0, user1]

while True:
    print()
    print("Press 'b' to get your balance")
    print("Press 'd' to make a deposit")
    print("Press 'w' to make a withdrawal")
    print("Press 's' to show the account")
    print("Press 'q' to quit")
    print()

    choice = input("What action do you want to perform? ")
    print()

    if choice == "b":
        print("Get Balance: ")
        account_number = int(input("Enter the account you want to login to (0/1): "))
        pass_check = input("Please enter your password: ")
        current_user = users[account_number]
        current_user.balance(pass_check)



    elif choice == "d":
        print("Make a deposit:")
        account_number = int(input("Enter the account you want to login to (0/1): "))
        deposit_amount = float(input("Please enter the amount you want to deposit: "))
        pass_check = input("Please enter your password: ")
        current_user = users[account_number]
        current_user.deposit(pass_check, deposit_amount)

    elif choice == "w":
        print("Make a withdrawal: ")
        account_number = int(input("Enter the account you want to login to (0/1): "))
        withdrawal_amount = float(input("Please enter the amount to withdraw: "))
        pass_check = input("Please enter your password: ")
        current_user = users[account_number]
        current_user.deposit(pass_check, withdrawal_amount)

    elif choice == "s":
        account_number = int(input("Enter the account you want to login to (0/1): "))
        current_user = users[account_number]
        current_user.show()

    elif choice == "q":
        break
