from dataclasses import dataclass


@dataclass
class UpdatePlantingDTO:
    harvest_id: int = None  # colher
    planted_area: int = None  # area plantada
    crop_name: str = None
