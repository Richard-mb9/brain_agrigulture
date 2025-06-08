from typing import Union, List
from src.services.interfaces import HarvestRepositoryInterface
from src.domain import Harvest


class FakeHarvestRepository(HarvestRepositoryInterface):
    def __init__(self):
        self.current_id = 1
        self.data: List[Harvest] = []

    def create(self, harvest: Harvest) -> Harvest:
        harvest.id = self.current_id
        self.data.append(harvest)
        self.current_id += 1
        return harvest

    def find_by_id(self, harvest_id: int) -> Union[Harvest, None]:
        for harvest in self.data:
            if harvest.id == harvest_id:
                return harvest

    def list_all(self) -> List[Harvest]:
        return self.data

    def update(self, entity_id: int, data_to_update: dict):
        for entity in self.data:
            if entity.id == entity_id:
                for key in data_to_update:
                    if data_to_update[key] is not None:
                        setattr(entity, key, data_to_update[key])


fake_harvest_repository = FakeHarvestRepository()
