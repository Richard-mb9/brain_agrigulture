from src.infra import DatabaseManager
from src.infra.repositories import RepositoryManager
from src.services import ProducerService
from src.services.dtos import CreateProducerDTO, UpdateProducerDTO
from src.domain import Producer

from ..schemas import (
    DefaultCreateResponse,
    CreateProducerRequest,
    UpdateProducerRequest,
    ProducerResponse,
    PropertyResponse,
)


class ProducerController:
    def __init__(self, db_manager: DatabaseManager):
        repository_manager = RepositoryManager(db_manager=db_manager)
        self.service = ProducerService(repository_manager)

    def create(self, data: CreateProducerRequest):
        dto = CreateProducerDTO(
            name=data.name, cpf_cnpj=data.cpfCnpj, document_type=data.documentType
        )

        producer = self.service.create(dto)
        return DefaultCreateResponse(id=producer.id)

    def find_by_id(self, producer_id: int):
        producer = self.service.find_by_id(
            producer_id=producer_id, raise_if_is_none=True
        )

        return self.__build_response(producer)

    def list_all(self, cpf_cnpj: str = None):
        producers = self.service.list_all(cpf_cnpj=cpf_cnpj)
        return [self.__build_response(producer) for producer in producers]

    def update(self, producer_id: int, data: UpdateProducerRequest):
        dto = UpdateProducerDTO(
            name=data.name,
            cpf_cnpj=data.cpfCnpj,
            document_type=data.documentType,
        )

        self.service.update(producer_id=producer_id, data_to_update=dto)

    def delete(self, producer_id: int):
        self.service.delete(producer_id)

    def __build_response(self, producer: Producer):
        return ProducerResponse(
            id=producer.id,
            name=producer.name,
            cpfCnpj=producer.cpf_cnpj,
            documentType=producer.document_type,
            createdAt=producer.created_at,
            properties=[
                PropertyResponse(
                    id=property.id,
                    producerId=property.producer_id,
                    name=property.name,
                    city=property.city,
                    state=property.state,
                    totalArea=property.total_area,
                    agriculturalArea=property.agricultural_area,
                    areaVegetation=property.area_vegetation,
                )
                for property in producer.properties
            ],
        )
