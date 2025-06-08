from dataclasses import dataclass
from src.commons import UFEnum


@dataclass
class UpdatePropertyRequest:
    producerId: int = None
    name: str = None
    city: str = None
    state: UFEnum = None
    totalAreal: int = None
    agriculturalArea: int = None
    areaVegetation: int = None
