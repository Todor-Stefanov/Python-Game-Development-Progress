# Single Account Version
# With functions


account_username = ''
account_password = ''
account_balance = 0


def create_an_account(username, password, balance):
    global account_username, account_password, account_balance
    account_username = username
    account_password = password
    account_balance = balance


def actions_info():
    print()
    print("Press 'b' to get your balance")
    print("Press 'd' to make a deposit")
    print("Press 'w' to make a withdrawal")
    print("Press 's' to show the account")
    print("Press 'q' to quit")
    print()


def get_balance(password):
    global account_balance
    if password == account_password:
        return f"Your balance is {account_balance}$"
    else:
        return "Incorrect password!"


def deposit(amount, password):
    global account_password, account_balance
    if password == account_password:
        if amount < 0:
            print("You cannot deposit a negative amount")
        else:
            account_balance += amount
            print(f"Your new balance is: {account_balance}$")
    else:
        print("Incorrect password!")


def withdraw(amount, password):
    global account_password, account_balance
    if password == account_password:
        if account_balance < amount:
            print("You can not withdraw more than you have in your account")
        elif amount < 0:
            print("you cannot withdraw a negative amount")
        else:
            account_balance -= amount
            print(f"You successfully withdrew {amount} dollars from your account.")
            print(f"Your current balance is {account_balance}$")
    else:
        print("Incorrect password!")


def show():
    print("Account information:")
    print(f"         Username: {account_username}")
    print(f"         Password: {account_password}")
    print(f"         Balance: {account_balance}")
    print()


create_an_account("Peter", "P123!", 500)

while True:
    actions_info()

    choice = input("What action do you want to perform? ")
    print()

    if choice == "b":
        print("Get Balance: ")
        pass_check = input("Please enter your password: ")
        balance = get_balance(pass_check)
        if pass_check is not None:
            print(balance)

    elif choice == "d":
        print("Make a deposit:")
        deposit_amount = float(input("Please enter the amount you want to deposit: "))
        pass_check = input("Please enter your password: ")
        deposit(deposit_amount, pass_check)

    elif choice == "w":
        print("Make a withdrawal: ")
        withdrawal_amount = float(input("Please enter the amount to withdraw: "))
        pass_check = input("Please enter your password: ")
        withdraw(withdrawal_amount, pass_check)

    elif choice == "s":
        show()
    elif choice == "q":
        break
