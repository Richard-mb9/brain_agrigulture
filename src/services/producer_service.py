from .interfaces import RepositoriesManagerInterface

from src.commons.errors import NotFoundError, ConflictError
from .dtos import CreateProducerDTO, UpdateProducerDTO

from src.domain import Producer


class ProducerService:
    def __init__(self, repositories_manager: RepositoriesManagerInterface):
        self.repository = repositories_manager.producer_repository()

    def create(self, data: CreateProducerDTO):
        p = self.list_all(cpf_cnpj=data.cpf_cnpj)
        if len(p) > 0:
            raise ConflictError(
                "There is already a producer registered with this document"
            )

        producer = Producer(
            name=data.name, cpf_cnpj=data.cpf_cnpj, document_type=data.document_type
        )

        return self.repository.create(producer)

    def find_by_id(self, producer_id: int, raise_if_is_none: bool = False):
        producer = self.repository.find_by_id(producer_id)
        if raise_if_is_none is True and producer is None:
            raise NotFoundError(f"producer with id: {producer_id} not founded")

        return producer

    def update(self, producer_id: int, data_to_update: UpdateProducerDTO):
        self.find_by_id(producer_id=producer_id, raise_if_is_none=True)
        self.repository.update(
            producer_id=producer_id, data_to_update=data_to_update.__dict__
        )

    def list_all(self, cpf_cnpj: str = None):
        return self.repository.list_all(cpf_cnpj=cpf_cnpj)

    def delete(self, producer_id: int):
        self.repository.delete(producer_id)
