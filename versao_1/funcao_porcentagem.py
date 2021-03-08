def CalculoPorcentagem(listaMegaBytes, somaMegaBytes):
  '''Função com objetivo de fazer o calculo de porcentagem por mega bytes 
  utilizado no sistema.'''

  #criando uma lista vazia para acrescentar os itens em porcentagem no loop for
  listaMegaBytesPorcentagem = []

  #função loop for para calculo de porcentagem
  for MegaBytes in listaMegaBytes:
    MegaBytesPorcentagem = ((MegaBytes/somaMegaBytes)*100)
    MegaBytesPorcentagem = round(MegaBytesPorcentagem, 2)
    MegaBytesPorcentagem = str(MegaBytesPorcentagem) + '%'
    listaMegaBytesPorcentagem.append(MegaBytesPorcentagem)
  
  #retorno da lista de porcentagem
  return listaMegaBytesPorcentagem
