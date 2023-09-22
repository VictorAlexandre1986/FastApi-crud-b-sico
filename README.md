# FastApi crud básico

## Tecnologias utilizadas

<ul>
  <li>Python</li>
  <li>FastApi</li>
  <li>Pydantic</li>
  <li>SQLAlchemy</li>
  <li>ORMAR</li>
  <li>SQLite</li>
</ul>

## Para rodar o app

Primeiro é necessário criar um ambiente virtual com:
```
python -m venv venv
```

Depois acessar o ambiente virtual
```
.\venv\Scripts\activate
```

Depois instalar as dependencias:
```
pip install -r requirements.txt
```

Para executar o servidor digite:
```
uvicorn main:app
```
Acesse o endereco que foi disponibilizado e digite /docs no final para acessar o swagger e testar os endpoints:
http://127.0.0.1:8000/docs#/
