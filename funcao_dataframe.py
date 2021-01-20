def DataFrameRelatorio(listaUsuarios, listaMegaBytes, listaMegaBytesPorcentagem):

  '''Função que converte dados em tabela'''

  #usando o pandas vamos utilizar a função para converter em tabela
  tabelaDados = pd.DataFrame({
      "Usuário": listaUsuarios,
      "Espaço Utilizado": listaMegaBytes,
      "% de Uso": listaMegaBytesPorcentagem,
     })
  
  #retornando dataframe
  return tabelaDados
