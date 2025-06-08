from dataclasses import dataclass
from datetime import date


@dataclass
class HarvestResponse:
    id: int
    name: str
    startDate: date
    endDate: date
