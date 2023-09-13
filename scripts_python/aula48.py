'''
Listas em python

tipo -> list (mutavel) ou seja permite a mudança de valores 

suporta varios valores de qualquer tipo

conhecimentos reutilizaveis (indices e fatiamento)

metodos uteis( append, insert, pop, del, clear, extend, +)

'''
'''
#         +01234 
#         -54321
#string = "ABCDE" cadeia de caracteres

#       [-5    -4     -3     -2      -1    ]
#       [ 0     1      2      3       4    ]
lista = [123, True, 'André', 1.2, [54,'oi']] # vemos que ela suporta qualquer tipos de dado, e uma lista dentro de outra lista

print(lista, f'seu tipo é: {type(lista)}') # verificando o tipo da lista

print(lista[2].upper(), type(lista[2])) 

print('Lista original:', lista[2]) # lista original
lista[2] = "caliari" # modificando o valor da lista no indice 2
print('Lista modificada:', lista[2]) # lista modificada
print(lista)

create, Read, Update, Delete
criar   Ler   alterar deletar

se eu mover 1 item do inicio da lista o python e eu tiver 10 mil itens 9999 itens terão que ser alterados em seus indices,
e requer muito processamento. no entando a ideia de lista é adicionar itens e retirar itens do final de uma lista.
'''

####################################################################################################
#        0  1  2  3
#lista = [10, 20, 30, 40, 50, 60, 70] # criando uma lista iteravel
# print(lista)
#numero = lista[2] # (lendo)pegando um item da lista e colocando em uma variavel 
#print(numero)

#lista[2] = 300 # alterando o valor de uma lista
#print(lista)

#del lista[2] # apagando um item da lista
#print(lista)

# adicionar mais coisas a lista(final da lista)
# lista.append(50)
# lista.pop() #no momento atual do código meu utlimo item é o 50 e pop retira esse valor sendo o ultimo da lista
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop() #no momento atual do código meu utlimo item é o 70 e pop retira esse valor sendo o ultimo da lista
# print(lista, 'Removido:', ultimo_valor)
# remover_por_indice = lista.pop(3) # removendo o item da lista cujo indice é 0 e seu valor é 10
# print(lista, 'Removido:', remover_por_indice)
###################################################################################################
'''

'''
# lista = [10, 20, 30, 40] # criando uma lista iteravel
# lista.append('André') # adicionando um item str no fim da lista
# nome = lista.pop() # capturando o ultimo item da lista e colocando o valor na variavale nome
# lista.append(12333) # adicionando outro item ao fina lda lista do tipo int 
# del lista[-1] # retirando o ultimo item da lista pelo indice negativo, quando eu n sei o numero de indices da lista, por exempl ose for uma lista mt grande
# lista.insert(100, 5) # inserindo um dado no indice 100(entende como ultimo item da lista), colocando o valor 5 neste indice 100
# print(lista[4]) # meu proximo indice é 4 e abriga o valor 5, mesmo que passado o valor 100. 
# # lista.clear() # limpa a lista inteira.
#############################################################################################################
# concatenando listas em apenas uma lista
# lista_a = [1,2,3] # criando uma lista a
# lista_b = [4,5,6] # criando uma lista b
# lista_c = lista_a + lista_b # concatenando as duas listas acima 
# print(lista_c) # printando as listas concatenadas 


# lista_a.extend(lista_b) # o método extendo n retorna nada porque ele atua no objeto ao qual esta aplicando uma ação.
# # ou seja eu n consigo pegar o a linha acima e jogar em uma variavel pq o retonro do valor é sobre o objeto alterado, no caso aqui a lista 1.
# print(lista_a)

########################################################################################################################

'''
Cuidados que precisamos ter com dados mutaveis

= -> copiando o valor(imutaveis)

= -> aponta para o mesmo valor na memória (mutavel)
'''

lista_a= ['qualquer coisa','Andre'] # variavel original que ocupa um lugar na memoria
print(lista_a)
lista_b= lista_a # variavel que aponta para o valor de lista a na memoria.

lista_a[0] = 'oi' #alterando a lista_a eu tbm altero a lista B porque indicamos para o mesmo local na memoria

print(lista_b)

# criando uma cópia dos valor para uma poutra variavel sem que apontamos o mesmo valor, evitando que alteremos todas as variaveis seguintes que referenciam este valor alocado na memoria.
lista_c = lista_a.copy()
print(lista_c)
'''
Em dados mutavel quando uso = estamso apontando para o mesmo valor na memoria,
quando são dados imutaveis a gente copia para outra variavel. 
'''




