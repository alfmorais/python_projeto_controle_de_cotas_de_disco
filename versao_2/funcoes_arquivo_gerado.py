def leitura_arquivo_gerado(caminho):
    """Função que tem o objetivo de ler um caminho de diretório com o arquivo gerado pelo 
    programa e retornar esse conteudo em uma lista. 

    Args:
        caminho ([string]): [caminho do diretório ou path]

    Returns:
        [lista]: [lista com o conteudo do arquivo]
    """

    conteudo = []

    with open(caminho, 'r') as arquivo_dados:
        for linha in arquivo_dados:
            linha = str(linha)
            conteudo.append(linha)

    return conteudo


def limpando_dados_gerado(conteudo):
    """ Função tem como objetivo receber um parametro em forma de lista,
    fazer o tratamento de dados, tais como: Eliminando o cabeçalho do dataframe,
    eliminando os ultimos digitos, eliminando os espaços em branco e o primeiro digito. 

    Returns:
        [lista]: ['Francisco41714', 'Ygor4856']
    """

    # Eliminando o cabeçalho do dataframe
    # Eliminando os ultimos digitos
    # Eliminando os espaços em branco
    if conteudo[0] == '              Nome   Dado\n':
        del(conteudo[0])

    novo_conteudo = []

    for indice in conteudo:
        indice = indice[:-1]
        indice = indice.replace(' ', '')
        indice = indice.replace(indice[0], '')
        novo_conteudo.append(indice)

    return novo_conteudo


def lista_usuarios(novo_conteudo):
    pass


def lista_bytes(novo_conteudo):
    pass
