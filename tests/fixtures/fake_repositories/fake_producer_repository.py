from typing import List, Union
from src.domain import Producer
from src.services.interfaces import ProducerRepositoryInterface


class FakeProducerRepository(ProducerRepositoryInterface):
    def __init__(self):
        self.current_id = 1
        self.producers: List[Producer] = []

    def create(self, producer: Producer):
        producer.id = self.current_id
        self.producers.append(producer)
        self.current_id += 1
        return producer

    def find_by_id(self, producer_id: int) -> Union[Producer, None]:
        for producer in self.producers:
            if producer.id == producer_id:
                return producer

    def list_all(self, cpf_cnpj: str = None):
        return [
            producer
            for producer in self.producers
            if (cpf_cnpj is None or producer.cpf_cnpj == cpf_cnpj)
        ]

    def update(self, producer_id: int, data_to_update: dict):
        for producer in self.producers:
            if producer.id == producer_id:
                for key in data_to_update:
                    if data_to_update[key] is not None:
                        setattr(producer, key, data_to_update[key])

    def delete(self, producer_id: int):
        self.producers = [
            producer for producer in self.producers if producer.id != producer_id
        ]


fake_producer_repository = FakeProducerRepository()
