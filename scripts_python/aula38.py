'''
Repetições While
Executando uma ação até que uma condição seja verdadeira
Usando o continue => termina o laço, quando o laço bater no continue ele volta a executar o laço naquele momento deixando de executar o restante do código
'''

qtd_linhas = 5
qtd_colunas = 5

linha = 1
# para cada 1 volta do while eu tenho outras 5 voltas do while interno.
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('acabou')