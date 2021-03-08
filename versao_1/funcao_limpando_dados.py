def ElimandoEspacos(conteudoArquivo):
  '''Função para limpar os dados do arquivo'''

  #nova lista para o conteudo do arquivo
  arquivoDados = []

  #eliminando espaços em branco
  for item in conteudoArquivo:
    item = item.replace(' ', '')
    arquivoDados.append(item)
  
  #retornando uma lista sem espaços
  return arquivoDados
