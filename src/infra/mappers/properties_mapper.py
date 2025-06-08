from sqlalchemy import Column, Integer, Table, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from . import metadata, mapper_registry

from src.commons import UFEnum
from src.domain import Property


properties = Table(
    "properties",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("producer_id", Integer, ForeignKey("producers.id"), nullable=False),
    Column("city", String, nullable=False),
    Column("state", Enum(UFEnum), nullable=False),
    Column("total_area", Integer, nullable=False),
    Column("agricultural_area", Integer, nullable=False),
    Column("area_vegetation", Integer, nullable=False),
)


mapper_registry.map_imperatively(
    Property,
    properties,
    properties={"producer": relationship("Producer", back_populates="properties")},
)
