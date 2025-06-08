from typing import List, TYPE_CHECKING


if TYPE_CHECKING:  # pragma: no cover
    from .producer import Producer
    from src.commons import UFEnum


class Property:
    id: int
    producer: List["Producer"]

    def __init__(
        self,
        producer_id: int,
        name: str,
        city: str,
        state: "UFEnum",
        total_area: int,
        agricultural_area: int,
        area_vegetation: int,
    ):
        self.producer_id = producer_id
        self.name = name
        self.city = city
        self.state = state
        self.total_area = total_area
        self.agricultural_area = agricultural_area
        self.area_vegetation = area_vegetation

    def area_is_valid(self):
        return self.agricultural_area + self.area_vegetation <= self.total_area
