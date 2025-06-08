from dataclasses import dataclass
from src.commons import UFEnum


@dataclass
class UpdatePropertyDTO:
    producer_id: int = None
    name: str = None
    city: str = None
    state: UFEnum = None
    total_areal: int = None
    agricultural_area: int = None
    area_vegetation: int = None
