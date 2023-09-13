'''
Exercicio de listas
exiba os indices da lista
0 Andre
1 Maria
2 Luiz
'''

lista = ['Andre', 'Maria', 'Luiz']
lista.append('Ana')
lista.append('Pedro')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    
