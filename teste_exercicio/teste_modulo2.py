import pytest
from funcao_luciano.funcaoModulo2 import Fibonacci

# Classe de teste para a atividade do modulo 02

class Teste_modulo2():
    def setup(self):
        pass

    def Teste_fibonacci(self):
        resultado = Fibonacci(0)

        assert resultado == 0


