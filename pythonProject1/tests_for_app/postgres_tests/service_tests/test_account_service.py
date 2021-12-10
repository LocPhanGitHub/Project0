from custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException, \
    NegativeDepositMoneyException, NegativeWithdrawalMoneyException, NegativeBalanceFromWithdrawingMoneyException, \
    NegativeBalanceFromTransferringMoneyException, NegativeMoneyTransferringMoneyException
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from entities.account import Account
from service_layer.implementation_services.account_postgres_service import AccountPostgresService

account_dao = AccountPostgresDAO()
account_service = AccountPostgresService(account_dao)

account = Account(2, 100, 8, 1)
another_account = Account(3, 300, 9, 1)


def test_validate_create_account_method():
    try:
        account_service.service_create_account(account)
    except DuplicateAccountNumberException as e:
        assert str(e) == "This account number is not available!"


def test_validate_deposit_negative_money_method():
    try:
        account_service.service_deposit_into_account_by_id(account_balance=50, account_id=8)
    except NegativeDepositMoneyException as e:
        assert str(e) == "You cannot deposit negative money into your account"


def test_validate_withdraw_negative_money_method():
    try:
        account_service.service_withdrawal_from_account_by_id(account_balance=150, account_id=8)
    except NegativeWithdrawalMoneyException as e:
        assert str(e) == "You cannot withdraw negative money!"


def test_validate_withdraw_that_result_negative_balance():
    try:
        account_service.service_withdrawal_from_account_by_id(account_balance=-1, account_id=8)
    except NegativeBalanceFromWithdrawingMoneyException as e:
        assert str(e) == "You cannot withdraw more than your current balance!"


def test_validate_transfer_negative_money_between_account():
    try:
        account_service.service_transfer_money_between_account_by_ids(transfer_account_id=9, receiving_account_id=8, transfer_value=-100)
    except NegativeMoneyTransferringMoneyException as e:
        assert str(e) == "You cannot transfer negative money into another account"


def test_validate_transfer_more_money_than_balance_between_account():
    try:
        account_service.service_transfer_money_between_account_by_ids(transfer_account_id=9, receiving_account_id=8, transfer_value=301)
    except NegativeBalanceFromTransferringMoneyException as e:
        assert str(e) == "You cannot transfer more money than your current account balance"
