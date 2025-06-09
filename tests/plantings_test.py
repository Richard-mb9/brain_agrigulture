from json import dumps
from http import HTTPStatus


from src.services import PlantingService
from tests.fixtures.fake_repositories import FakeRepositoriesManager
from tests.fixtures.app import Client

from .harvest_test import create_harvest_returning_id
from .properties_test import create_property_returning_id
from .producers_test import create_producer_returning_id

planting_service = PlantingService(FakeRepositoriesManager())


DEFAULT_PLANTING = {"plantedArea": 500, "cropName": "ARROZ"}


def create_planting_returning_id(
    client: Client,
    property_id: int = None,
    harvest_id: int = None,
    producer_id: int = None,
    producer_document: str = None,
):
    if producer_id is None:
        producer_id = create_producer_returning_id(client, cpf_cnpj=producer_document)

    if property_id is None:
        property_id = create_property_returning_id(client, producer_id=producer_id)

    if harvest_id is None:
        harvest_id = create_harvest_returning_id(client)

    payload = {"propertyId": property_id, "harvestId": harvest_id, **DEFAULT_PLANTING}

    response = client.post("plantings", data=dumps(payload))
    response_data = response.json()
    return response_data["id"]


def test_should_create_planting(client: Client):
    property_id = create_property_returning_id(client)
    harvest_id = create_harvest_returning_id(client)

    payload = {"propertyId": property_id, "harvestId": harvest_id, **DEFAULT_PLANTING}

    response = client.post("plantings", data=dumps(payload))

    assert response.status_code == HTTPStatus.CREATED

    response_data = response.json()

    assert response_data.get("id") is not None


def test_should_list_all_plantings(client: Client):
    producer_id = create_producer_returning_id(client)

    for _ in range(0, 5):
        create_planting_returning_id(client=client, producer_id=producer_id)

    response = client.get("plantings")
    assert response.status_code == HTTPStatus.OK

    response_data = response.json()
    assert len(response_data) == 5


def test_should_find_planting_by_id(client: Client):
    planting_id = create_planting_returning_id(client)

    response = client.get(f"plantings/{planting_id}")

    assert response.status_code == HTTPStatus.OK

    response_data = response.json()

    assert response_data.get("cropName") == DEFAULT_PLANTING["cropName"]
    assert response_data.get("platedArea") == DEFAULT_PLANTING["plantedArea"]


def test_should_return_http_status_404_if_planting_not_exist(client: Client):
    response = client.get("plantings/123")

    assert response.status_code == HTTPStatus.NOT_FOUND

    response_data = response.json()

    assert response_data.get("detail") == "planting with id: 123 not founded"


def test_should_update_planting(client: Client):
    planting_id = create_planting_returning_id(client)

    payload = {"cropName": "UPDATED"}

    response = client.put(f"plantings/{planting_id}", data=dumps(payload))
    assert response.status_code == HTTPStatus.NO_CONTENT

    planting = planting_service.find_by_id(planting_id, True)
    assert planting.crop_name == payload["cropName"]
