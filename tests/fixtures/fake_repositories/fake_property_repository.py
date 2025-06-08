from typing import Union, List
from src.services.interfaces import PropertyRepositoryInterface
from src.domain import Property


class FakePropertyRepository(PropertyRepositoryInterface):
    def __init__(self):
        self.current_id = 1
        self.data: List[Property] = []

    def create(self, property: Property):
        property.id = self.current_id
        self.data.append(property)
        self.current_id += 1
        return property

    def find_by_id(self, property_id) -> Union[Property, None]:
        for property in self.data:
            if property.id == property_id:
                return property_id

    def find_by_producer_id(self, producer_id: int) -> List[Property]:
        return [
            property for property in self.data if property.producer_id == producer_id
        ]

    def list_all(self) -> List[Property]:
        return self.data

    def update(self, entity_id: int, data_to_update: dict):
        for entity in self.data:
            if entity.id == entity_id:
                for key in data_to_update:
                    if data_to_update[key] is not None:
                        setattr(entity, key, data_to_update[key])

    def delete(self, entity_id: int):
        self.data = [entity for entity in self.data if entity.id != entity_id]


fake_property_repository = FakePropertyRepository()
