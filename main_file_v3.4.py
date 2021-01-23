import re
import pandas as pd

def DigitandoCaminho():
    '''Função que recebe o caminho do relatório e armazena em uma variavél'''

    #algoritmo principal da função
    print('Digite o caminho do arquivo:')
    caminhoArquivo = str(input())
    return caminhoArquivo

def LeituraDoArquivo(caminhoArquivo):
  '''Função para leitura do arquivo .txt e converter o mesmo em uma lista de 
  strings'''

  #abrindo uma lista vazia para armazenar o conteudo do arquivo
  conteudoArquivo = []

  #abrindo o arquivo
  arquivoInicial = open(caminhoArquivo, 'r')
  
  #algoritmo para gravar linha por linha do arquivo
  for linha in arquivoInicial:
    linha = linha.rstrip()
    conteudoArquivo.append(linha)
  
  #retornando a lista do conteudo
  return conteudoArquivo

def EliminandoEspacos(conteudoArquivo):
  '''Função para limpar os dados do arquivo'''

  #nova lista para o conteudo do arquivo
  arquivoDados = []

  #eliminando espaços em branco
  for item in conteudoArquivo:
    item = item.replace(' ', '')
    arquivoDados.append(item)
  
  #retornando uma lista sem espaços
  return arquivoDados

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

def ConversaoBytes(listaBytes):
  '''Função que recebe uma lista de valores em bytes e converte para uma lista 
  de valores em mega bytes'''

  #criando a lista vazia que será retornada como resultado da função
  listaMegaBytes = []

  #algoritmo para converção de dados em bytes para mega bytes
  for dadosBytes in listaBytes:
      for dados in dadosBytes:
          dados = int(dados)
          dados = (dados/1024) / 1024
          dados = round(dados, 2)
          listaMegaBytes.append(dados)

  #retorno da lista convertida em mega bytes
  return listaMegaBytes

def TotalMegaBytes(listaMegaBytes):
  '''somando os valores de uma lista e retornando variavel do tipo inteiro'''
  
  #variavel total de dados utilizados
  somaMegaBytes = sum(listaMegaBytes)
  return somaMegaBytes

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

def QtdeUsuarios(listaUsuarios):
  '''verificando a quantidade de items da lista e convertendo em variavel do 
  tipo inteiros'''

  #variavel quantidade total de usuarios
  valorUsuarios = len(listaUsuarios)
  return valorUsuarios

def CalculoMedioDados(somaMegaBytes, valorUsuarios):
  '''Função que recebe duas listas: quantidade total de usuarios e a quantidade 
  de dados em mega bytes, e retorna o valor médio de uso de dados em mega bytes'''

  #efetuando o calculo médio de dados
  dadosMedio = somaMegaBytes/valorUsuarios
  dadosMedio = round(dadosMedio, 2)
  
  #retornando variaveis importante do algoritmo
  return dadosMedio

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

def EscreverArquivoRelatorio(tabelaDados, somaMegaBytes, dadosMedio):
   '''Função para escrever o relatorio final do problema'''
   arquivo_final = open('relatório.txt', 'w')
   arquivo_final.write('ACME Inc.           Uso do espaço em disco pelos usuários')
   arquivo_final.write('\n')
   arquivo_final.write('-' * 70)
   arquivo_final.write('\n')
   arquivo_final.write(tabelaDados.to_string())
   arquivo_final.write('\n')
   arquivo_final.write('\n')
   arquivo_final.write('Espaço total ocupado: {:.2f} MB'.format(somaMegaBytes))
   arquivo_final.write('\n')
   arquivo_final.write('Espaço médio ocupado: {:.2f} MB'.format(dadosMedio))
   arquivo_final.close()
   
   return arquivo_final

caminhoArquivo = DigitandoCaminho()
conteudoArquivo = LeituraDoArquivo(caminhoArquivo)
arquivoDados = EliminandoEspacos(conteudoArquivo)
listaBytes = ListaBytes(arquivoDados)
listaUsuarios = ListaUsuarios(arquivoDados)
listaMegaBytes = ConversaoBytes(listaBytes)
somaMegaBytes = TotalMegaBytes(listaMegaBytes)
listaMegaBytesPorcentagem = CalculoPorcentagem(listaMegaBytes, somaMegaBytes)
valorUsuarios = QtdeUsuarios(listaUsuarios)
dadosMedio = CalculoMedioDados(somaMegaBytes, valorUsuarios)
tabelaDados = DataFrameRelatorio(listaUsuarios, listaMegaBytes, listaMegaBytesPorcentagem)
arquivo_final = EscreverArquivoRelatorio(tabelaDados, somaMegaBytes, dadosMedio)
