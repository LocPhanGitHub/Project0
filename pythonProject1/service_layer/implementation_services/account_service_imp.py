from typing import Type

from custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException, \
    NegativeDepositMoneyException, NegativeWithdrawalMoneyException, NegativeBalanceFromWithdrawingMoneyException
from data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
from entities.account import Account
from service_layer.abstract_services.account_service import AccountService


class AccountServiceImp(AccountService):
    def __init__(self, account_dao):
        self.account_dao: AccountDAOImp = account_dao

    def service_create_account(self, account: Account):
        for current_account in self.account_dao.account_list:
            if current_account.customer_id == account.customer_id and current_account.account_number == account.account_number:
                raise DuplicateAccountNumberException("This account number is not available")
            else:
                return self.account_dao.create_account(account)

    def service_get_account_by_id(self, account_id: int):
        return self.account_dao.get_account_by_id(account_id)

    def service_get_all_account_by_id(self):
        return self.account_dao.get_all_account_by_id()

    def service_deposit_into_account_by_id(self, account_balance: float, account_id: int):
        for current_account in self.account_dao.account_list:
            if current_account.account_id == account_id:
                if current_account.account_balance < account_balance:
                    raise NegativeDepositMoneyException("You cannot deposit negative money into your account")
            else:
                return current_account.account_balance

    def service_withdrawal_from_account_by_id(self, account_balance: float, account_id: int):
        for current_account in self.account_dao.account_list:
            if current_account.account_id == account_id and current_account.account_balance > account_balance:
                raise NegativeWithdrawalMoneyException("You cannot withdraw negative money into your account")
            elif current_account.account_id == account_id and current_account.account_balance < 0:
                raise NegativeBalanceFromWithdrawingMoneyException("You cannot withdraw more money than your current account balance")
            else:
                return current_account.account_balance

    def service_transfer_money_between_account_by_ids(self, account: Account):
        pass

    def service_delete_account_by_id(self, account_id: int) -> Type[bool]:
        return self.account_dao.delete_account_by_id(account_id)
