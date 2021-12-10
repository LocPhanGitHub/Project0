from data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from entities.customer import Customer

customer_dao = CustomerDAOImp()
# create a test customer
customer_one = Customer("test", "customer", "emailone@email.com", 1)
# update test customer to updated customer
updated_customer = Customer("updated", "customer", "newemail@email.com", 2)


def test_create_customer_success():
    create_customer = customer_dao.create_customer(customer_one)
    assert create_customer.customer_id != 0


def test_get_customer_information_by_id_success():
    selected_customer = customer_dao.get_customer_by_id(2)
    assert selected_customer.customer_id == 2


def test_get_all_customer_information_by_id_success():
    customers = customer_dao.get_all_customer_by_id()
    assert len(customers) >= 2


def test_update_customer_by_id_success():
    result: Customer = customer_dao.update_customer_information(updated_customer)
    assert result.first_name == updated_customer.first_name and result.last_name == updated_customer.last_name


def test_delete_customer_by_id_success():
    result = customer_dao.delete_customer_by_id(4)
    assert result
