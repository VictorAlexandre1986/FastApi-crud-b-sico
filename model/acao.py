import ormar
from config import database, metadata
from pydantic import validator
import re

class Acao(ormar.Model):
    class Meta:
        metadata = metadata
        database =  database
        tablename = 'acoes'
        
        
    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    sigla: str = ormar.String(max_length=10)
    cnpj: str = ormar.String(max_length=20)
    
    

        
 
        