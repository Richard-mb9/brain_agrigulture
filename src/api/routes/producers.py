from http import HTTPStatus
from typing import List
from fastapi import APIRouter, Depends

from src.infra import DatabaseManager
from src.api.controllers import ProducerController
from src.api.schemas import (
    DefaultCreateResponse,
    CreateProducerRequest,
    ProducerResponse,
    UpdateProducerRequest,
)

from src.api.routes.handlers import HttpErrorsSchemas, get_database_manager


router = APIRouter(
    prefix="/producers",
)


@router.post(
    "",
    status_code=HTTPStatus.CREATED,
    responses=HttpErrorsSchemas().bad_request().build(),
    response_model=DefaultCreateResponse,
    description="Cadastra um novo produtor",
)
def create(
    data: CreateProducerRequest,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return ProducerController(db_manager=db_manager).create(data)


@router.get(
    "/{producerId}",
    status_code=HTTPStatus.OK,
    responses=HttpErrorsSchemas().not_found("Producer not found").build(),
    response_model=ProducerResponse,
    description="Busca um produtor pelo id",
)
def find_by_id(
    producerId: int,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return ProducerController(db_manager=db_manager).find_by_id(producerId)


@router.get(
    "",
    status_code=HTTPStatus.OK,
    response_model=List[ProducerResponse],
    description="Lista todos os produtores de acordo com os filtros",
)
def list_all(
    cpfCnpj: str = None, db_manager: DatabaseManager = Depends(get_database_manager)
):
    return ProducerController(db_manager=db_manager).list_all(cpf_cnpj=cpfCnpj)


@router.put(
    "/{producerId}",
    status_code=HTTPStatus.NO_CONTENT,
    responses=HttpErrorsSchemas()
    .bad_request()
    .not_found("Producer not founded")
    .build(),
    description="Atualiza os dados de um determinado produtor",
)
def update(
    producerId: int,
    data: UpdateProducerRequest,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return ProducerController(db_manager=db_manager).update(
        producer_id=producerId, data=data
    )


@router.delete(
    "/{producerId}",
    status_code=HTTPStatus.NO_CONTENT,
    responses=HttpErrorsSchemas().build(),
    description="Exclui um determinado produtor",
)
def delete(
    producerId: int,
    db_manager: DatabaseManager = Depends(get_database_manager),
):
    return ProducerController(db_manager=db_manager).delete(producer_id=producerId)
