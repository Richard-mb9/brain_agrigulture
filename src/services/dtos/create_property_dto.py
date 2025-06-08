from dataclasses import dataclass

from src.commons import UFEnum


@dataclass
class CreatePropertyDTO:
    producer_id: int
    name: str
    city: str
    state: UFEnum
    total_area: int
    agricultural_area: int
    area_vegetation: int
