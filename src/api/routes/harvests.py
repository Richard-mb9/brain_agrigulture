from http import HTTPStatus
from typing import List
from fastapi import APIRouter, Depends

from src.infra import DatabaseManager
from src.api.controllers import HarvestController
from src.api.schemas import (
    DefaultCreateResponse,
    CreateHarvestRequest,
    HarvestResponse,
    UpdateHarvestRequest,
)

from src.api.routes.handlers import HttpErrorsSchemas, get_database_manager


router = APIRouter(
    prefix="/harvests",
)


@router.post(
    "",
    status_code=HTTPStatus.CREATED,
    responses=HttpErrorsSchemas().bad_request().build(),
    response_model=DefaultCreateResponse,
    description="Cadastra uma nova Safra",
)
def create(
    data: CreateHarvestRequest,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return HarvestController(db_manager=db_manager).create(data)


@router.get(
    "/{harvestId}",
    status_code=HTTPStatus.OK,
    responses=HttpErrorsSchemas().not_found("Harvest not founded").build(),
    response_model=HarvestResponse,
    description="Busca uma safra pelo id",
)
def find_by_id(
    harvestId: int,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return HarvestController(db_manager=db_manager).find_by_id(harvestId)


@router.get(
    "",
    status_code=HTTPStatus.OK,
    responses=HttpErrorsSchemas().build(),
    response_model=List[HarvestResponse],
    description="Lista todas as safras de acordo com os filtros",
)
def list_all(
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return HarvestController(db_manager=db_manager).list_all()


@router.put(
    "/{harvestId}",
    status_code=HTTPStatus.NO_CONTENT,
    responses=HttpErrorsSchemas().build(),
    description="Atualiza os dados de uma safra",
)
def update(
    harvestId: int,
    data: UpdateHarvestRequest,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    HarvestController(db_manager=db_manager).update(harvest_id=harvestId, data=data)
