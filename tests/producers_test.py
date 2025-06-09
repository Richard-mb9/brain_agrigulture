# pylint: disable=W0613
from json import dumps
from http import HTTPStatus
from copy import deepcopy


from src.services import ProducerService
from tests.fixtures.fake_repositories import FakeRepositoriesManager
from tests.fixtures.app import Client


producer_service = ProducerService(FakeRepositoriesManager())

DEFAULT_PRODUCER = {
    "name": "francisco",
    "cpfCnpj": "22090106328",
    "documentType": "CPF",
}


def create_producer_returning_id(client: Client, cpf_cnpj: str = None):
    payload = deepcopy(DEFAULT_PRODUCER)

    if cpf_cnpj is not None:
        payload["cpfCnpj"] = cpf_cnpj

    response = client.post("producers", dumps(payload))
    response_data = response.json()
    return response_data["id"]


def test_should_create_a_producer(client: Client):

    response = client.post(
        "producers",
        data=dumps(DEFAULT_PRODUCER),
    )

    assert response.status_code == HTTPStatus.CREATED

    producers = producer_service.list_all(cpf_cnpj=DEFAULT_PRODUCER["cpfCnpj"])

    assert len(producers) > 0


def test_should_not_create_two_producer_with_same_document(client: Client):

    client.post(
        "producers",
        data=dumps(DEFAULT_PRODUCER),
    )
    response = client.post(
        "producers",
        data=dumps(DEFAULT_PRODUCER),
    )

    assert response.status_code == HTTPStatus.CONFLICT

    response_data = response.json()
    assert (
        response_data.get("detail")
        == "There is already a producer registered with this document"
    )


def test_should_list_all_producers(client: Client, producers):
    response = client.get("producers")
    assert response.status_code == HTTPStatus.OK

    response_data = response.json()
    assert len(response_data) == 10


def test_should_get_producer_by_document(client: Client, producers):
    document = "22090106328"
    response = client.get("producers", params={"cpfCnpj": document})

    assert response.status_code == HTTPStatus.OK
    response_data = response.json()

    assert len(response_data) == 1

    assert response_data[0].get("cpfCnpj") == document


def test_should_find_producer_by_id(client: Client):
    producer_id = create_producer_returning_id(client)

    response = client.get(f"producers/{producer_id}")

    assert response.status_code == HTTPStatus.OK

    response_data = response.json()

    assert response_data.get("cpfCnpj") == DEFAULT_PRODUCER["cpfCnpj"]


def test_should_return_http_status_404_if_producer_not_exist(client: Client):
    response = client.get("producers/123")
    assert response.status_code == HTTPStatus.NOT_FOUND

    response_data = response.json()
    assert response_data.get("detail") == "producer with id: 123 not founded"


def test_should_update_producer(client: Client):
    producer_id = create_producer_returning_id(client)

    payload_to_update = {"name": "updated"}

    response = client.put(f"producers/{producer_id}", data=dumps(payload_to_update))

    assert response.status_code == HTTPStatus.NO_CONTENT

    producer = producer_service.find_by_id(producer_id)

    assert producer.name == payload_to_update["name"]


def test_should_delete_producer(client: Client):
    assert len(producer_service.list_all()) == 0

    producer_id = create_producer_returning_id(client)

    assert len(producer_service.list_all()) == 1

    response = client.delete(f"producers/{producer_id}")

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert len(producer_service.list_all()) == 0
