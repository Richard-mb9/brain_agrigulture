from typing import Union, List
from src.services.interfaces import HarvestRepositoryInterface
from src.infra import DatabaseManager
from src.domain import Harvest


class HarvestRepository(HarvestRepositoryInterface):
    def __init__(self, db_manager: DatabaseManager):
        self.session = db_manager.get_session()

    def create(self, harvest: Harvest):
        self.session.add(harvest)
        self.session.commit()
        return harvest

    def find_by_id(self, harvest_id: int) -> Union[Harvest, None]:
        return self.session.query(Harvest).filter_by(id=harvest_id).first()

    def list_all(self) -> List[Harvest]:
        return self.session.query(Harvest).all()

    def update(self, harvest_id: int, data_to_update: dict):
        entity = self.find_by_id(harvest_id)
        if entity is not None:
            for key in data_to_update:
                if data_to_update[key] is not None:
                    setattr(entity, key, data_to_update[key])
            self.session.commit()
