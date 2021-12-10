from custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException, \
    NegativeDepositMoneyException, NegativeWithdrawalMoneyException, NegativeBalanceFromWithdrawingMoneyException, \
    NegativeBalanceFromTransferringMoneyException, NegativeMoneyTransferringMoneyException
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from entities.account import Account
from service_layer.abstract_services.account_service import AccountService


class AccountPostgresService(AccountService):
    def __init__(self, account_dao: AccountPostgresDAO):
        self.account_dao = account_dao

    def service_create_account(self, account: Account):
        accounts = self.account_dao.get_all_account_by_id()
        for existing_account in accounts:
            if existing_account.account_id == account.account_id:
                if existing_account.account_number == account.account_number:
                    raise DuplicateAccountNumberException("This account number is not available!")
        created_account = self.account_dao.create_account(account)
        return created_account

    def service_get_account_by_id(self, account_id: int):
        return self.account_dao.get_account_by_id(account_id)

    def service_get_all_account_by_id(self) -> list[Account]:
        return self.account_dao.get_all_account_by_id()

    def service_deposit_into_account_by_id(self, account_balance: float, account_id: int):
        accounts = self.account_dao.get_all_account_by_id()
        for current_account in accounts:
            if current_account.account_id == account_id:
                if current_account.account_balance < account_balance:
                    raise NegativeDepositMoneyException("You cannot deposit negative money into your account")
        return self.account_dao.deposit_into_account_by_id(float(account_balance), account_id)

    def service_withdrawal_from_account_by_id(self, account_balance: float, account_id: int):
        if account_balance < 0:
            raise NegativeBalanceFromWithdrawingMoneyException("You cannot withdraw more than your current balance!")
        accounts = self.account_dao.get_all_account_by_id()
        for current_account in accounts:
            if current_account.account_id == account_id:
                if current_account.account_balance >= account_balance:
                    return self.account_dao.withdrawal_from_account_by_id(float(account_balance), account_id)
                else:
                    raise NegativeWithdrawalMoneyException("You cannot withdraw negative money!")

    def service_transfer_money_between_account_by_ids(self, transfer_account_id: int, receiving_account_id: int, transfer_value: float):
        transfer_account = self.service_get_account_by_id(transfer_account_id)
        transfer_account.account_balance -= transfer_value
        receiving_account = self.service_get_account_by_id(receiving_account_id)
        receiving_account.account_balance += transfer_value
        if transfer_account.account_balance < transfer_value:
            raise NegativeBalanceFromTransferringMoneyException("You cannot transfer more money than your current account balance")
        if receiving_account.account_balance + transfer_value < receiving_account.account_balance:
            raise NegativeMoneyTransferringMoneyException("You cannot transfer negative money into another account")
        return self.account_dao.transfer_money_between_account_by_ids(transfer_account_id, receiving_account_id, transfer_value)

    def service_delete_account_by_id(self, account_id: int):
        return self.account_dao.delete_account_by_id(account_id)
