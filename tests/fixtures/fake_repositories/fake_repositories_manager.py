from src.services.interfaces import RepositoriesManagerInterface

from .fake_producer_repository import fake_producer_repository
from .fake_property_repository import fake_property_repository
from .fake_planting_repository import fake_planting_repository
from .fake_harvest_repository import fake_harvest_repository


class FakeRepositoriesManager(RepositoriesManagerInterface):
    def producer_repository(self):
        return fake_producer_repository

    def property_repository(self):
        return fake_property_repository

    def planting_repository(self):
        return fake_planting_repository

    def harvest_repository(self):
        return fake_harvest_repository
