from typing import List, Union
from src.domain import Planting
from src.services.interfaces import PlantingRepositoryInterface


class FakePlantingRepository(PlantingRepositoryInterface):
    def __init__(self):
        self.current_id = 1
        self.data: List[Planting] = []

    def create(self, planting: Planting):
        planting.id = self.current_id
        self.data.append(planting)
        self.current_id += 1
        return planting

    def find_by_id(self, planting_id: int) -> Union[Planting, None]:
        for planting in self.data:
            if planting.id == planting_id:
                return planting

    def find_by_property_id(self, property_id: int) -> List[Planting]:
        return [
            planting for planting in self.data if planting.property_id == property_id
        ]

    def list_all(self, crop_name: str = None):
        return [
            planting
            for planting in self.data
            if (crop_name is None or planting == crop_name)
        ]

    def update(self, planting_id: int, data_to_update: dict):
        for entity in self.data:
            if entity.id == planting_id:
                for key in data_to_update:
                    if data_to_update[key] is not None:
                        setattr(entity, key, data_to_update[key])

    def delete(self, planting_id: int):
        self.data = [entity for entity in self.data if entity.id != planting_id]


fake_planting_repository = FakePlantingRepository()
