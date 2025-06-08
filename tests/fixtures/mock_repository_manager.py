from pytest import fixture
from mockito import when, unstub


from src.infra.repositories.repositories_manager import RepositoryManager
from tests.fixtures.fake_repositories import (
    fake_harvest_repository,
    fake_planting_repository,
    fake_producer_repository,
    fake_property_repository,
)


@fixture(scope="function", autouse=True)
def mock_repository_manager():
    when(RepositoryManager).producer_repository(...).thenReturn(
        fake_producer_repository
    )
    when(RepositoryManager).property_repository(...).thenReturn(
        fake_property_repository
    )
    when(RepositoryManager).planting_repository(...).thenReturn(
        fake_planting_repository
    )
    when(RepositoryManager).harvest_repository(...).thenReturn(fake_harvest_repository)

    yield
    unstub()
