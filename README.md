# python_projeto_controle_de_cotas_de_disco #
Projeto proposto pelo site <a href="https://wiki.python.org.br/ListaDeExerciciosProjetos">Python Brasil</a>


<p>A ACME Inc., uma organização com mais de 1500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço em disco ocupado pelas contas dos usuários, e identificar os usuários com maior espaço ocupado. Através de um aplicativo baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado <b>usuarios.txt</b>: </p>

![Text Alt](/imagem_1.png)

<p>Neste arquivo, o primeiro campo corresponde ao login do usuário e o segundo ao espaço em disco ocupado pelo seu diretório home. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado <b>relatório.txt</b>, no seguinte formato:</p>

![Text Alt](/imagem_2.png)

<p>O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.</p>

## Recursos adicionais: opcionalmente, desenvolva as seguintes funcionalidades: ##

1. Ordenar os usuários pelo percentual de espaço ocupado.
2. Mostrar apenas os n primeiros em uso, definido pelo usuário.
3. Gerar a saída numa página html.
4. Criar o programa que lê as pastas e gera o arquivo inicial.
