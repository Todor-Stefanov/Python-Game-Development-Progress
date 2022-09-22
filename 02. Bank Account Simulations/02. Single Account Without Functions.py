# Any number of accounts - using lists Version
# With functions

accounts_usernames = []
accounts_passwords = []
accounts_balances = []


def create_an_account(username, password, balance):
    global accounts_usernames, accounts_passwords, accounts_balances
    accounts_usernames.append(username)
    accounts_passwords.append(password)
    accounts_balances.append(balance)


def actions_info():
    print()
    print("Press 'b' to get your balance")
    print("Press 'd' to make a deposit")
    print("Press 'w' to make a withdrawal")
    print("Press 's' to show the account")
    print("Press 'q' to quit")
    print()


def get_balance(account_number, password):
    global accounts_usernames, accounts_passwords, accounts_balances
    if password == accounts_passwords[account_number]:
        return f"{accounts_usernames[account_number]}'s balance is {accounts_balances[account_number]}$"
    else:
        return "Incorrect password!"


def deposit(account_number, amount, password):
    global accounts_usernames, accounts_passwords, accounts_balances

    if password == accounts_passwords[account_number]:
        if amount < 0:
            print("You cannot deposit a negative amount")
        else:
            accounts_balances[account_number] += amount
            print(f"{accounts_usernames[account_number]}, your new balance is: {accounts_balances[account_number]}$")
    else:
        print("Incorrect password!")


def withdraw(account_number, amount, password):
    global accounts_usernames, accounts_passwords, accounts_balances
    if account_number == 0:
        if password == accounts_passwords[account_number]:
            if accounts_balances[account_number] < amount:
                print("You can not withdraw more than you have in your account")
            elif amount < 0:
                print("You cannot withdraw a negative amount")
            else:
                accounts_balances[account_number] -= amount
                print(f"{accounts_usernames[account_number]} successfully withdrew {amount} dollars from your account.")
                print(f"Your current balance is {accounts_balances[account_number]}$")
        else:
            print("Incorrect password!")


def show(account_number):

    print("Account information:")
    print(f"         Username: {accounts_usernames[account_number]}")
    print(f"         Password: {accounts_passwords[account_number]}")
    print(f"         Balance: {accounts_balances[account_number]}")
    print()


print(f"Peter's account number is {len(accounts_usernames)}")  # 0
create_an_account("Peter", "P123!", 500)

print(f"Peter's account number is {len(accounts_usernames)}")  # 1
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
