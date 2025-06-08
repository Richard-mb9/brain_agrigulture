from typing import Union, List
from src.services.interfaces import PlantingRepositoryInterface
from src.infra import DatabaseManager
from src.domain import Planting


class PlantingRepository(PlantingRepositoryInterface):
    def __init__(self, db_manager: DatabaseManager):
        self.session = db_manager.get_session()

    def create(self, planting: Planting):
        self.session.add(planting)
        self.session.commit()
        return planting

    def find_by_id(self, planting_id: int) -> Union[Planting, None]:
        return self.session.query(Planting).filter_by(id=planting_id).first()

    def find_by_property_id(self, property_id: int) -> List[Planting]:
        return self.session.query(Planting).filter_by(property_id=property_id).all()

    def list_all(self, crop_name: str = None):
        filters = []
        if crop_name is not None:
            filters.append(Planting.crop_name.like(f"%{crop_name}%"))
        return self.session.query(Planting).filter(*filters).all()

    def update(self, planting_id: int, data_to_update: dict):
        entity = self.find_by_id(planting_id)
        if entity is not None:
            for key in data_to_update:
                if data_to_update[key] is not None:
                    setattr(entity, key, data_to_update[key])
            self.session.commit()

    def delete(self, producer_id: int):
        entity = self.find_by_id(producer_id)
        if entity is not None:
            self.session.delete(entity)
            self.session.commit()
