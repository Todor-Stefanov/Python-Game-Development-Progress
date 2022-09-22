# Two Accounts Version
# With functions


account0username = ''
account0password = ''
account0balance = 0
account1username = ''
account1password = ''
account1balance = 0

def create_an_account(account_number, username, password, balance):
    global account0username, account0password, account0balance
    global account1username, account1password, account1balance
    if account_number == 0:
        account0username = username
        account0password = password
        account0balance = balance
    else:
        account1username = username
        account1password = password
        account1balance = balance


def actions_info():
    print()
    print("Press 'b' to get your balance")
    print("Press 'd' to make a deposit")
    print("Press 'w' to make a withdrawal")
    print("Press 's' to show the account")
    print("Press 'q' to quit")
    print()


def get_balance(account_number, password):
    global account0username, account0password, account0balance
    global account1username, account1password, account1balance
    if account_number == 0:
        if password == account0password:
            return f"{account0username}'s balance is {account0balance}$"
        else:
            return "Incorrect password!"
    else:
        if password == account1password:
            return f"{account1username}'s balance is {account1balance}$"
        else:
            return "Incorrect password!"

def deposit(account_number, amount, password):
    global account0username, account0password, account0balance
    global account1username, account1password, account1balance
    if account_number == 0:
        if password == account0password:
            if amount < 0:
                print("You cannot deposit a negative amount")
            else:
                account0balance += amount
                print(f"{account0username}, your new balance is: {account0balance}$")
        else:
            print("Incorrect password!")
    else:
        if password == account1password:
            if amount < 0:
                print("You cannot deposit a negative amount")
            else:
                account1balance += amount
                print(f"{account1username}, your new balance is: {account1balance}$")
        else:
            print("Incorrect password!")


def withdraw(account_number, amount, password):
    global account0username, account0password, account0balance
    global account1username, account1password, account1balance
    if account_number == 0:
        if password == account0password:
            if account0balance < amount:
                print("You can not withdraw more than you have in your account")
            elif amount < 0:
                print("You cannot withdraw a negative amount")
            else:
                account0balance -= amount
                print(f"{account0username} successfully withdrew {amount} dollars from your account.")
                print(f"Your current balance is {account0balance}$")
        else:
            print("Incorrect password!")
    else:
        if password == account1password:
            if account1balance < amount:
                print("You can not withdraw more than you have in your account")
            elif amount < 0:
                print("You cannot withdraw a negative amount")
            else:
                account1balance -= amount
                print(f"{account1username} successfully withdrew {amount} dollars from your account.")
                print(f"Your current balance is {account1balance}$")
        else:
            print("Incorrect password!")


def show(account_number):
    if account_number == 0:
        print("Account information:")
        print(f"         Username: {account0username}")
        print(f"         Password: {account0password}")
        print(f"         Balance: {account0balance}")
        print()
    else:
        print("Account information:")
        print(f"         Username: {account1username}")
        print(f"         Password: {account1password}")
        print(f"         Balance: {account1balance}")
        print()

create_an_account(0,"Peter", "P123!", 500)
create_an_account(1, "Mark", "M123", 300)

while True:
    actions_info()

    choice = input("What action do you want to perform? ")
    print()

    if choice == "b":
        print("Get Balance: ")
        account_number = int(input("Enter the account you want to login to (0/1): "))
        pass_check = input("Please enter your password: ")
        balance = get_balance(account_number, pass_check)
        if pass_check is not None:
            print(balance)

    elif choice == "d":
        print("Make a deposit:")
        account_number = int(input("Enter the account you want to login to (0/1): "))
        deposit_amount = float(input("Please enter the amount you want to deposit: "))
        pass_check = input("Please enter your password: ")
        deposit(account_number, deposit_amount, pass_check)

    elif choice == "w":
        print("Make a withdrawal: ")
        account_number = int(input("Enter the account you want to login to (0/1): "))
        withdrawal_amount = float(input("Please enter the amount to withdraw: "))
        pass_check = input("Please enter your password: ")
        withdraw(account_number, withdrawal_amount, pass_check)

    elif choice == "s":
        account_number = int(input("Enter the account you want to login to (0/1): "))
        show(account_number)
    elif choice == "q":
        break
