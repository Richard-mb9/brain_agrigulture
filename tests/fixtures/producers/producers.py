from pytest import fixture

from src.domain import Producer
from tests.fixtures.fake_repositories import fake_producer_repository
from .mock_create_producers_data import MOCK_CREATE_PRODUCERS_DATA


@fixture(scope="function")
def producers():
    for producer in MOCK_CREATE_PRODUCERS_DATA:
        fake_producer_repository.create(
            Producer(
                name=producer["name"],
                cpf_cnpj=producer["cpfCnpj"],
                document_type=producer["documentType"],
            )
        )
