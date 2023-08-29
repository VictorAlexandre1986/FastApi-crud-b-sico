from fastapi import APIRouter

from models.acao import Acao


router = APIRouter()

banco_de_dados = []

@router.post('/')
def add_acao(acao: Acao):
    banco_de_dados.append(acao)
    return acao


@router.get('/')
def list_acao():
    return banco_de_dados