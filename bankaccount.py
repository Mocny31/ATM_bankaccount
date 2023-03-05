class Result:
    def __init__(self, message, value=None):
        self.is_success = None
        self.message = message
        self.value = value


class Ok(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.is_success = True


class Error(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.is_success = False


class BankAccount:
    next_id = 1

    def __init__(self, balance: float = 0):
        self.balance = balance
        self.user_id = BankAccount.next_id
        BankAccount.next_id += 1

    def deposit(self, amount):
        self.balance += amount
        return Ok("Deposit made successfully", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return Ok("Withdraw made successfully.", amount)
        else:
            return Error("The account balance is too low, you cannot make a withdrawal.", amount)

    def check_balance_account(self):
        return "Your account balance: " + str(self.balance)

    def __str__(self):
        return "The account is assigned id nr " + str(self.user_id) + "and its balance " + str(self.balance)
