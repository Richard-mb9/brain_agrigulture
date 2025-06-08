from typing import List, Union
from abc import ABC, abstractmethod

from src.domain import Harvest


class HarvestRepositoryInterface(ABC):
    @abstractmethod
    def create(self, harvest: Harvest) -> Harvest:
        raise NotImplementedError("Should implement method: create")

    @abstractmethod
    def find_by_id(self, harvest_id: int) -> Union[Harvest, None]:
        raise NotImplementedError("Should implement method: find_by_id")

    @abstractmethod
    def list_all(self) -> List[Harvest]:
        raise NotImplementedError("Should implement method: list_all")

    @abstractmethod
    def update(self, harvest_id: int, data_to_update: dict) -> None:
        raise NotImplementedError("Should implement method: update")
