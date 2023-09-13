'''
desenpacotamento em chamadas de métodos e funções
'''
string = 'ABCD'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
tupla = 'Python', 'é', 'legal',

# a, b, *_, f = lista # desenpacotando as listas

# print (a, f) #printando o primeiro e ultimo item da lista

# desenpacotando no print
print('Maria', 'Helena', 1,2,3, 'Eduarda') # printando normal
print(*lista) # desta forma ele passa pro cada ite mdentro da lista e coloca em apenas uma linha
print(*string) # desta forma ele passa pro cada ite mdentro da lista e coloca em apenas uma linha
print(*tupla) # desta forma ele passa pro cada ite mdentro da lista e coloca em apenas uma linha