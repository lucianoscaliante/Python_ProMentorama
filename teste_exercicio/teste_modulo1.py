from funcao_luciano.funcaoModulo1 import Multiplo

#classe criada para fazer teste unitario do modulo01
class TesteModulo01:
    def Setup(self):
        pass

    # Fução para executar o teste  
    def test_multiplo(self):
        resultado = Multiplo(0)

        assert resultado
