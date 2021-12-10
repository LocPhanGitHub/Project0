from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customer import Customer

customer_dao = CustomerPostgresDAO()

new_customer = Customer("new", "customer", "newcustomer@email.com", 0)

update_customer = Customer("update", "customer", "updatecustomer@email.com", 0)

delete_customer = Customer("deleted", "customer", "customertobedeleted@email.com", 0)


def test_create_customer_success():
    customer_result = customer_dao.create_customer(new_customer)
    assert customer_result.customer_id != 0


def test_select_customer_by_id_success():
    initial_customer = customer_dao.get_customer_by_id(1)
    assert initial_customer.customer_id == 1


def test_select_all_customer_success():
    customers = customer_dao.get_all_customer_by_id()
    assert len(customers) >= 2


def test_update_customer_success():
    to_be_updated_customer = customer_dao.update_customer_information(update_customer)
    assert to_be_updated_customer.customer_email == update_customer.customer_email


def test_delete_customer_success():
    to_be_deleted = customer_dao.create_customer(delete_customer)
    result = customer_dao.delete_customer_by_id(to_be_deleted.customer_id)
    assert result
