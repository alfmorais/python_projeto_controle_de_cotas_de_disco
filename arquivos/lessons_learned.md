# Lições Aprendidas
Esse arquivo tem como objetivo mostrar as funções, módulos e outros conhecimentos adquiridos durante o planejamento e a execução do projeto proposto. 

# Funções utilizadas no desenvolvimento do projeto: 
1. to.string(index=False) -> Essa função tem como objetivo fazer a conversão de dados em formato dataframe para string. Foi necessário fazer essa conversão para escrever os dados em um arquivo .txt e usa-lá como exemplo gerado pelo o programa, de acordo com os requisitos do software. Exemplo:

~~~python
tabela = pd.DataFrame({
  'Nome': ['Alfredo', 'Denise', 'Helena']
  'Idade': [28, 30, 1]
  'Sexo': ['M', 'F', 'F']
  })

# o argumento index=False retorna um dataframe sem os indices padrão do módulo pandas.
tabela = tabela.to_string(index=False)

# ---> Código para salvar o dataframe no arquivo.txt 
~~~

2. rand.sample() -> A função rand.sample está contida no módulo random da biblioteca padrão do python. Essa função retorna um número de valores aleatórios contido em uma lista, tuplas e sets. A quantidade de valores aleatórios é o programador que define. Exemplo:

~~~python
''' 
Sintaxe da função: 
rand.sample(colecao, k)

colecao = lista, tupla e sets
k = quantidade de vezes para gerar os valores aleatórios
'''

import random as rand

lista = list(range(1000))

valores = rand.sample(lista, 4)
print(valores)

~~~ 

3. 
4.
5.
6. 
7. 
8. 
9. 
10. 
11. 
12. 
13. 
