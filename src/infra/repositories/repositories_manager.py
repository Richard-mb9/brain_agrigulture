from src.services.interfaces import (
    RepositoriesManagerInterface,
    ProducerRepositoryInterface,
    PropertyRepositoryInterface,
    PlantingRepositoryInterface,
    HarvestRepositoryInterface,
)
from src.infra import DatabaseManager


from .producer_repository import ProducerRepository
from .property_repository import PropertyRepository
from .planting_repository import PlantingRepository
from .harvest_repository import HarvestRepository


class RepositoryManager(RepositoriesManagerInterface):
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def producer_repository(self) -> ProducerRepositoryInterface:
        return ProducerRepository(self.db_manager)

    def property_repository(self) -> PropertyRepositoryInterface:
        return PropertyRepository(self.db_manager)

    def planting_repository(self) -> PlantingRepositoryInterface:
        return PlantingRepository(self.db_manager)

    def harvest_repository(self) -> HarvestRepositoryInterface:
        return HarvestRepository(self.db_manager)
