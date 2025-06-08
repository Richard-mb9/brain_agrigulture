from dataclasses import dataclass


@dataclass
class PlantingResponse:
    id: int
    propertyId: int
    propertyName: str
    harvestId: int
    platedArea: int
    cropName: str
