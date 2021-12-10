from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from entities.account import Account

account_dao = AccountPostgresDAO()

account: Account = Account(10, 100, 3, 1)
new_account: Account = Account(11, 100, 10, 1)
another_account: Account = Account(12, 100, 15, 1)

to_transfer_account: Account = Account(13, 100, 16, 1)
to_receive_account: Account = Account(14, 100, 17, 1)

account_to_delete = Account(3, 300, 3, 1)


def test_create_account_success():
    created_account = account_dao.create_account(account)
    assert created_account.account_id != 3


def test_get_account_info_success():
    get_account = account_dao.get_account_by_id(1)
    assert get_account.account_number == 1


def test_get_all_account_info_success():
    accounts = account_dao.get_all_account_by_id()
    assert len(accounts) >= 2


def test_deposit_account_success():
    deposit_account = account_dao.create_account(new_account)
    deposit_result = account_dao.deposit_into_account_by_id(50, deposit_account.account_id)
    assert deposit_result == 150


def test_withdrawal_account_success():
    withdraw_account = account_dao.create_account(another_account)
    withdraw_result = account_dao.withdrawal_from_account_by_id(50, withdraw_account.account_id)
    assert withdraw_result == 50


# gotta check back
def test_transfer_account_success():
    account_to_transfer = account_dao.create_account(to_transfer_account)
    account_to_receive = account_dao.create_account(to_receive_account)
    result = account_dao.transfer_money_between_account_by_ids(account_to_transfer.account_id,
                                                               account_to_receive.account_id, 50)
    print(account_to_transfer.account_balance)
    print(account_to_receive.account_balance)
    assert result


def test_delete_account_success():
    account_to_be_deleted = account_dao.create_account(account_to_delete)
    result = account_dao.delete_account_by_id(account_to_be_deleted.account_id)
    assert result
