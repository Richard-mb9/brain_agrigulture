from sqlalchemy import Column, Integer, Table, ForeignKey, String
from sqlalchemy.orm import relationship


from . import metadata, mapper_registry

from src.domain import Planting


plantings = Table(
    "plantings",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "property_id", Integer, ForeignKey("properties.id"), nullable=False, index=True
    ),
    Column("property_name", String, nullable=False),
    Column("harvest_id", Integer, ForeignKey("harvests.id"), nullable=False),
    Column("planted_area", Integer, nullable=False),
    Column("crop_name", String, nullable=False, index=True),
)


mapper_registry.map_imperatively(
    Planting,
    plantings,
    properties={
        "property": relationship("Property"),
        "harvest": relationship("Harvest"),
    },
)
