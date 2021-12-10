from abc import ABC, abstractmethod

from entities.account import Account


class AccountService(ABC):
    # create account method
    @abstractmethod
    def service_create_account(self, account: Account):
        pass

    # get account information
    @abstractmethod
    def service_get_account_by_id(self, account_id: int):
        pass

    # get all account information
    @abstractmethod
    def service_get_all_account_by_id(self) -> list[Account]:
        pass

    # deposit into specific account
    @abstractmethod
    def service_deposit_into_account_by_id(self, account_balance: float, account_id: int):
        pass

    # withdrawal from a specific account
    @abstractmethod
    def service_withdrawal_from_account_by_id(self, account_balance: float, account_id: int):
        pass

    # transfer money between account
    @abstractmethod
    def service_transfer_money_between_account_by_ids(self, transfer_account_id: int, receiving_account_id: int, transfer_amount: float):
        pass

    # delete account information
    @abstractmethod
    def service_delete_account_by_id(self, account_id: int):
        pass
