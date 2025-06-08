from dataclasses import dataclass
from src.commons import UFEnum


@dataclass
class PropertyResponse:
    id: int
    producerId: int
    name: str
    city: str
    state: UFEnum
    totalArea: int
    agriculturalArea: int
    areaVegetation: int
