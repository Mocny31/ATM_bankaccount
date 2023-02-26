from bankaccount import BankAccount
from enum import IntEnum

startedBalance = float(input("Enter your starting bank account balance: "))
myAccount = BankAccount(startedBalance)

Menu_ATM = IntEnum(
    "Menu_ATM", ["Deposit", "Withdraw", "Check_balance", "Close"])

while (True):
    try:
        disposition = int(input("""
        Welcome to STRONG's ATM. Choose what you want to do.
        1. Deposit
        2. Withdraw
        3. Check_balance
        4. Close
        Your choose: """))
        if disposition == Menu_ATM.Deposit:
            value = int(input("Enter the amount to be deposited: "))
            if value <= 0:
                print("Wrong value.")
            else:
                result = myAccount.deposit(value)
                print(result.message)
        elif disposition == Menu_ATM.Withdraw:
            value = int(input("Enter the amount to be withdrawn: "))
            if value <= 0:
                print("Wrong value.")
            else:
                result = myAccount.withdraw(value)
                print(result.message)
        elif disposition == Menu_ATM.Check_balance:
            print(myAccount.check_balance_account())
        elif disposition == Menu_ATM.Close:
            break
        else:
            print("Wrong value.")
    except ValueError:
        print("Wrong value.")
