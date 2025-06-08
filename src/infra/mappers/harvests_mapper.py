from sqlalchemy import Column, Integer, Table, String, Date
from . import metadata, mapper_registry

from src.domain import Harvest

harvests = Table(
    "harvests",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, index=True),
    Column("start_date", Date, nullable=True, index=True),
    Column("end_date", Date, nullable=True, index=True),
)


mapper_registry.map_imperatively(Harvest, harvests)
