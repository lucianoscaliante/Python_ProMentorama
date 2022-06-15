# Função para calcular Fibonacci do numero que passado pelo o Usuario!!!!
def Fibonacci(numero):
  #lista criada para aprezentar a Fibonacci
  lista = [0,1]

  #condição de o usúario inserir  0  como dados no teclado
  if numero == 0:
      print("Zero não tem sequência de Fibonacci!!")
  elif numero == 1:
      print('0')
  elif numero == 2:
      print('[0,','1]')
  else:
    while(len(lista) < numero):
        lista.append(0)
    if(numero == 0 or numero == 1):
        return 1
    else:
        lista[0]=0
        lista[1]=1
        for i in range(2, numero):
          lista[i] = lista[i-1] + lista[i-2]
        print(lista)
