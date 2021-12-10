class DuplicateCreateCustomerEmailException(Exception):
    def __init__(self, message: str):
        self.message = message


class DuplicateUpdateCustomerEmailException(Exception):
    def __init__(self, message: str):
        self.message = message
