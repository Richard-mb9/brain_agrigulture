from pydantic import BaseModel, model_validator
from src.commons import UFEnum
from src.commons.errors import BadRequestError


class CreatePropertyRequest(BaseModel):
    producerId: int
    name: str
    city: str
    state: UFEnum
    totalArea: int
    agriculturalArea: int
    areaVegetation: int

    @model_validator(mode="after")
    def validate_area(self):
        if self.__area_is_valid() is False:
            raise BadRequestError(
                "The area of vegetation and the agricultural area combined cannot be greater than the total area."
            )

        return self

    def __area_is_valid(self):
        return self.agriculturalArea + self.areaVegetation <= self.totalArea
