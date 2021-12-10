from data_access_layer.implementation_classes.account_dao_imp import AccountDAOImp
from entities.account import Account

account_dao_imp = AccountDAOImp()

account = Account(1, 100, 0, 0)


def test_create_account_success():
    new_account: Account = account_dao_imp.create_account(account)
    assert new_account.account_id != 0


def test_get_account_info_success():
    returned_account: Account = account_dao_imp.get_account_by_id(1)
    assert returned_account.account_id == 1


def test_get_all_account_info_success():
    account_list = account_dao_imp.get_all_account_by_id()
    assert len(account_list) >= 2


def test_deposit_account_success():
    pass


def test_withdrawal_account_success():
    pass


def test_transfer_account_success():
    pass


def test_delete_account_success():
    confirm_account_deleted = account_dao_imp.delete_account_by_id(3)
    assert confirm_account_deleted
