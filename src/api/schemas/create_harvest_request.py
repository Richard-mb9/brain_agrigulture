from datetime import date
from pydantic import BaseModel, Field, model_validator
from src.commons.errors import BadRequestError


class CreateHarvestRequest(BaseModel):
    name: str
    startDate: date = Field(
        default=None,
        description="Date format: YYYY-MM-DD, example: 2025-06-30",
    )
    endDate: date = Field(
        default=None,
        description="Date format: YYYY-MM-DD, example: 2025-06-30",
    )

    @model_validator(mode="after")
    def validate_document(self):
        if self.startDate is not None and self.endDate is not None:
            if self.endDate < self.startDate:
                raise BadRequestError(
                    "the end date cannot be greater than the start date"
                )
        return self
