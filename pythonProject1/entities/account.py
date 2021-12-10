class Account:
    def __init__(self, account_number: int, account_balance: float, account_id: int, customer_id: int):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_id = account_id
        self.customer_id = customer_id

    def make_account_dictionary(self):
        return {
            "accountNumber": self.account_number,
            "accountBalance": self.account_balance,
            "accountId": self.account_id,
            "customerId": self.customer_id
        }

    def __str__(self):
        return "account number: {}, account balance: {}, account ID: {}, customer ID: {}".format(
            self.account_number,
            self.account_balance,
            self. account_id,
            self.customer_id
        )
