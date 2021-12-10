from abc import ABC, abstractmethod
from typing import List

from entities.customer import Customer


class CustomerDAO(ABC):

    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def get_all_customer_by_id(self) -> List[Customer]:
        pass

    @abstractmethod
    def update_customer_information(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
