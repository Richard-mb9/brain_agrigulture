from src.infra import DatabaseManager
from src.infra.repositories import RepositoryManager
from src.services import HarvestService
from src.services.dtos import CreateHarvestDTO, UpdateHarvestDTO
from src.domain import Harvest

from ..schemas import (
    CreateHarvestRequest,
    DefaultCreateResponse,
    HarvestResponse,
    UpdateHarvestRequest,
)


class HarvestController:
    def __init__(self, db_manager: DatabaseManager):
        repository_manager = RepositoryManager(db_manager=db_manager)
        self.service = HarvestService(repository_manager)

    def create(self, data: CreateHarvestRequest):
        dto = CreateHarvestDTO(
            name=data.name, start_date=data.startDate, end_date=data.endDate
        )

        harvest = self.service.create(dto)

        return DefaultCreateResponse(id=harvest.id)

    def find_by_id(self, harvest_id: int):
        harvest = self.service.find_by_id(harvest_id=harvest_id, raise_if_is_none=True)
        return self.__build_response(harvest)

    def list_all(self):
        harvests = self.service.list_all()
        return [self.__build_response(harvest) for harvest in harvests]

    def update(self, harvest_id: int, data: UpdateHarvestRequest):
        dto = UpdateHarvestDTO(
            name=data.name, start_date=data.startDate, end_date=data.endDate
        )

        self.service.update(harvest_id=harvest_id, data_to_update=dto)

    def __build_response(self, harvest: Harvest):
        return HarvestResponse(
            id=harvest.id,
            name=harvest.name,
            startDate=harvest.start_date,
            endDate=harvest.end_date,
        )
