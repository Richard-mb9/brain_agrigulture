from pydantic import BaseModel
from src.commons import DocumentTypeEnum


class UpdateProducerRequest(BaseModel):
    name: str = None
    cpfCnpj: str = None
    documentType: DocumentTypeEnum = None
