from dataclasses import dataclass
from src.commons import DocumentTypeEnum


@dataclass
class UpdateProducerDTO:
    name: str = None
    cpf_cnpj: str = None
    document_type: DocumentTypeEnum = None
