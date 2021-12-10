class DuplicateAccountNumberException(Exception):
    def __init__(self, message):
        self.message = message


class NegativeDepositMoneyException(Exception):
    def __init__(self, message):
        self.message = message


class NegativeWithdrawalMoneyException(Exception):
    def __init__(self, message):
        self.message = message


class NegativeBalanceFromWithdrawingMoneyException(Exception):
    def __init__(self, message):
        self.message = message


class NegativeBalanceFromTransferringMoneyException(Exception):
    def __init__(self, message):
        self.message = message


class NegativeMoneyTransferringMoneyException(Exception):
    def __init__(self, message):
        self.message = message
