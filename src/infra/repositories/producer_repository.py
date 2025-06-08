from typing import List, Union
from src.services.interfaces import ProducerRepositoryInterface
from src.infra import DatabaseManager
from src.domain import Producer


class ProducerRepository(ProducerRepositoryInterface):
    def __init__(self, db_manager: DatabaseManager):
        self.session = db_manager.get_session()

    def create(self, producer: Producer):
        self.session.add(producer)
        self.session.commit()
        return producer

    def find_by_id(self, producer_id: int) -> Union[Producer, None]:
        return self.session.query(Producer).filter_by(id=producer_id).first()

    def list_all(self, cpf_cnpj: str = None) -> List[Producer]:
        filters = []
        if cpf_cnpj is not None:
            filters.append(Producer.cpf_cnpj == cpf_cnpj)

        return self.session.query(Producer).filter(*filters).all()

    def update(self, producer_id: int, data_to_update: dict):
        entity = self.find_by_id(producer_id)
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
