from custom_exceptions.duplicate_customer_name_exception import DuplicateCreateCustomerEmailException, \
    DuplicateUpdateCustomerEmailException
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customer import Customer
from service_layer.implementation_services.customer_postgres_service import CustomerPostgresService

customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresService(customer_dao)

bad_customer = Customer("bad", "customer", "duplicate_email@email.com", 2)
bad_update_customer = Customer("bad", "update customer", "update_email@email.com", 2)


def test_catch_creating_customer_with_duplicate_email():
    try:
        customer_service.service_create_customer(bad_customer)
    except DuplicateCreateCustomerEmailException as e:
        assert str(e) == "You can not create that email: it is already taken"


def test_catch_updating_customer_with_duplicate_email():
    try:
        customer_service.service_update_customer_information(bad_update_customer)
    except DuplicateUpdateCustomerEmailException as e:
        assert str(e) == "You can not use that email: it is already taken"
