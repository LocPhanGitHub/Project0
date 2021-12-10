from data_access_layer.abstract_classes.account_dao import AccountDAO
from entities.account import Account
from util.database_connection import connection


class AccountPostgresDAO(AccountDAO):
    def create_account(self, account: Account) -> Account:
        sql = "insert into account values (%s, %s, default, %s) returning account_id"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_number, account.account_balance, account.customer_id))
        connection.commit()
        account_id = cursor.fetchone()[0]
        account.account_id = account_id
        return account

    def get_account_by_id(self, account_id: int) -> Account:
        sql = "select * from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        account_record = cursor.fetchone()
        account = Account(*account_record)
        return account

    def get_all_account_by_id(self) -> list[Account]:
        sql = "select * from account"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_records = cursor.fetchall()
        account_list = []
        for account in account_records:
            account_list.append(Account(*account))
        return account_list

    def deposit_into_account_by_id(self, deposit_value: float, account_id: int):
        sql = "update account set account_balance = account_balance + %s where account_id = %s returning account_balance"
        cursor = connection.cursor()
        cursor.execute(sql, (deposit_value, account_id))
        connection.commit()
        account_balance = cursor.fetchone()[0]
        return account_balance

    def withdrawal_from_account_by_id(self, withdraw_value: float, account_id: int):
        sql = "update account set account_balance = account_balance - %s where account_id = %s returning account_balance"
        cursor = connection.cursor()
        cursor.execute(sql, (withdraw_value, account_id))
        connection.commit()
        account_balance = cursor.fetchone()[0]
        return account_balance

    def transfer_money_between_account_by_ids(self, transfer_account_id: int, receiving_account_id: int, transfer_value: float):
        sql = "update account set account_balance = account_balance + %s where account_id = %s returning account_balance"
        cursor = connection.cursor()
        cursor.execute(sql, (transfer_value, receiving_account_id))
        connection.commit()
        received_account_balance = cursor.fetchone()[0]

        sql = "update account set account_balance = account_balance - %s where account_id = %s returning account_balance"
        cursor = connection.cursor()
        cursor.execute(sql, (transfer_value, transfer_account_id))
        connection.commit()
        transferred_account_balance = cursor.fetchone()[0]
        return [received_account_balance, transferred_account_balance]

    def delete_account_by_id(self, account_id: int) -> bool:
        sql = "delete from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True
