from pytest import fixture

from tests.fixtures.fake_repositories import (
    fake_harvest_repository,
    fake_planting_repository,
    fake_producer_repository,
    fake_property_repository,
)


@fixture(scope="function", autouse=True)
def clear_all_tables():
    fake_property_repository.data = []
    fake_harvest_repository.data = []
    fake_planting_repository.data = []
    fake_producer_repository.producers = []
