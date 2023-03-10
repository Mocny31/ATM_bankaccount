"""
This module provides a simple implementation of
a BankAccount class and related classes for representing
the results of account operations.

Classes:
- Result: Represents the result of an operation.
- Ok: Represents a successful result of an operation.
- Error: Represents a failed result of an operation.
- BankAccount: Represents a bank account and provides methods for making deposits and withdrawals,
checking the balance, and getting a string representation of the account.

Usage:
- Import the module.
- Create an instance of BankAccount using the default or optional arguments.
- Call the deposit or withdraw method to make a transaction.
- Call the check_balance_account method to check the account balance.
- Call the __str__ method to get a string representation of the account.

Author: Michal Mocny
Date: 05.03.2023
"""


class Result:
    """
    Class representing the result of an operation.

    Args:
    message: A message describing the result of the operation.
    value: An optional argument containing the value returned by the operation.
    """

    def __init__(self, message: str, value: float = None) -> None:
        self.is_success = None
        self.message = message
        self.value = value


class Ok(Result):
    """
    Class representing the result of a successful operation.

    Args:
    message: A message describing the result of the operation.
    value: An optional argument containing the value returned by the operation.
    """

    def __init__(self, message: str, value: float = None) -> None:
        super().__init__(message, value)
        self.is_success = True


class Error(Result):
    """
    Class representing the result of a failed operation.

    Args:
    message: A message describing the result of the operation.
    value: An optional argument containing the value returned by the operation.
    """

    def __init__(self, message: str, value: float = None) -> None:
        super().__init__(message, value)
        self.is_success = False


class BankAccount:
    """
    Class representing a bank account, has methods for depositing,
    withdrawing and checking the balance.

    Args:
    balance: An optional argument specifying the initial account balance.
    """
    next_id = 1

    def __init__(self, balance: float = 0) -> None:
        self.balance = balance
        self.user_id = BankAccount.next_id
        BankAccount.next_id += 1

    def deposit(self, amount: int) -> Ok:
        """
        Method for making a deposit into a bank account.

        Args:
        amount: The amount to be deposited into the account.

        Returns:
        Ok: An object representing a successful result of the operation.
        """
        self.balance += amount
        return Ok("Deposit made successfully", amount)

    def withdraw(self, amount: int) -> (Ok | Error):
        """
        Method for making a withdrawal from a bank account.

        Args:
        amount: The amount to be withdrawn from the account.

        Returns:
        Ok: An object representing a successful result of the operation.
        Error: An object representing a failed result of the operation
        """
        if self.balance >= amount:
            self.balance -= amount
            return Ok("Withdraw made successfully.", amount)

        return Error("The account balance is too low, you cannot make a withdrawal.", amount)

    def check_balance_account(self) -> str:
        """
        Method for checking the balance of a bank account.
        """
        return f"Your account balance: {self.balance}"

    def __str__(self) -> str:
        return f"The account is assigned id nr {self.user_id} and its balance is {self.balance}"
