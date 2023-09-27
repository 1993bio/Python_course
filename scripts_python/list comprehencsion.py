# lst comprehention é uma forma rápida de criar listas

# vejamos um exemplo:
# obs: o que vem a esquerda do for é mapeamento o que vem a direita é filtro

import pprint

def p(v):
    pprint.pprint(v, sort_dicts= False, width=40)

lista=[]

for numero in range(10):
    lista.append(numero)
# print(lista)


3#  podemos fazer de outra forma  pr list comprehension

lista=[numero*2 for numero in range(10)]

print(lista)

# ------------------------------------------------------
# mapeando dados em list comprehension

produtos = [
    {'nome': 'sabão', 'preço': 20},
    {'nome': 'macarrão', 'preço': 5},
    {'nome': 'peixe', 'preço': 30},
    {'nome': 'goiaba', 'preço': 12},
]

# criando um mapeamento de listas sem função e alterando o preço dos produtos

novos_produtos = [
    {**produto, 'preço': produto['preço']*1.5} # alterando o preço do produtoe em 1.5%
    if produto['preço'] > 20 else {**produto} # if ternario para qualquer produto com preço maior  que 20 o preço do prosuto é alterado.
    for produto in produtos
]
p(novos_produtos)

# filtro de uma lista 

lista2 = [n for n in range(10) if n < 3] # criando um filtro se o numero da lista for menor que 3 faça a introduçã odele na nova lista
p(lista2)


# filtrando uma lista de produtos
novos_produtos2 = [
    # mapeamento a esquerda do for 
    {**produto, 'preço': produto['preço']*1.5} # alterando o preço do produtoe em 1.5%
    if produto['preço'] > 20 else {**produto} # if ternario para qualquer produto com preço maior  que 20 o preço do prosuto é alterado.
    for produto in produtos  # for 
    # filtro a direita do for
    if produto['preço'] > 12 
]
p(novos_produtos2)

