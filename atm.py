from bankaccount import BankAccount


class ATM:
    """
    A class that represents an ATM machine.

    Attributes:
    account: BankAccount
        An object representing the bank account that will be used for transactions.



    check_balance() -> str:
        Returns a string message representing the current balance of the bank account.
    """

    def __init__(self, started_balance: float = 0):
        self.account = BankAccount(started_balance)

    def deposit_funds(self, value: int) -> str:
        """
        Deposits the specified amount to the bank account.
        Returns a string message representing the success or failure of the transaction.
        """
        if value <= 0:
            result = "Wrong value. The value must be a positive."
            return result
        else:
            result = self.account.deposit(value)
            return result.message

    def withdraw_funds(self, value: int) -> str:
        """
        Withdraws the specified amount from the bank account.
        Returns a string message representing the success or failure of the transaction.
        """
        if value <= 0:
            result = "Wrong value. The value must be a positive."
            return result
        else:
            result = self.account.withdraw(value)
            return result.message

    def check_balance(self) -> str:
        """
        Returns a string message representing the current balance of the bank account.
        """
        return self.account.check_balance_account()
