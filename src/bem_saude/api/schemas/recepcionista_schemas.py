"""
Schemas Pydantinc para Recepcionista.

Define os DTOs (Data Tranfer Objects) para requisicoes e respostas relacionadas a recepcionistas.
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from bem_saude.dominio.enums.status_cadastro import StatusCadastro

class RecepcionistaCriarRequest(BaseModel):

    """
    Schma para criacao de recepcionista

    nome é obrigatorio

    Status padrao é ATIVO se não informado.

    Validacoes:
    - nome: minimo 3 caracteres, maximo 45 caracteres
    """

    nome: str = Field(
        ...,
        min_length=3,
        max_length=255,
        description="Nome completo do recepcionista",
        examples=["Mario dos Santos"]
    )
    status: StatusCadastro = Field(
        default=StatusCadastro.ATIVO,
        description="Status do cadastro",
        examples=["ATIVO"]
    )
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "nome": "Mario dos Santos",
                "status": "ATIVO"
            }
            ]
        }
    }

class RecepcionistaResponse(BaseModel):
    """
    Schma de resposta de recepcionista

    Retorna todos os dados do recepcionista, incluindo campos de auditoria.
    """
    id: UUID = Field(
        ..., # Campo obrigatorio e nao tem valor padrao
        description="ID do recepcionista",
        examples=["019c4506-d794-77eb-91c2-92c4bf3408a9"]
    )
    nome: str = Field(
        ..., # Campo obrigatorio e nao tem valor padrao
        description="Nome completo do recepcionista",
        examples=["Mario dos Santos"]
    )
    status: StatusCadastro = Field(
        ...,
        description="Status do cadastro",
        examples=["ATIVO"]
    )
    criado_em: datetime = Field(
        ...,
        description="Data e hora de criação do registro",
        examples=["2024-01-30T10:30:30"]
    )
    alterado_em: datetime | None = Field(
        None,
        description="Data e hora da ultima alteracao do registro",
        examples=["2024-01-30T11:45:00"]
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Mario dos Santos",
                    "status": "ATIVO"
                }
            ]
        }
    }

class RecepcionistaAlterarRequest(BaseModel):

    """
    Schma para criacao de recepcionista

    nome é obrigatorio

   
    Validacoes:
    - nome: minimo 3 caracteres, maximo 45 caracteres
    """

nome: str = Field(
    ...,
    min_length=3,
    max_length=255,
    description="Nome completo do recepcionista",
    examples=["Mario dos Santos"]
)

model_config = {
    "json_schema_extra": {
        "examples": [
            {
            "nome": "Mario dos Santos",
            
        }
        ]
    }
}