from .interfaces import RepositoriesManagerInterface

from src.commons.errors import NotFoundError

from src.domain import Property

from .dtos import CreatePropertyDTO, UpdatePropertyDTO


class PropertyService:
    def __init__(self, repositories_manager: RepositoriesManagerInterface):
        self.repositories_manager = repositories_manager
        self.repository = repositories_manager.property_repository()

    def create(self, data: CreatePropertyDTO):
        property = Property(
            producer_id=data.producer_id,
            name=data.name,
            city=data.city,
            state=data.state,
            total_area=data.total_area,
            agricultural_area=data.agricultural_area,
            area_vegetation=data.area_vegetation,
        )

        return self.repository.create(property)

    def find_by_id(self, property_id: int, raise_if_is_none: bool = False):
        property = self.repository.find_by_id(property_id)
        if raise_if_is_none is True and property is None:
            raise NotFoundError(f"property with id: {property_id} not founded")
        return property

    def find_by_producer_id(self, producer_id: int):
        from .producer_service import ProducerService

        producer_service = ProducerService(self.repositories_manager)
        producer_service.find_by_id(producer_id=producer_id, raise_if_is_none=True)
        return self.repository.find_by_producer_id(producer_id)

    def list_all(self):
        return self.repository.list_all()

    def update(self, property_id: int, data_to_update: UpdatePropertyDTO):
        self.find_by_id(property_id=property_id, raise_if_is_none=True)
        self.repository.update(
            property_id=property_id, data_to_update=data_to_update.__dict__
        )

    def delete(self, property_id: int):
        self.repository.delete(property_id)
