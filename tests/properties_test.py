from json import dumps
from http import HTTPStatus


from src.services import PropertyService
from tests.fixtures.fake_repositories import FakeRepositoriesManager
from tests.fixtures.app import Client
from .producers_test import create_producer_returning_id

properties_service = PropertyService(FakeRepositoriesManager())


DEFAULT_PROPERTY = {
    "name": "Fazenda do Francisco",
    "city": "Resende",
    "state": "RJ",
    "totalArea": 1000,
    "agriculturalArea": 900,
    "areaVegetation": 100,
}


def create_property_returning_id(client: Client, producer_id: int = None):
    if producer_id is None:
        producer_id = create_producer_returning_id(client)

    payload = {"producerId": producer_id, **DEFAULT_PROPERTY}

    response = client.post("properties", data=dumps(payload))
    response_data = response.json()
    return response_data["id"]


def test_should_create_a_property(client: Client):
    payload = {"producerId": create_producer_returning_id(client), **DEFAULT_PROPERTY}

    response = client.post("properties", data=dumps(payload))

    assert response.status_code == HTTPStatus.CREATED

    response_data = response.json()
    assert response_data.get("id") is not None


def test_should_return_bad_request_error_if_invalid_area(client: Client):
    payload = {
        "producerId": create_producer_returning_id(client),
        "name": "Fazenda do Francisco",
        "city": "Resende",
        "state": "RJ",
        "totalArea": 1000,
        "agriculturalArea": 1000,
        "areaVegetation": 100,
    }

    response = client.post("properties", data=dumps(payload))

    assert response.status_code == HTTPStatus.BAD_REQUEST

    response_data = response.json()
    assert (
        response_data.get("detail")
        == "The area of vegetation and the agricultural area combined cannot be greater than the total area."
    )


def test_should_list_all_properties(client: Client):
    producer_id = create_producer_returning_id(client)
    for _ in range(0, 10):
        create_property_returning_id(client, producer_id=producer_id)

    response = client.get("properties")

    assert response.status_code == HTTPStatus.OK

    response_data = response.json()

    assert len(response_data) == 10


def test_should_find_property_by_id(client: Client):
    property_id = create_property_returning_id(client)

    response = client.get(f"properties/{property_id}")

    assert response.status_code == HTTPStatus.OK

    response_data = response.json()

    assert response_data["name"] == DEFAULT_PROPERTY["name"]


def test_should_return_status_404_if_property_not_exist(client: Client):
    response = client.get("properties/123")

    assert response.status_code == HTTPStatus.NOT_FOUND

    response_data = response.json()

    assert response_data["detail"] == "property with id: 123 not founded"


def test_find_by_producer_id(client: Client):
    producer_id_1 = create_producer_returning_id(client)
    producer_id_2 = create_producer_returning_id(client=client, cpf_cnpj="09538085051")

    for _ in range(0, 5):
        create_property_returning_id(client, producer_id_1)

    for _ in range(0, 5):
        create_property_returning_id(client, producer_id_2)

    response = client.get(f"properties/producer/{producer_id_1}")

    assert response.status_code == HTTPStatus.OK

    response_data = response.json()

    assert len(response_data) == 5

    for property in response_data:
        assert property["producerId"] == producer_id_1


def test_should_update_property(client: Client):
    property_id = create_property_returning_id(client)

    payload = {"name": "updated"}

    response = client.put(f"properties/{property_id}", data=dumps(payload))

    assert response.status_code == HTTPStatus.NO_CONTENT

    property = properties_service.find_by_id(property_id, True)

    assert property.name == payload["name"]
    assert property.city == DEFAULT_PROPERTY["city"]


def test_should_delete_property(client: Client):
    assert len(properties_service.list_all()) == 0
    property_id = create_property_returning_id(client)
    assert len(properties_service.list_all()) == 1

    response = client.delete(f"properties/{property_id}")

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert len(properties_service.list_all()) == 0
