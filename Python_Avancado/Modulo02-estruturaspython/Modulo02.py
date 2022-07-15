from funcaomodulo02.funcaoModulo2 import Fibonacci

#class para sequencia de fibonacci
class Fibonaccii:
    def __init__(self, numero):
        self.numero = numero

    # Metodo para executar a sequencia de fibonacci
    def Sequencia(self):
        return Fibonacci(self.numero)



#####################################################
#Input para a entrada do usúario !!!
numero = int(input('Digite um numero? '))

#Estanciando a class Fibonacci
fibona = Fibonaccii(numero)

# Usando o Dict com prehension
resultado = {j : numero for j, numero in enumerate(str(fibona.Sequencia()))}
print(resultado)