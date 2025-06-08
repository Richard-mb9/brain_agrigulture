from src.infra import DatabaseManager
from src.infra.repositories import RepositoryManager
from src.services import PlantingService
from src.services.dtos import CreatePlantingDTO, UpdatePlantingDTO
from src.domain import Planting

from ..schemas import (
    CreatePlantingRequest,
    DefaultCreateResponse,
    UpdatePlantingRequest,
    PlantingResponse,
)


class PlantingController:
    def __init__(self, db_manager: DatabaseManager):
        repository_manager = RepositoryManager(db_manager=db_manager)
        self.service = PlantingService(repository_manager)

    def create(self, data: CreatePlantingRequest):
        dto = CreatePlantingDTO(
            property_id=data.propertyId,
            harvest_id=data.harvestId,
            planted_area=data.plantedArea,
            crop_name=data.cropName,
        )

        planting = self.service.create(dto)

        return DefaultCreateResponse(id=planting.id)

    def find_by_id(self, planting_id: int):
        planting = self.service.find_by_id(
            planting_id=planting_id, raise_if_is_none=True
        )
        return self.__build_response(planting)

    def list_all(self, crop_name: str = None):
        plantings = self.service.list_all(crop_name=crop_name)
        return [self.__build_response(planting) for planting in plantings]

    def update(self, planting_id: int, data: UpdatePlantingRequest):
        dto = UpdatePlantingDTO(
            harvest_id=data.harvestId,
            planted_area=data.plantedArea,
            crop_name=data.cropName,
        )

        self.service.update(planting_id=planting_id, data_to_update=dto)

    def __build_response(self, planting: Planting):
        return PlantingResponse(
            id=planting.id,
            propertyId=planting.property_id,
            propertyName=planting.property_name,
            harvestId=planting.harvest_id,
            platedArea=planting.planted_area,
            cropName=planting.crop_name,
        )
