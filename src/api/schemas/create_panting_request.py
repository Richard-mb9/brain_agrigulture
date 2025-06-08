from pydantic import BaseModel


class CreatePlantingRequest(BaseModel):
    propertyId: int
    harvestId: int
    plantedArea: int
    cropName: str
