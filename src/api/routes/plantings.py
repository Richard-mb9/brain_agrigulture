from http import HTTPStatus
from typing import List
from fastapi import APIRouter, Depends

from src.infra import DatabaseManager
from src.api.controllers import PlantingController
from src.api.schemas import (
    DefaultCreateResponse,
    CreatePlantingRequest,
    PlantingResponse,
    UpdatePlantingRequest,
)

from src.api.routes.handlers import HttpErrorsSchemas, get_database_manager


router = APIRouter(
    prefix="/plantings",
)


@router.post(
    "",
    status_code=HTTPStatus.CREATED,
    responses=HttpErrorsSchemas().bad_request().build(),
    response_model=DefaultCreateResponse,
    description="Cadastra uma nova plantação",
)
def create(
    data: CreatePlantingRequest,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return PlantingController(db_manager=db_manager).create(data)


@router.get(
    "/{plantingId}",
    status_code=HTTPStatus.OK,
    responses=HttpErrorsSchemas().not_found("Planting not founded").build(),
    response_model=PlantingResponse,
    description="busca uma plantação pelo id",
)
def find_by_id(
    plantingId: int,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return PlantingController(db_manager=db_manager).find_by_id(plantingId)


@router.get(
    "",
    status_code=HTTPStatus.OK,
    responses=HttpErrorsSchemas().not_found("Planting not founded").build(),
    response_model=List[PlantingResponse],
    description="lista todas as plantações de acordo com os filtros",
)
def list_all(
    cropName: str = None,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return PlantingController(db_manager=db_manager).list_all(crop_name=cropName)


@router.put(
    "/{plantingId}",
    status_code=HTTPStatus.NO_CONTENT,
    responses=HttpErrorsSchemas()
    .not_found("Planting not founded")
    .bad_request()
    .build(),
    description="Atualiza os dados de uma plantação",
)
def update(
    plantingId: int,
    data: UpdatePlantingRequest,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    PlantingController(db_manager=db_manager).update(planting_id=plantingId, data=data)
