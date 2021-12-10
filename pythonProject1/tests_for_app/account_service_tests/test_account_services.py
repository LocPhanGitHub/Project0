from custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException, \
    NegativeDepositMoneyException, NegativeWithdrawalMoneyException, NegativeBalanceFromWithdrawingMoneyException
from data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
from entities.account import Account
from service_layer.implementation_services.account_service_imp import AccountServiceImp

account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)

account = Account(2, 100, 8, 0)


def test_validate_create_account_method():
    try:
        account_service.service_create_account(account)
        assert False
    except DuplicateAccountNumberException as e:
        assert str(e) == "This account number is not available"


def test_validate_deposit_negative_money_method():
    # test reject deposit negative money
    try:
        account_service.service_deposit_into_account_by_id(account_balance=50, account_id=8)
    except NegativeDepositMoneyException as e:
        assert str(e) == "You cannot deposit negative money into your account"


def test_validate_withdraw_negative_money_method():
    # test reject withdrawal negative money
    try:
        account_service.service_deposit_into_account_by_id(account_balance=150, account_id=8)
    except NegativeWithdrawalMoneyException as e:
        assert str(e) == "You cannot withdraw negative money into your account"


def test_validate_withdraw_that_result_negative_balance():
    try:
        account_service.service_deposit_into_account_by_id(account_balance=-1, account_id=8)
    except NegativeBalanceFromWithdrawingMoneyException as e:
        assert str(e) == "You cannot withdraw more money than your current account balance"


def test_validate_transfer_money_between_account():
    pass
