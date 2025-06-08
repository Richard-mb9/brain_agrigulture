from dataclasses import dataclass
from datetime import date


@dataclass
class UpdateHarvestDTO:
    name: str = None
    start_date: date = None
    end_date: date = None
