from validate_docbr import CPF, CNPJ
from pydantic import BaseModel, model_validator
from src.commons import DocumentTypeEnum
from src.commons.errors import BadRequestError


class CreateProducerRequest(BaseModel):
    name: str
    cpfCnpj: str
    documentType: DocumentTypeEnum

    @model_validator(mode="after")
    def validate_document(self):
        if (
            self.documentType == DocumentTypeEnum.CPF
            and len(self.cpfCnpj) == 11
            and CPF().validate(self.cpfCnpj)
        ):
            return self
        elif (
            self.documentType == DocumentTypeEnum.CNPJ
            and len(self.cpfCnpj) == 14
            and CNPJ().validate(self.cpfCnpj)
        ):
            return self
        else:
            raise BadRequestError("Invalid Document")
