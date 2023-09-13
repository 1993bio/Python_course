'''
o python tem metodos para numerar valores
sem precisar criar um laço iteravel para obte-los

o metodo enumerate , enumera iteraveis

'''

lista = ['andre', 'luiz', 'caliari']
lista.append('pedro')

#lista_enumerada = enumerate(lista) # o ideal é nao criar uma nova variavel mas usar ele diretamente na lista
for item in enumerate(lista): # aqui estamos criando um iterator por vez, e o for com enumerate gera uma tupla
    indice, valor = item # desenpacotando uma lista
    print(indice,valor)
    
# simplificando
# Aqui para cada iteração do for ele separa o indice, e valor da tupla.
print('-----------simplificando-----------')
for indice, valor in enumerate(lista):
    print(indice, valor)
    
    
'''
e caso eu rcriar uma variavel e criar um laço para iterar a variavel com
o metodo enumerate, eu irei esgotar o meu iterator, ou seja, não havera masi itens iteraveis
e o melhor metodo é utilizalo na variavel que deve ser aplicada, sem que criamos uma nova variavel para receber o enumerate.
Se utilizarmos ele em uma variavel, veremos o objeto com o valor alocado na memoria at 0x212655458796 por exemplo.

pra ser usado em uma variavel teremos que converter a variavel em uma lista, porque ao usar o metodo enumerate ela vira uma tupla
vejamos

'''
#lista_enumerada = list(enumerate(lista))
#print(lista_enumerada)
# vejamos uma lista com varias tuplas com seus indices (enumerate) e seus valores

