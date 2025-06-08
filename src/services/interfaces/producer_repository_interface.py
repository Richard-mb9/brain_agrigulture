from typing import List, Union
from abc import ABC, abstractmethod

from src.domain import Producer


class ProducerRepositoryInterface(ABC):
    @abstractmethod
    def create(self, producer: Producer) -> Producer:
        raise NotImplementedError("Should implement method: create")

    @abstractmethod
    def find_by_id(self, producer_id: int) -> Union[Producer, None]:
        raise NotImplementedError("Should implement method: find_by_id")

    @abstractmethod
    def list_all(self, cpf_cnpj: str = None) -> List[Producer]:
        raise NotImplementedError("Should implement method: list_all")

    @abstractmethod
    def update(self, producer_id: int, data_to_update: dict) -> None:
        raise NotImplementedError("Should implement method: update")

    @abstractmethod
    def delete(self, producer_id: int) -> None:
        raise NotImplementedError("Should implement method: delete")
