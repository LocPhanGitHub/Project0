from flask import Flask, request, jsonify

from custom_exceptions.duplicate_account_number_exception import DuplicateAccountNumberException, \
    NegativeWithdrawalMoneyException, NegativeBalanceFromWithdrawingMoneyException, NegativeDepositMoneyException, \
    NegativeBalanceFromTransferringMoneyException, NegativeMoneyTransferringMoneyException
from custom_exceptions.duplicate_customer_name_exception import DuplicateUpdateCustomerEmailException, \
    DuplicateCreateCustomerEmailException
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.account import Account
from entities.customer import Customer
from service_layer.implementation_services.account_postgres_service import AccountPostgresService
from service_layer.implementation_services.customer_postgres_service import CustomerPostgresService

import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)

account_dao = AccountPostgresDAO()
account_service = AccountPostgresService(account_dao)
customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresService(customer_dao)


# create account method
@app.post("/account")
def create_account():
    try:
        account_data = request.get_json()
        new_account = Account(
            account_data["accountNumber"],
            account_data["accountBalance"],
            account_data["accountId"],
            account_data["customerId"]
        )
        account_to_return = account_service.service_create_account(new_account)
        account_as_dictionary = account_to_return.make_account_dictionary()
        account_as_json = jsonify(account_as_dictionary)
        return account_as_json
    except DuplicateAccountNumberException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


# get account information
@app.get("/account/<account_id>")
def get_account_by_id(account_id: str):
    result = account_service.service_get_account_by_id(int(account_id))
    result_as_dictionary = result.make_account_dictionary()
    account_as_json = jsonify(result_as_dictionary)
    return account_as_json


# get all account information
@app.get("/account")
def get_all_account_by_id():
    accounts_as_accounts = account_service.service_get_all_account_by_id()
    accounts_as_dictionary = []
    for accounts in accounts_as_accounts:
        dictionary_account = accounts.make_account_dictionary()
        accounts_as_dictionary.append(dictionary_account)
    return jsonify(accounts_as_dictionary)


# deposit into specific account
@app.patch("/account/deposit/<account_id>")
def deposit_into_account_by_id(account_id: str):
    try:
        body = request.get_json()
        deposit_value = body["depositValue"]
        result = account_service.service_deposit_into_account_by_id(float(deposit_value), int(account_id))
        balance = {"account_balance": result}
        return balance
    except NegativeDepositMoneyException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


# withdrawal from a specific account
@app.patch("/account/withdraw/<account_id>")
def withdrawal_from_account_by_id(account_id: str):
    try:
        body = request.get_json()
        withdraw_value = body["withdrawValue"]
        result = account_service.service_withdrawal_from_account_by_id(float(withdraw_value), int(account_id))
        balance = {"account_balance": result}
        return balance
    except NegativeWithdrawalMoneyException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400
    except NegativeBalanceFromWithdrawingMoneyException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


# transfer money between account
@app.patch("/account/transfer/<transfer_account_id>/<receiving_account_id>")
def transfer_money_between_account_by_ids(transfer_account_id: str, receiving_account_id: str):
    try:
        body = request.get_json()
        transfer_value = body["transferValue"]
        result = account_service.service_transfer_money_between_account_by_ids(
            int(transfer_account_id),
            int(receiving_account_id),
            float(transfer_value)
        )
        balance = {
            "receivedBalance": result[0],
            "transferredBalance": result[1]
        }
        return balance
    except NegativeBalanceFromTransferringMoneyException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400
    except NegativeMoneyTransferringMoneyException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


# delete account information
@app.delete("/account/<account_id>")
def delete_account_by_id(account_id: str):
    result = account_service.service_delete_account_by_id(int(account_id))
    if result:
        return "Account with ID {} was deleted successfully".format(account_id)
    else:
        return "Something went wrong: account with ID {} was not deleted".format(account_id)


@app.post("/customer")
def create_customer():
    try:
        body = request.get_json()
        new_customer = Customer(
            body["firstName"],
            body["lastName"],
            body["customerEmail"],
            body["customerId"]
        )
        created_customer = customer_service.service_create_customer(new_customer)
        created_customer_as_dictionary = created_customer.create_customer_dictionary()
        return jsonify(created_customer_as_dictionary)
    except DuplicateCreateCustomerEmailException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@app.get("/customer/<customer_id>")
def get_customer_by_id(customer_id: str):
    customer = customer_service.service_get_customer_by_id(int(customer_id))
    customer_as_dictionary = customer.create_customer_dictionary()
    return jsonify(customer_as_dictionary), 200


@app.get("/customer")
def get_all_customer_by_id():
    customers = customer_service.service_get_all_customer_by_id()
    customers_as_dictionaries = []
    for customer in customers:
        dictionary_customer = customer.create_customer_dictionary()
        customers_as_dictionaries.append(dictionary_customer)
    return jsonify(customers_as_dictionaries), 200


@app.patch("/customer/<customer_id>")
def update_customer(customer_id: str):
    try:
        body = request.get_json()
        update_info = Customer(
            body["firstName"],
            body["lastName"],
            body["customerEmail"],
            int(customer_id)
        )
        updated_customer = customer_service.service_update_customer_information(update_info)
        updated_customer_as_dictionary = updated_customer.create_customer_dictionary()
        return jsonify(updated_customer_as_dictionary), 200
    except DuplicateUpdateCustomerEmailException as e:
        return str(e)


@app.delete("/customer/<customer_id>")
def delete_customer(customer_id: str):
    result = customer_service.service_delete_customer_by_id(int(customer_id))
    if result:
        return f"Customer with ID {customer_id} was deleted successfully"
    else:
        return f"Something went wrong. Customer with ID {customer_id} was not deleted"


app.run()
