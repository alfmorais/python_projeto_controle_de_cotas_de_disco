def CalculoMedioDados(qtdeUsuarios, listaMegaBytes):
  '''Função que recebe duas listas: quantidade total de usuarios e a quantidade 
  de dados em mega bytes, e retorna o valor médio de uso de dados em mega bytes'''

  #alterando os valores da lista em variaveis do tipo inteiros
  somaMegaBytes = sum(listaMegaBytes)
  valorUsuarios = len(qtdeUsuarios)

  #efetuando o calculo médio de dados
  dadosMedio = somaMegaBytes/valorUsuarios
  dadosMedio = round(dadosMedio, 2)
  return dadosMedio
