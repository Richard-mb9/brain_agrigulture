from .interfaces import RepositoriesManagerInterface

from src.commons.errors import NotFoundError
from src.domain import Planting


from .dtos import CreatePlantingDTO, UpdatePlantingDTO


class PlantingService:
    def __init__(self, repositories_manager: RepositoriesManagerInterface):
        self.repository_manager = repositories_manager
        self.repository = repositories_manager.planting_repository()

    def create(self, data: CreatePlantingDTO):
        from .property_service import PropertyService

        property_service = PropertyService(self.repository_manager)
        property = property_service.find_by_id(data.property_id, True)

        planting = Planting(
            property_id=data.property_id,
            property_name=property.name,
            harvest_id=data.harvest_id,
            planted_area=data.planted_area,
            crop_name=data.crop_name.upper(),
        )

        return self.repository.create(planting)

    def find_by_id(self, planting_id: int, raise_if_is_none: bool = False):
        planting = self.repository.find_by_id(planting_id=planting_id)
        if raise_if_is_none is True and planting is None:
            raise NotFoundError(f"planting with id: {planting_id} not founded")
        return planting

    def update(self, planting_id: int, data_to_update: UpdatePlantingDTO):
        self.find_by_id(planting_id=planting_id, raise_if_is_none=True)
        self.repository.update(
            planting_id=planting_id, data_to_update=data_to_update.__dict__
        )

    def list_all(self, crop_name: str = None):
        return self.repository.list_all(
            crop_name=(crop_name.upper() if crop_name else None)
        )
