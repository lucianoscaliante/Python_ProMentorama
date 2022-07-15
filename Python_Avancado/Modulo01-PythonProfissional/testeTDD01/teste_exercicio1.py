import pytest
from funcaomodulo01.calculadora import soma


class TesteExercicio:
    def Setup(self):
        pass

    def test_soma(self):
        resultado = soma(2, 3)
        resultado2 = soma(5, 8)

        assert resultado == 5
        assert resultado2 > 10
