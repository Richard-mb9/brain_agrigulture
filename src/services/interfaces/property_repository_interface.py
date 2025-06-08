from typing import List, Union
from abc import ABC, abstractmethod

from src.domain import Property


class PropertyRepositoryInterface(ABC):
    @abstractmethod
    def create(self, property: Property) -> Property:
        raise NotImplementedError("Should implement method: create")

    @abstractmethod
    def find_by_id(self, property_id: int) -> Union[Property, None]:
        raise NotImplementedError("Should implement method: find_by_id")

    @abstractmethod
    def find_by_producer_id(self, producer_id: int) -> List[Property]:
        raise NotImplementedError("Should implement method: find_by_producer_id")

    @abstractmethod
    def list_all(self) -> List[Property]:
        raise NotImplementedError("Should implement method: list_all")

    @abstractmethod
    def update(self, property_id: int, data_to_update: dict) -> None:
        raise NotImplementedError("Should implement method: update")

    @abstractmethod
    def delete(self, property_id: int) -> None:
        raise NotImplementedError("Should implement method: delete")
