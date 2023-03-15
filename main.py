from enum import IntEnum
from atm import ATM


def get_starting_account_balance():
    """
    A method for determining the starting balance of the bank account,
    created for testing the application.
    """
    while True:
        try:
            started_account_balance = float(
                input("Enter your starting bank account balance: "))
            if started_account_balance >= 0:
                return started_account_balance
            print("The value must be a positive value or 0.")
        except ValueError:
            print("Wrong value. Enter a float value.")


def main():
    started_account_balance = get_starting_account_balance()
    session = ATM(started_account_balance)

    menu_atm = IntEnum(
        "menu_atm", ["Deposit", "Withdraw", "Check_balance", "Close"])

    while True:
        try:
            disposition = int(input("""
            Welcome to STRONG's ATM. Choose what you want to do.
            1. Deposit
            2. Withdraw
            3. Check_balance
            4. Close
            Your choose: """))
            if disposition == menu_atm.Deposit:
                value = int(input("Enter the amount to be deposited: "))
                result = session.deposit_funds(value)
                print(result)
            elif disposition == menu_atm.Withdraw:
                value = int(input("Enter the amount to be withdrawn: "))
                result = session.withdraw_funds(value)
                print(result)
            elif disposition == menu_atm.Check_balance:
                result = session.check_balance()
                print(result)
            elif disposition == menu_atm.Close:
                print("Bye bye.")
                break
            else:
                print("Wrong value.")
        except ValueError:
            print("Wrong value.")


if __name__ == '__main__':
    main()
