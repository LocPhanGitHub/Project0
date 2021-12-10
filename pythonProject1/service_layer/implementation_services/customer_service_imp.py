from typing import List

from custom_exceptions.duplicate_customer_name_exception import DuplicateCreateCustomerEmailException, \
    DuplicateUpdateCustomerEmailException
from data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from entities.customer import Customer
from service_layer.abstract_services.customer_service import CustomerService


class CustomerServiceImp(CustomerService):

    def __init__(self, customer_dao: CustomerDAOImp):
        self.customer_dao = customer_dao

    def service_create_customer(self, customer: Customer) -> Customer:
        for existing_customer in self.customer_dao.customer_list:
            if existing_customer.customer_email == customer.customer_email:
                raise DuplicateCreateCustomerEmailException("You can not create that email: it is already taken")
        new_customer = self.customer_dao.create_customer(customer)
        return new_customer

    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_by_id(customer_id)

    def service_get_all_customer_by_id(self) -> List[Customer]:
        return self.customer_dao.get_all_customer_by_id()

    def service_update_customer_information(self, customer: Customer) -> Customer:
        for existing_customer in self.customer_dao.customer_list:
            if existing_customer.customer_id != customer.customer_id:
                if existing_customer.customer_email == customer.customer_email:
                    raise DuplicateUpdateCustomerEmailException("You can not use that email: it is already taken")
        updated_customer = self.customer_dao.update_customer_information(customer)
        return updated_customer

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_by_id(customer_id)
