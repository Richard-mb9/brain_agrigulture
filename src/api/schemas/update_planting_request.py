from pydantic import BaseModel


class UpdatePlantingRequest(BaseModel):
    harvestId: int = None
    plantedArea: int = None
    cropName: str = None
