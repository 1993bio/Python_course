# exercicio de unir listas como um zipper..

# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# Solução....... de criação da função. OBS: o python ja tem a função zip() que faz a mesma coisa

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2= ['BA', 'SP', 'MG', 'RJ']

# def zipper(lista1, lista2): # definindo a função que recebe duas listas como argumentos.
#     intervalo_máximo =  min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range (intervalo_máximo)
#     ]


# print(zipper(l1, l2))

# função do python

print(list(zip(l1,l2)))   #ou importanto do itertools...

# aqui ai iterar ele usa o valor da lista maior
from itertools import zip_longest

print(list(zip_longest(l1,l2, fillvalue= 'SEM CIDADE'))) # fillvalue supre um valor vazio do tipo None em python

