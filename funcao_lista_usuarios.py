def ListaUsuarios(arquivoDados):
  '''Função que recebe o arquivo e converte em lista de usuario'''

  #criando uma lista vazia
  listaUsuarios = []

  #separando as letras e os numeros
  for item in arquivoDados:
    item = re.split('\d+',item)
    for userList in item:
      del(item[-1:])
      listaUsuarios.append(userList)

  return listaUsuarios
