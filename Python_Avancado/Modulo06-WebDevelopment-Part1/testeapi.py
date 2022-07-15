# importando as bibliotecas para realizaçoes dos teste 

import pytest
from requests import get, post
from json import loads


class Testapi:
    def setup(self): # construtor da classe
        self.url = "http://127.0.0.1:8000"

    # Metodo para saber se a api esta respondendo
    def Apistatus(self):
        resp = get(self.url)
        assert resp.ok

    #testando resposta da api 
    def testeResp(self):
        resposta = get(self.url)
        message = loads(resposta.text)
        assert message["Message"] == "Api conectada"

    #testando o metodo post da api
    def TestePost(self):
        resposta = post(self.url + "/operacao"
                    , json = {"valor1" : 2, "valor2" : 2, "operador" : "+"})

    #estou deixando o teste do pos meio vago pq eu não consegui realizalo

    
        