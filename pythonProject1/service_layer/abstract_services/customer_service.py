from abc import ABC, abstractmethod
from typing import List

from entities.customer import Customer


class CustomerService(ABC):
    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_get_all_customer_by_id(self) -> List[Customer]:
        pass

    @abstractmethod
    def service_update_customer_information(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        pass
