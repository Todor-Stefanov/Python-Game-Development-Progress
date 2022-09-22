# Single Account Version
# Without functions

account_username = 'Peter'
account_password = 'peTer123@'
account_balance = float(500)


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
        pass_check = input("Please enter your password: ")
        if pass_check == account_password:
            print(account_balance, "$")
        else:
            print("Incorrect password!")
    elif choice == "d":
        print("Make a deposit:")
        deposit_amount = float(input("Please enter the amount you want to deposit: "))
        pass_check = input("Please enter your password: ")
        if pass_check == account_password:
            if deposit_amount < 0:
                print("You cannot deposit a negative amount")
            else:
                account_balance += deposit_amount
                print(f"Your new balance is: {account_balance}$")
        else:
            print("Incorrect password!")

    elif choice == "w":
        print("Make a withdrawal: ")
        withdrawal_amount = float(input("Please enter the amount to withdraw: "))
        pass_check = input("Please enter your password:")
        if pass_check == account_password:
            if account_balance < withdrawal_amount:
                print("You can not withdraw more than you have in your account")
            elif withdrawal_amount < 0:
                print("you cannot withdraw a negative amount")
            else:
                account_balance -= withdrawal_amount
                print(f"You successfully withdrew {withdrawal_amount} dollars from your account.")
                print(f"Your current balance is {account_balance}$")
        else:
            print("Incorrect password!")

    elif choice == "s":
        print("Account information:")
        print(f"         Username: {account_username}")
        print(f"         Password: {account_password}")
        print(f"         Balance: {account_balance}")
        print()

    elif choice == "q":
        break
