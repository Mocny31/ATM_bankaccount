class Result:
    def __init__(self, message, value=None):
        self.isSucces = None
        self.message = message
        self.value = value


class Ok(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSucces = True


class Error(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSucces = False


class BankAccount:
    nextId = 1

    def __init__(self, balance: float = 0):
        self.balance = balance
        self.id = BankAccount.nextId
        BankAccount.nextId += 1

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
        return "The account is assigned id nr " + str(self.id) + "and its balance " + str(self.balance)
