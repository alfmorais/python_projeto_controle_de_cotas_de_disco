def LeituraDoArquivo(caminhoArquivo):
  '''Função para leitura do arquivo .txt e converter o mesmo em uma lista de 
  strings'''

  #abrindo uma lista vazia para armazenar o conteudo do arquivo
  conteudoArquivo = []

  #abrindo o arquivo
  arquivoInicial = open(caminho, 'r')
  
  #algoritmo para gravar linha por linha do arquivo
  for linha in arquivoInicial:
    linha = linha.rstrip()
    conteudoArquivo.append(linha)
  
  #retornando a lista do conteudo
  return conteudoArquivo
