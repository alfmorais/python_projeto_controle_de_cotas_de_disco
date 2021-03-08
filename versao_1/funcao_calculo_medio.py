def TotalMegaBytes(listaMegaBytes):
  '''somando os valores de uma lista e retornando variavel do tipo inteiro'''
  
  #variavel total de dados utilizados
  somaMegaBytes = sum(listaMegaBytes)
  return somaMegaBytes

def QtdeUsuarios(qtdeUsuarios):
  '''verificando a quantidade de items da lista e convertendo em variavel do 
  tipo inteiros'''

  #variavel quantidade total de usuarios
  valorUsuarios = len(qtdeUsuarios)
  return valorUsuarios

def CalculoMedioDados(somaMegaBytes, valorUsuarios):
  '''Função que recebe duas listas: quantidade total de usuarios e a quantidade 
  de dados em mega bytes, e retorna o valor médio de uso de dados em mega bytes'''

  #efetuando o calculo médio de dados
  dadosMedio = somaMegaBytes/valorUsuarios
  dadosMedio = round(dadosMedio, 2)
  
  #retornando variaveis importante do algoritmo
  return dadosMedio

lista = [434.99, 1187.99, 117.74, 87.03, 0.94, 752.88]
usuar = ['alexandre', 'anderson', 'antonio', 'carlos', 'cesar', 'rosemary']

somaMegaBytes = TotalMegaBytes(lista)
valorUsuarios = QtdeUsuarios(usuar)

CalculoMedioDados(somaMegaBytes, valorUsuarios)
