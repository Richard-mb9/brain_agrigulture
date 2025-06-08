from json import dumps
from http import HTTPStatus


from src.services import ProducerService
from tests.fixtures.fake_repositories import FakeRepositoriesManager
from tests.fixtures.app import Client


producer_service = ProducerService(FakeRepositoriesManager())


def test_should_create_a_producer(client: Client):

    payload = {
        "name": "francisco",
        "cpfCnpj": "22090106328",
        "documentType": "CPF",
    }
    response = client.post(
        "producers",
        data=dumps(payload),
    )

    assert response.status_code == HTTPStatus.CREATED

    producers = producer_service.list_all(cpf_cnpj=payload["cpfCnpj"])

    assert len(producers) > 0
