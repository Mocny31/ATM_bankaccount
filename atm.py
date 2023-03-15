"""
ATM system for the STRONG bank.

This script implements a simple ATM system for the STRONG bank
using the BankAccount class from the bankaccount module.

Usage:
    - Enter your starting bank account balance when prompted.
    - Choose an action from the menu by entering the corresponding number.
    - Follow the prompts to complete the selected action.

Actions:
    1. Deposit: Add funds to the account.
    2. Withdraw: Remove funds from the account.
    3. Check balance: Display the current balance of the account.
    4. Close: Exit the ATM system.

This script requires the following modules to be imported:
    - enum
    - bankaccount

Author: Michal Mocny
Date: 05.03.2023
"""

from enum import IntEnum
from bankaccount import BankAccount


def main():
    while True:
        try:
            started_balance = float(
                input("Enter your starting bank account balance: "))
            my_account = BankAccount(started_balance)
        except ValueError:
            print("Wrong value. Enter a number value.")
        else:
            if started_balance >= 0:
                break

            print("The value must be a positive value or 0.")

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
                if value <= 0:
                    print("Wrong value.")
                else:
                    result = my_account.deposit(value)
                    print(result.message)
            elif disposition == menu_atm.Withdraw:
                value = int(input("Enter the amount to be withdrawn: "))
                if value <= 0:
                    print("Wrong value.")
                else:
                    result = my_account.withdraw(value)
                    print(result.message)
            elif disposition == menu_atm.Check_balance:
                print(my_account.check_balance_account())
            elif disposition == menu_atm.Close:
                break
            else:
                print("Wrong value.")
        except ValueError:
            print("Wrong value.")
