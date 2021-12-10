from data_access_layer.abstract_classes.customer_dao import CustomerDAO
from entities.customer import Customer


class CustomerDAOImp(CustomerDAO):
    customer_two = Customer("customer", "one", "emailtwo@email.com", 2)
    customer_three = Customer("customer", "two", "emailthree@email.com", 3)
    customer_four = Customer("customer", "three", "emailfour@email.com", 4)
    customer_list = [customer_two, customer_three, customer_four]
    customer_id_generator = 5

    def create_customer(self, customer: Customer) -> Customer:
        new_customer = customer
        new_customer.customer_id = CustomerDAOImp.customer_id_generator
        CustomerDAOImp.customer_id_generator += 1
        CustomerDAOImp.customer_list.append(new_customer)
        return new_customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        for customer in CustomerDAOImp.customer_list:
            if customer.customer_id == customer_id:
                return customer

    def get_all_customer_by_id(self) -> list[Customer]:
        return CustomerDAOImp.customer_list

    def update_customer_information(self, customer: Customer) -> Customer:
        for customer_in_list in CustomerDAOImp.customer_list:
            if customer_in_list.customer_id == customer.customer_id:
                index = CustomerDAOImp.customer_list.index(customer_in_list)
                CustomerDAOImp.customer_list[index] = customer
                return customer

    def delete_customer_by_id(self, customer_id: int) -> bool:
        for customer in CustomerDAOImp.customer_list:
            if customer.customer_id == customer_id:
                index = CustomerDAOImp.customer_list.index(customer)
                del CustomerDAOImp.customer_list[index]
                return True
