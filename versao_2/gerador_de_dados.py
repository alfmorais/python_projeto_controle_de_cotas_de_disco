'''
08/03/2021

Desenvolvedor: Alfredo de Morais
Objetivo: Elaborar todas as funções que são usado no arquivo

'''
import re
import pandas as pd

caminho = 'C:/Users/Alfredo/AppData/Local/Programs/Python/Python39/python_projeto_controle_de_cotas_de_disco/versao_2/nomes.txt'

nomes = []

with open(caminho, 'r') as objeto_arquivo:
    arquivo = objeto_arquivo.readlines()
    for linha in arquivo:
        linha = linha.strip()
        nomes.append(linha)

print(nomes)
