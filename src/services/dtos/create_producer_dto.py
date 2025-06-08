from dataclasses import dataclass
from src.commons import DocumentTypeEnum


@dataclass
class CreateProducerDTO:
    name: str
    cpf_cnpj: str
    document_type: DocumentTypeEnum
