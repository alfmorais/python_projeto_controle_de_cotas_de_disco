import pandas as pd
import re

#abrindo o arquivo txt para efetuar o teste
caminho = 'D:\\00. PYTHON_PROJECTS\\04_PROJETO_PYTHON_COTAS//usuarios.txt'
arquivo = open(caminho, 'r')

#lendo os dados do arquivo e armazenando em uma lista
lista_arquivo = []

for linha in arquivo:
  linha = linha.rstrip()
  lista_arquivo.append(linha)

#fechando o arquivo que foi aberto
arquivo.close()

#limpando espaços vazios na lista
nova_lista_arquivo = []

for item in lista_arquivo:
  item = item.replace(' ', '')
  nova_lista_arquivo.append(item)

#separando os dados em duas lista: usuarios e numeros
lista_numeros = []
lista_usuario = []

#separando os dados da lista usuarios e eliminando listas vazias
for item in nova_lista_arquivo:
  item = re.split('\d+',item)
  lista_usuario.append(item)
for item in lista_usuario:
  del(item[-1:])

#separando os dados da lista de numeros
for item in nova_lista_arquivo:
  item = re.findall('\d+', item)
  lista_numeros.append(item)

#limpandos e tratando os dados para deixar conforme solicitado no projeto
lista_numeros_2 = []
lista_porcentag = []

#laço responsavel por pegar o item da lista numero, que está em bytes converter p/ megabytes
#após a conversao é utilizado um método de arredondamento para duas casas decimais
for lista in lista_numeros:
  for i in lista:
    i = float(i)
    i = (i / 1024) / 1024
    i = round(i, 2)
    lista_numeros_2.append(i)

#somado a quantidade total de bytes para calculo de porcentagem e valor total
soma_lista = float(sum(lista_numeros_2))
soma_lista = round(soma_lista, 2)

#calculo de porcentagem, item por item
for num in lista_numeros_2:
  porcentagem = ((num/soma_lista))*100
  porcentagem = round(porcentagem, 2)
  porcentagem = str(porcentagem) + '%'
  lista_porcentag.append(porcentagem)

#conversao da lista de números em strings para facilitar o entedimento
lista_numeros_3 =[]
for i in lista_numeros_2:
  i = str(i) + ' MB'
  lista_numeros_3.append(i)

#alterando a lista dos usuarios
lista_usuario_2 = []
for lista in lista_usuario:
  for i in lista:
    lista_usuario_2.append(i)

#criando o dataframe com os dados que foram gerados
tabela = pd.DataFrame({
    "Nome_Usuarios": lista_usuario_2,
    "Dados_Usuario": lista_numeros_3,
    "%_de_uso_dado": lista_porcentag,
     })

#Calculando o valor médio utilizado
qtde_usuarios = len(lista_usuario_2)
medio_ocupado = soma_lista / qtde_usuarios

#abrindo e escrevendo o arquivo relatorio
caminho = 'D:\\00. PYTHON_PROJECTS\\04_PROJETO_PYTHON_COTAS//'
arquivo_final = open((caminho + 'relatório.txt'), 'w') 
arquivo_final.write('ACME Inc.           Uso do espaço em disco pelos usuários')
arquivo_final.write('\n')
arquivo_final.write('-' * 70)
arquivo_final.write('\n')
arquivo_final.write(tabela.to_string())
arquivo_final.write('\n')
arquivo_final.write('\n')
arquivo_final.write('Espaço total ocupado: {:.2f} MB'.format(soma_lista))
arquivo_final.write('\n')
arquivo_final.write('Espaço médio ocupado: {:.2f} MB'.format(medio_ocupado))
arquivo_final.close()
print(arquivo_final)
