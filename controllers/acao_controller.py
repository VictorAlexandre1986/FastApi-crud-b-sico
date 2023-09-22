from fastapi import APIRouter, Response

from dto.acao import AcaoDTO
from model.acao import Acao
from model.requests.patch_papel import PapelUpdate


import ormar

router = APIRouter()


@router.post('/')
async def add_acao(acao: Acao):
    validado = AcaoDTO(acao)
    await validado.save()
    return acao


@router.get('/')
async def list_acao():
    return await Acao.objects.all()

@router.get('/{acao_id}')
async def get_acao(acao_id : int, response: Response):
    try:
        acao = await Acao.objects.get(id=acao_id)
        return acao
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return{"mensagem":"Entidade não encontrada"}
    
    
@router.patch('/{acao_id}')
async def patch_acao(propriedades_atualizacao: PapelUpdate, acao_id: int, response: Response):
    try:
        acao_salvo = await Acao.objects.get(id=acao_id)
        #exclude = exclua o que nao tiver selecionado, ficou vago mas foi o que foi dito 
        propriedades_atualizadas = propriedades_atualizacao.dict(exclude_unset=True)
        await acao_salvo.update(**propriedades_atualizadas)
        return acao_salvo
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return{"mensagem":"Entidade não encontrada"}
    
    
    
@router.delete('/{papel_id}')
async def delete_acao(acao_id: int, response: Response):
    try:
        acao = await Acao.objects.get(id=acao_id)
        return await acao.delete()
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return{'mensagem':'Entidade não encontrada'}
    