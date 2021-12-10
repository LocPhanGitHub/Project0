from abc import ABC, abstractmethod

from entities.account import Account


class AccountDAO(ABC):

    # create account method
    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    # get account information
    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    # get all account information
    @abstractmethod
    def get_all_account_by_id(self) -> list[Account]:
        pass

    # deposit into specific account
    @abstractmethod
    def deposit_into_account_by_id(self, deposit_value: float, account_id: int):
        pass

    # withdrawal from a specific account
    @abstractmethod
    def withdrawal_from_account_by_id(self, withdraw_value: float, account_id: int):
        pass

    # transfer money between account
    @abstractmethod
    def transfer_money_between_account_by_ids(self, transfer_account_id: int, receiving_account_id: int, transfer_value: float):
        pass

    # delete account information
    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass
