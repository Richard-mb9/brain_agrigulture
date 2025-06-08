from typing import TYPE_CHECKING


if TYPE_CHECKING:  # pragma: no cover
    from .harvest import Harvest
    from .property import Property


class Planting:
    id: int
    crop_name: str
    property: "Property"
    harvest: "Harvest"

    def __init__(
        self,
        property_id: int,
        property_name: str,
        harvest_id: int,  # colher
        planted_area: int,  # area plantada
        crop_name: str,  # cultura
    ):
        self.property_id = property_id
        self.property_name = property_name
        self.harvest_id = harvest_id
        self.planted_area = planted_area
        self.crop_name = crop_name
