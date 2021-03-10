'''
08/03/2021
Desenvolvedor: Alfredo de Morais
Objetivo: Elaborar todas as funções que são usado no arquivo
'''

import pandas as pd
import random as rand


# Caminho do arquivo nomes.txt -> OBS: Sempre verificar o path
caminho = 'C:/Users/Alfredo/github/python_projeto_controle_de_cotas_de_disco-1/versao_2/nomes.txt'

# Lista vazia para nomes
nomes = []

# Abrindo o arquivo nomes.txt e armazenando todos os nomes em uma lista
with open(caminho, 'r') as objeto_arquivo:
    arquivo = objeto_arquivo.readlines()
    for linha in arquivo:
        linha = linha.strip()
        nomes.append(linha)

# Lista de números para simular a quantidades de dados
dados = list(range(99999))


def dados_teste(nomes, dados, quantidade):
    '''
    Função que retorna a quantidade de funcionários e dados referentes ao 
    arquivo teste, Exemplo de uso da função:

    codigo:

    arquivo = dados_teste(lista, lista, int)

    o retorno da função será um arquivo txt com dados selecionados de maneira 
    randomica. 
    '''

    # Função random.choices para o nome e dados
    lista_nome = rand.sample(nomes, quantidade)
    lista_dado = rand.sample(dados, quantidade)

    # Dataframe com os dados de teste
    arquivo_dados = pd.DataFrame({
        'Nome': lista_nome,
        'Dado': lista_dado,
    })

    # Elaboração do arquivo txt para teste
    with open('dados_de_texto.txt', 'w') as arquivo_dados_de_teste:
        arquivo_dados_de_teste.write(arquivo_dados.to_string())

    # Retorno do arquivo dados de teste
    return arquivo_dados_de_teste


arquivo = dados_teste(nomes, dados, 99)
