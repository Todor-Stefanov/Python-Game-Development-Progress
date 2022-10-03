from Bank import *

obj_bank = Bank()

peter_account = obj_bank.create_account("Peter", "123", 0)
print("Peter's Account number is: ", peter_account)

john_account = obj_bank.create_account("John", "John123", 200)
print("John's Account number is: ", john_account)

while True:
    print()
    print("Press 'o' to open a new account")
    print("Press 'c' to close an account")
    print("Press 'b' to get your balance")
    print("Press 'd' to make a deposit")
    print("Press 'w' to make a withdrawal")
    print("Press 's' to show all accounts")
    print("Press 'q' to quit")
    print()

    choice = input("What action do you want to perform? ")

    if choice == "b":
        obj_bank.balance()
    elif choice == "d":
        obj_bank.deposit()
    elif choice == "w":
        obj_bank.withdraw()
    elif choice == "s":
        obj_bank.show()
    elif choice == "o":
        obj_bank.open_account()
    elif choice == "c":
        obj_bank.close_account()
    else:
        break
