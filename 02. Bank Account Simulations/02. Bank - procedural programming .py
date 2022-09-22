# Any number of accounts - using dictionaries Version
# With functions
accounts = []


def create_an_account(username, password, balance):
    global accounts
    new_acc = {'username': username, 'password': password, 'balance': balance}
    accounts.append(new_acc)


def actions_info():
    print()
    print("Press 'b' to get your balance")
    print("Press 'd' to make a deposit")
    print("Press 'w' to make a withdrawal")
    print("Press 's' to show the account")
    print("Press 'q' to quit")
    print()


def get_balance(account_number, password):
    global accounts
    current_account = accounts[account_number]
    if password == current_account['password']:
        return f"{current_account['username']}'s balance is {current_account['balance']}$"
    else:
        return "Incorrect password!"


def deposit(account_number, amount, password):
    global accounts
    current_account = accounts[account_number]

    if password == current_account['password']:
        if amount < 0:
            print("You cannot deposit a negative amount")
        else:
            current_account['balance'] += amount
            print(f"{current_account['username']}, your new balance is: {current_account['balance']}$")
    else:
        print("Incorrect password!")


def withdraw(account_number, amount, password):
    global accounts
    current_account = accounts[account_number]

    if password == current_account['password']:
        if current_account['balance'] < amount:
            print("You can not withdraw more than you have in your account")
        elif amount < 0:
            print("You cannot withdraw a negative amount")
        else:
            current_account['balance'] -= amount
            print(f"{current_account['username']}, you successfully withdrew {amount} dollars from your account.")
            print(f"Your current balance is {current_account['balance']}$")
    else:
        print("Incorrect password!")


def show(account_number):
    global accounts
    current_account = accounts[account_number]
    print("Account information:")
    print(f"         Username: {current_account['username']}")
    print(f"         Password: {current_account['password']}")
    print(f"         Balance: {current_account['balance']}")
    print()


# Two sample accounts
create_an_account("Peter", "P123!", 500)

create_an_account("Mark", "M123", 300)

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
