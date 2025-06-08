from dataclasses import dataclass


@dataclass
class CreatePlantingDTO:
    property_id: int
    harvest_id: int
    planted_area: int
    crop_name: str
