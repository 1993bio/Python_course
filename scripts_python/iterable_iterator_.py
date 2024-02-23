import sys # importando a biblioteca sys 


# o iteravel pode ser uma lista, tupla, dicionário....
Iterable = ['Eu', 'tenho', '__iter__']

iterator = iter(Iterable) # tem __iter__ e __next__

# se passarmos isso com chaves cria uma lista com 10000 valores na memória do computador
lista = [n for n in range(10000)] # cria uma lçista com 10000 itens na memoria 

generator = (n for n in range(10000))  # cria um objeto generator em apenas um espaço na    memória sem ter salvo todos os valores dos 10000 itens.
print('tamanho do generator em bytes', sys.getsizeof(generator))
print('tamanho da lista em bytes',sys.getsizeof(lista))


# printando todos os valores
for i in generator: 
    print(i)



