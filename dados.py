{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled69.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOEWYI7aVVWNvb1KhFR22T8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/alfmorais/python_projeto_controle_de_cotas_de_disco/blob/main/dados.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iSqUgItRemBk"
      },
      "source": [
        "'''\r\n",
        "08/03/2021\r\n",
        "Desenvolvedor: Alfredo de Morais\r\n",
        "Objetivo: Elaborar todas as funções que são usado no arquivo\r\n",
        "'''\r\n",
        "import pandas as pd\r\n",
        "import random as rand\r\n",
        "\r\n",
        "\r\n",
        "# Caminho do arquivo nomes.txt -> OBS: Sempre verificar o path\r\n",
        "caminho = '/content/nomes.txt'\r\n",
        "\r\n",
        "# Lista vazia para nomes\r\n",
        "nomes = []\r\n",
        "\r\n",
        "# Abrindo o arquivo nomes.txt e armazenando todos os nomes em uma lista\r\n",
        "with open(caminho, 'r') as objeto_arquivo:\r\n",
        "    arquivo = objeto_arquivo.readlines()\r\n",
        "    for linha in arquivo:\r\n",
        "        linha = linha.strip()\r\n",
        "        nomes.append(linha)\r\n",
        "\r\n",
        "# Lista de números para simular a quantidades de dados\r\n",
        "dados = list(range(99999))\r\n",
        "\r\n",
        "def dados_teste(nomes, dados, quantidade):\r\n",
        "    '''\r\n",
        "    Função que retorna a quantidade de funcionários e dados referentes ao \r\n",
        "    arquivo teste, Exemplo de uso da função:\r\n",
        "\r\n",
        "    codigo:\r\n",
        "\r\n",
        "    arquivo = dados_teste(lista, lista, int)\r\n",
        "\r\n",
        "    o retorno da função será um arquivo txt com dados selecionados de maneira \r\n",
        "    randomica. \r\n",
        "    '''\r\n",
        "\r\n",
        "    # Função random.choices para o nome e dados\r\n",
        "    lista_nome = rand.sample(nomes, quantidade)\r\n",
        "    lista_dado = rand.sample(dados, quantidade)\r\n",
        "\r\n",
        "    # Dataframe com os dados de teste\r\n",
        "    arquivo_dados = pd.DataFrame({\r\n",
        "        'Nome': lista_nome,\r\n",
        "        'Dado': lista_dado,\r\n",
        "    })\r\n",
        "\r\n",
        "    # Elaboração do arquivo txt para teste\r\n",
        "    with open('dados_de_texte.txt', 'w') as arquivo_dados_de_teste:\r\n",
        "        arquivo_dados_de_teste.write(arquivo_dados.to_string())\r\n",
        "\r\n",
        "    # Retorno do arquivo dados de teste\r\n",
        "    return arquivo_dados_de_teste"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "89rhZGL9gDZS"
      },
      "source": [
        "arquivo = dados_teste(nomes, dados, 6)"
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OpK4e3Mjiyg9"
      },
      "source": [
        "arquivo = dados_teste(nomes, dados, 10)"
      ],
      "execution_count": 16,
      "outputs": []
    }
  ]
}