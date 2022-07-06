
# Função para saber se o numero inserido pelo usuário e Multiplo ou não
def Multiplo(num):
    #IF para saber se multiplo de 5 e 7
    if ((num % 5 == 0) and (num % 7 == 0)):
        print('FizzBuzz')

    #ELIF para saber se o número e multiplo de 5
    elif (num % 5 == 0):
        print('Fizz')

    #ELIF para saber se o número e multiplo de 7
    elif (num % 7 == 0):
        print('Buzz')

    #ELSE se o número não for multiplo nem de 45 e nem de 7!!
    else:
        print('Miss')
