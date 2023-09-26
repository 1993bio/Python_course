# aqui realizamos um exempl ode uma função lambda, ou seja funções sem nomes que recebe operações em apenas uma linha.

# ordenando uma lista pelo método sort, obse o metodo sorted tambem realiza a mesma operação 

# lista = [5, 9, 8, 7, 4, 6, 5, 6, 2, 1, 2, 5, 5, 8] # uma lista com numeros aleatórios
# lista.sort(reverse=True) # este é o primeiro modo, e podemos passar parametros como o "reverse para ordenar ao contrario"
# print(lista) # printa a lista acima de traz para frente 

# print(sorted(lista, reverse= False)) # segundo modo de ordenação de listas 

# o python não consegue ordenar dicionarios, uma vez que faz comparação logica utilizando > que, < que em listas, ja em dicionários as coisas mudam um pouco, por exemplo por nome ou sobrenome utilizando as funções acima para isso precisamos criar uma função para que o processo seja executado.


# um dicionário com nomes e sobrenomes
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda', 'idade': 10},
    {'nome': 'Andre', 'sobrenome': 'Caliari', 'idade': 5},
    {'nome': 'Pedro', 'sobrenome': 'Goto', 'idade': 1},
]
# -------------------------------------------------------------------------------------------------------------------
# ORDENANDO POR FUNÇÃO 

# # a funçã orecebe um parametro ou seja o item e retorna este item dado o "nome"
# def ordena(item):
#     return item['nome'] # em key podemos passar as chaves dos dicionários para ele poder ordenar por exemplo pelo sobrenome

# lista.sort(key=ordena) # o sorted recebe a função ordena em key, que busca a chave nome e ordena o dicionario por nome

# for item in lista: # para cadas item da lista print o item ordenado
#     print(item)

# ----------------------------------------------------------------------------------------------------------------
print("*"*40)
#ORDENANDO PELA FUNÇÃO lAMBDA

def exibir(lista):
    for item in lista:
        print(item)



#l0= lista.sort(key=lambda i: i['idade']) # dentro de sort passamos uma expressão lamda que facilita a criação de funçõe
# aqui passamos a função lambda para ordenar pela idade

# utilizando o metodo sorted (retorna uma nova copia rasa da lista atribuida a função)

l1= sorted(lista, key=lambda i: i['nome']) # ordena pelo nome
l2 = sorted(lista, key=lambda i: i['idade']) # ordena pela idade


exibir(l1)
print("*"*40)
exibir(l2)





