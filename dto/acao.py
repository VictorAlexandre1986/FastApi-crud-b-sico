from pydantic import BaseModel,validator
import re

class AcaoDTO(BaseModel):
    id: int
    nome: str
    sigla: str
    cnpj: str 
    
    @validator('sigla')
    def valida_formatacao_sigla(cls,valor):
        regex = r"^[A-Z]{4}[0-9]{2}$"
        validacao = re.match(regex, valor)
        # validacao = re.search(regex, valor)
        if validacao:
            # return validacao.group(0)
            return valor
        else:
            raise ValueError('A sigla do papel é inválida')