from typing import List, Union
from abc import ABC, abstractmethod

from src.domain import Planting


class PlantingRepositoryInterface(ABC):

    @abstractmethod
    def create(self, planting: Planting) -> Planting:
        raise NotImplementedError("Should implement method: create")

    @abstractmethod
    def find_by_id(self, planting_id: int) -> Union[Planting, None]:
        raise NotImplementedError("Should implement method: find_by_id")

    @abstractmethod
    def find_by_property_id(self, property_id: int) -> List[Planting]:
        raise NotImplementedError("Should implement method: find_by_property_id")

    @abstractmethod
    def list_all(self, crop_name: str = None) -> List[Planting]:
        raise NotImplementedError("Should implement method: list_all")

    @abstractmethod
    def update(self, planting_id: int, data_to_update: dict) -> None:
        raise NotImplementedError("Should implement method: update")

    @abstractmethod
    def delete(self, planting_id: int) -> None:
        raise NotImplementedError("Should implement method: delete")
