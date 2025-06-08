from .interfaces import RepositoriesManagerInterface

from src.commons.errors import NotFoundError, BadRequestError
from src.domain import Harvest

from .dtos import CreateHarvestDTO, UpdateHarvestDTO


class HarvestService:
    def __init__(self, repositories_manager: RepositoriesManagerInterface):
        self.repository = repositories_manager.harvest_repository()

    def create(self, data: CreateHarvestDTO):
        harvest = Harvest(
            name=data.name, start_date=data.start_date, end_date=data.end_date
        )

        return self.repository.create(harvest)

    def find_by_id(self, harvest_id: int, raise_if_is_none: bool = False):
        harvest = self.repository.find_by_id(harvest_id=harvest_id)
        if raise_if_is_none is True and harvest is None:
            raise NotFoundError(f"harvest with id: {harvest_id} not founded")
        return harvest

    def update(self, harvest_id: int, data_to_update: UpdateHarvestDTO):
        harvest = self.find_by_id(harvest_id=harvest_id, raise_if_is_none=True)
        if (
            harvest.start_date is not None
            and data_to_update.end_date is not None
            and data_to_update.start_date is None
        ):
            if harvest.start_date > data_to_update.end_date:
                raise BadRequestError(
                    "the end date cannot be greater than the start date"
                )
        elif (
            harvest.end_date is not None
            and data_to_update.start_date is not None
            and data_to_update.end_date is None
        ):
            if harvest.end_date < data_to_update.start_date:
                raise BadRequestError(
                    "the end date cannot be greater than the start date"
                )
        self.repository.update(
            harvest_id=harvest_id, data_to_update=data_to_update.__dict__
        )

    def list_all(self):
        return self.repository.list_all()
