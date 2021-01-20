def ListaBytes(arquivoDados):
  '''Função que recebe o arquivo e converte em lista de bytes'''

  #criando uma lista vazia
  listaBytes = []

  #separando as letras e os numeros
  for item in arquivoDados:
    item = re.findall('\d+', item)
    listaBytes.append(item)

  #retornando lista de bytes
  return listaBytes
