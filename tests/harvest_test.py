from json import dumps
from http import HTTPStatus


from src.services import HarvestService
from tests.fixtures.fake_repositories import FakeRepositoriesManager
from tests.fixtures.app import Client


harvest_service = HarvestService(FakeRepositoriesManager())

DEFAULT_HARVEST = {
    "name": "Safra de 2021",
    "startDate": "2021-01-01",
    "endDate": "2021-10-30",
}


def create_harvest_returning_id(client: Client):
    response = client.post("harvests", data=dumps(DEFAULT_HARVEST))
    response_data = response.json()
    return response_data["id"]


def test_should_create_harvest(client: Client):
    response = client.post("harvests", data=dumps(DEFAULT_HARVEST))
    assert response.status_code == HTTPStatus.CREATED

    response_data = response.json()
    assert response_data.get("id") is not None


def test_should_list_all_harvests(client: Client):
    assert len(harvest_service.list_all()) == 0

    for _ in range(0, 5):
        create_harvest_returning_id(client)

    response = client.get("harvests")
    assert response.status_code == HTTPStatus.OK

    response_data = response.json()
    assert len(response_data) == 5


def test_should_find_harvest_by_id(client: Client):
    harvest_id = create_harvest_returning_id(client)

    response = client.get(f"harvests/{harvest_id}")
    assert response.status_code == HTTPStatus.OK

    response_data = response.json()
    assert response_data.get("name") == DEFAULT_HARVEST["name"]


def test_should_return_http_status_404_if_harvest_not_exist(client: Client):
    response = client.get("harvests/123")
    assert response.status_code == HTTPStatus.NOT_FOUND

    response_data = response.json()
    assert response_data.get("detail") == "harvest with id: 123 not founded"


def test_should_update_harvest(client: Client):
    harvest_id = create_harvest_returning_id(client)
    payload = {"name": "updated"}

    response = client.put(f"harvests/{harvest_id}", data=dumps(payload))
    assert response.status_code == HTTPStatus.NO_CONTENT

    harvest = harvest_service.find_by_id(harvest_id, True)
    assert harvest.name == payload["name"]
