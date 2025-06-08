from typing import List
from datetime import datetime
from dataclasses import dataclass
from src.commons import DocumentTypeEnum
from .property_response import PropertyResponse


@dataclass
class ProducerResponse:
    id: int
    name: str
    cpfCnpj: str
    documentType: DocumentTypeEnum
    createdAt: datetime
    properties: List[PropertyResponse]
