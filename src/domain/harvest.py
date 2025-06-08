from datetime import date


class Harvest:
    id: int

    def __init__(self, name: str, start_date: date, end_date: date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
