from http import HTTPStatus
from typing import List
from fastapi import APIRouter, Depends

from src.infra import DatabaseManager
from src.api.controllers import PropertyController
from src.api.schemas import (
    DefaultCreateResponse,
    CreatePropertyRequest,
    UpdatePropertyRequest,
    PropertyResponse,
)

from src.api.routes.handlers import HttpErrorsSchemas, get_database_manager


router = APIRouter(
    prefix="/properties",
)


@router.post(
    "",
    status_code=HTTPStatus.CREATED,
    responses=HttpErrorsSchemas().bad_request().build(),
    response_model=DefaultCreateResponse,
    description="Cadastra uma nova propriedade",
)
def create(
    data: CreatePropertyRequest,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return PropertyController(db_manager=db_manager).create(data)


@router.get(
    "/{propertyId}",
    status_code=HTTPStatus.OK,
    responses=HttpErrorsSchemas().not_found("Property not found").build(),
    response_model=PropertyResponse,
    description="Busca uma propriedade pelo id",
)
def find_by_id(
    propertyId: int,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return PropertyController(db_manager=db_manager).find_by_id(propertyId)


@router.get(
    "/producer/{producerId}",
    status_code=HTTPStatus.OK,
    response_model=List[PropertyResponse],
    description="Lista as propriedades de um produtor",
)
def find_by_producer_id(
    producerId: int, db_manager: DatabaseManager = Depends(get_database_manager)
):
    return PropertyController(db_manager=db_manager).find_by_producer_id(
        producer_id=producerId
    )


@router.get(
    "",
    status_code=HTTPStatus.OK,
    response_model=List[PropertyResponse],
    description="Lista todas as propriedades de acordo com os filtros",
)
def list_all(db_manager: DatabaseManager = Depends(get_database_manager)):
    return PropertyController(db_manager=db_manager).list_all()


@router.put(
    "/{propertyId}",
    status_code=HTTPStatus.NO_CONTENT,
    responses=HttpErrorsSchemas()
    .bad_request()
    .not_found("property not founded")
    .build(),
    description="Atualiza os dados de uma propriedade",
)
def update(
    propertyId: int,
    data: UpdatePropertyRequest,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return PropertyController(db_manager=db_manager).update(
        property_id=propertyId, data=data
    )


@router.delete(
    "/{propertyId}",
    status_code=HTTPStatus.NO_CONTENT,
    description="Exclui um determinada propriedade",
)
def delete(
    producerId: int,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return PropertyController(db_manager=db_manager).delete(property_id=producerId)
