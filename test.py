from main import ATM


def test_balance():
    started_balance = 100
    atm = ATM(started_balance)
    assert atm.check_balance() == "Your account balance: 100"


def test_deposit():
    started_balance = 100
    atm = ATM(started_balance)
    assert atm.deposit_funds(-100) == "Wrong value. The value must be a positive."
    assert atm.deposit_funds(50) == "Deposit made successfully"
    assert atm.check_balance() == "Your account balance: 150"


def test_withdraw():
    started_balance = 100
    atm = ATM(started_balance)
    assert atm.withdraw_funds(50) == "Withdraw made successfully."
    assert atm.check_balance() == "Your account balance: 50"
    assert atm.withdraw_funds(-100) == "Wrong value. The value must be a positive."
    assert atm.withdraw_funds(
        100) == "The account balance is too low, you cannot make a withdrawal."
