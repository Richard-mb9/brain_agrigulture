from dataclasses import dataclass
from datetime import date


@dataclass
class CreateHarvestDTO:
    name: str
    start_date: date = None
    end_date: date = None
