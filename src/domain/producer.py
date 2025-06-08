from typing import List, TYPE_CHECKING
from datetime import datetime
from src.commons import DocumentTypeEnum

if TYPE_CHECKING:  # pragma: no cover
    from .property import Property


class Producer:
    id: int
    cpf_cnpj: str
    properties: List["Property"]

    def __init__(self, name: str, cpf_cnpj: str, document_type: DocumentTypeEnum):
        self.name = name
        self.cpf_cnpj = cpf_cnpj
        self.document_type = document_type
        self.created_at = datetime.now()
