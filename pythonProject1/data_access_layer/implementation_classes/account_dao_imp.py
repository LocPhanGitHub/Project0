from typing import Type

from data_access_layer.abstract_classes.account_dao import AccountDAO
from entities.account import Account


class AccountDAOImp(AccountDAO):
    # premade account to test methods

    premade_account = Account(2, 100, 1, 0)
    premade_account_two = Account(3, 200, 2, 0)
    to_delete = Account(4, 100, 3, 0)
    deposited_account = Account(5, 100, 4, 0)
    withdrawal_account = Account(6, 100, 5, 0)
    transfer_account = Account(7, 100, 6, 0)
    received_transfer_account = Account(8, 100, 7, 0)

    # "Database" list
    account_list = [premade_account, premade_account_two, to_delete, deposited_account, withdrawal_account]
    account_id_generator = 8

    def create_account(self, account: Account) -> Account:
        account.account_id = AccountDAOImp.account_id_generator
        AccountDAOImp.account_id_generator += 1
        AccountDAOImp.account_list.append(account)
        return account

    def get_account_by_id(self, account_id: int):
        for account in AccountDAOImp.account_list:
            if account.account_id == account_id:
                return account

    def get_all_account_by_id(self) -> list[Account]:
        return AccountDAOImp.account_list

    def deposit_into_account_by_id(self, account_balance: float, account_id: int):
        pass

    def withdrawal_from_account_by_id(self, account_balance: float, account_id: int):
        pass

    def transfer_money_between_account_by_ids(self, account: Account) -> Account:
        pass

    def delete_account_by_id(self, account_id: int) -> Type[bool]:
        for account_in_list in AccountDAOImp.account_list:
            if account_in_list.account_id == account_id:
                index = AccountDAOImp.account_list.index(account_in_list)
                del AccountDAOImp.account_list[index]
                return bool
