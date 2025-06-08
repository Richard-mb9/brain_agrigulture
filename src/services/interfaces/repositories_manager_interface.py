from abc import ABC, abstractmethod

from .producer_repository_interface import ProducerRepositoryInterface
from .property_repository_interface import PropertyRepositoryInterface
from .plating_repository_interface import PlantingRepositoryInterface
from .harvest_repository_interface import HarvestRepositoryInterface


class RepositoriesManagerInterface(ABC):
    @abstractmethod
    def producer_repository(self) -> ProducerRepositoryInterface:
        raise NotImplementedError("Should implement method: producer_repository")

    @abstractmethod
    def property_repository(self) -> PropertyRepositoryInterface:
        raise NotImplementedError("Should implement method: property_repository")

    @abstractmethod
    def planting_repository(self) -> PlantingRepositoryInterface:
        raise NotImplementedError("Should implement method: property_repository")

    @abstractmethod
    def harvest_repository(self) -> HarvestRepositoryInterface:
        raise NotImplementedError("Should implement method: property_repository")
