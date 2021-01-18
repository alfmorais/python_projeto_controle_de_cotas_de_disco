def EscreverArquivoRelatorio(tabelaDados, somaMegaBytes, dadosMedio):
'''Função para escrever o relatorio final do problema'''

  arquivo_final = open('relatório.txt', 'w') 
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
