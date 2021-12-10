from typing import List

from data_access_layer.abstract_classes.customer_dao import CustomerDAO
from entities.customer import Customer
from util.database_connection import connection


class CustomerPostgresDAO(CustomerDAO):
    def create_customer(self, customer: Customer) -> Customer:
        sql = "insert into customer values(%s, %s, %s, default) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.customer_email))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        customer.customer_id = generated_id
        return customer

    def get_customer_by_id(self, customer_id: int) -> Customer:
        sql = "select * from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer

    def get_all_customer_by_id(self) -> List[Customer]:
        sql = "select * from customer"
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_records = cursor.fetchall()
        customers = []
        for customer in customer_records:
            customers.append(Customer(*customer))
        return customers

    def update_customer_information(self, customer: Customer) -> Customer:
        sql = "update customer set customer_email = %s where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.customer_email, customer.customer_id))
        connection.commit()
        return customer

    def delete_customer_by_id(self, customer_id: int) -> bool:
        sql = "delete from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True
