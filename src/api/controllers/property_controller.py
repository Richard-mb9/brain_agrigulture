from src.infra import DatabaseManager
from src.infra.repositories import RepositoryManager
from src.services import PropertyService
from src.services.dtos import CreatePropertyDTO, UpdatePropertyDTO
from src.domain import Property

from ..schemas import (
    CreatePropertyRequest,
    DefaultCreateResponse,
    PropertyResponse,
    UpdatePropertyRequest,
)


class PropertyController:
    def __init__(self, db_manager: DatabaseManager):
        repository_manager = RepositoryManager(db_manager=db_manager)
        self.service = PropertyService(repository_manager)

    def create(self, data: CreatePropertyRequest):
        dto = CreatePropertyDTO(
            producer_id=data.producerId,
            name=data.name,
            city=data.city,
            state=data.state,
            total_area=data.totalArea,
            agricultural_area=data.agriculturalArea,
            area_vegetation=data.areaVegetation,
        )

        property = self.service.create(dto)

        return DefaultCreateResponse(id=property.id)

    def find_by_id(self, property_id: int):
        property = self.service.find_by_id(
            property_id=property_id, raise_if_is_none=True
        )
        return self.__build_response(property)

    def find_by_producer_id(self, producer_id: int):
        properties = self.service.find_by_producer_id(producer_id)
        return [self.__build_response(property) for property in properties]

    def list_all(self):
        properties = self.service.list_all()
        return [self.__build_response(property) for property in properties]

    def update(self, property_id: int, data: UpdatePropertyRequest):
        dto = UpdatePropertyDTO(
            producer_id=data.producerId,
            name=data.name,
            city=data.city,
            state=data.state,
            total_areal=data.totalAreal,
            agricultural_area=data.agriculturalArea,
            area_vegetation=data.areaVegetation,
        )

        self.service.update(property_id=property_id, data_to_update=dto)

    def delete(self, property_id: int):
        self.service.delete(property_id)

    def __build_response(self, property: Property):
        return PropertyResponse(
            id=property.id,
            producerId=property.producer_id,
            name=property.name,
            city=property.city,
            state=property.state,
            totalArea=property.total_area,
            agriculturalArea=property.agricultural_area,
            areaVegetation=property.area_vegetation,
        )
