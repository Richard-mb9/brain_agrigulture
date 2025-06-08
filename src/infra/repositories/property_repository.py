from typing import List, Union
from src.services.interfaces import PropertyRepositoryInterface
from src.infra import DatabaseManager
from src.domain import Property


class PropertyRepository(PropertyRepositoryInterface):
    def __init__(self, db_manager: DatabaseManager):
        self.session = db_manager.get_session()

    def create(self, property: Property):
        self.session.add(property)
        self.session.commit()
        return property

    def find_by_id(self, property_id: int) -> Union[Property, None]:
        return self.session.query(Property).filter_by(id=property_id).first()

    def find_by_producer_id(self, producer_id: int) -> List[Property]:
        return self.session.query(Property).filter_by(producer_id=producer_id).all()

    def list_all(self):
        return self.session.query(Property).all()

    def update(self, entity_id: int, data_to_update: dict):
        entity = self.find_by_id(entity_id)
        if entity is not None:
            for key in data_to_update:
                if data_to_update[key] is not None:
                    setattr(entity, key, data_to_update[key])
            self.session.commit()

    def delete(self, entity_id: int):
        entity = self.find_by_id(entity_id)
        if entity is not None:
            self.session.delete(entity)
            self.session.commit()
