# importando bibliotecas do FASTAPI

from fastapi import FastAPI
from pydantic import BaseModel


# Criando a API 
app = FastAPI()

#iniciando a API com get !!!!

@app.get("/")
async def root():
    return {"Message" : "Api conectada"}  #menssagem para para monstra que ele esta conctada

# Classe para determina o que tera no arquivo json!!!!
class Resp(BaseModel):

    # valor para serem colocado no json para fazer a aoperação
    valor1 : int
    valor2 : int
    Operador : str

# Método POST da API 

@app.post("/operacao")
async def operacao(resultado: Resp ):

    #usando os if e elif para fazer a conparação para saber qual operado o usuario digitou!!!

    if resultado.operador == '+':
        resultado = resultado.valor1 + resultado.valor2
        return resultado

    elif resultado.operador == '-':
        resultado = resultado.valor1 - resultado.valor2
        return resultado

    elif resultado.operador == '/':
        resultado = resultado.valor1 / resultado.valor2
        return resultado

    elif resultado.operador == '*':
        resultado = resultado.valor1 * resultado.valor2
        return resultado

    else:
        return 'Operador não encontrado'