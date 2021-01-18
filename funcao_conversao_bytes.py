def ConversaoBytes(listaBytes):
  '''Função que recebe um valor em bytes e converte para mega bytes'''

  #criando a lista vazia que será retornada como resultado da função
  listaMegaBytes = []

  #algoritmo para converção de dados em bytes para mega bytes
  for dadosBytes in listaBytes:
    dadosBytes = int(dadosBytes)
    dadosBytes = (dadosBytes/1024) / 1024
    dadosBytes = round(dadosBytes, 2)
    listaMegaBytes.append(dadosBytes)
  
  #retorno da lista convertida em mega bytes
  return listaMegaBytes
