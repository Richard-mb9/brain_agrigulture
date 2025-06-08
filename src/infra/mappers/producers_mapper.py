from sqlalchemy import Column, Integer, Table, String, Enum, DateTime
from sqlalchemy.orm import relationship

from . import metadata, mapper_registry

from src.commons import DocumentTypeEnum
from src.domain import Producer

producers = Table(
    "producers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("cpf_cnpj", String, nullable=False, unique=True, index=True),
    Column("document_type", Enum(DocumentTypeEnum), nullable=False),
    Column("created_at", DateTime, nullable=False),
)


mapper_registry.map_imperatively(
    Producer,
    producers,
    properties={
        "properties": relationship(
            "Property",
            back_populates="producer",
            cascade="all, delete-orphan",
        )
    },
)
