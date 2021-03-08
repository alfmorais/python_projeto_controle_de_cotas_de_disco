'''
08/03/2021

Desenvolvedor: Alfredo de Morais
Objetivo: Elaborar todas as funções que são usado no arquivo

'''

import pandas as pd

caminho = 'C:/Users/Alfredo/AppData/Local/Programs/Python/Python39/python_projeto_controle_de_cotas_de_disco/versao_2/nomes.txt'

lista_nomes = []

with open(caminho, 'r') as arquivo:
    print(arquivo.read())
    '''
    for linha in arquivo_aberto:
        linha = linha.rstrip()
        lista_nomes.append(linha)

print(lista_nomes)
'''
