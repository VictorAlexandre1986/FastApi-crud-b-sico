from pydantic import BaseModel

class Acao(BaseModel):
    id: int
    nome: str
    sigla: str
    cnpj: str 